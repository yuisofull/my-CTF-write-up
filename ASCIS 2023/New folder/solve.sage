def coron(pol, X, Y, k=2, debug=False):
    """
    Returns all small roots of pol.

    Applies Coron's reformulation of Coppersmith's algorithm for finding small
    integer roots of bivariate polynomials modulo an integer.

    Args:
        pol: The polynomial to find small integer roots of.
        X: Upper limit on x.
        Y: Upper limit on y.
        k: Determines size of lattice. Increase if the algorithm fails.
        debug: Turn on for debug print stuff.

    Returns:
        A list of successfully found roots [(x0,y0), ...].

    Raises:
        ValueError: If pol is not bivariate
    """

    if pol.nvariables() != 2:
        raise ValueError("pol is not bivariate")

    P.<x,y> = PolynomialRing(ZZ)
    pol = pol(x,y)

    # Handle case where pol(0,0) == 0
    xoffset = 0

    while pol(xoffset,0) == 0:
        xoffset += 1

    pol = pol(x+xoffset,y)

    # Handle case where gcd(pol(0,0),X*Y) != 1
    while gcd(pol(0,0), X) != 1:
        X = next_prime(X, proof=False)

    while gcd(pol(0,0), Y) != 1:
        Y = next_prime(Y, proof=False)

    pol = P(pol/gcd(pol.coefficients())) # seems to be helpful
    p00 = pol(0,0)
    delta = max(pol.degree(x),pol.degree(y)) # maximum degree of any variable

    W = max(abs(i) for i in pol(x*X,y*Y).coefficients())
    u = W + ((1-W) % abs(p00))
    N = u*(X*Y)^k # modulus for polynomials

    # Construct polynomials
    p00inv = inverse_mod(p00,N)
    polq = P(sum((i*p00inv % N)*j for i,j in zip(pol.coefficients(),
                                                 pol.monomials())))
    polynomials = []
    for i in range(delta+k+1):
        for j in range(delta+k+1):
            if 0 <= i <= k and 0 <= j <= k:
                polynomials.append(polq * x^i * y^j * X^(k-i) * Y^(k-j))
            else:
                polynomials.append(x^i * y^j * N)

    # Make list of monomials for matrix indices
    monomials = []
    for i in polynomials:
        for j in i.monomials():
            if j not in monomials:
                monomials.append(j)
    monomials.sort()

    # Construct lattice spanned by polynomials with xX and yY
    L = matrix(ZZ,len(monomials))
    for i in range(len(monomials)):
        for j in range(len(monomials)):
            L[i,j] = polynomials[i](X*x,Y*y).monomial_coefficient(monomials[j])

    # makes lattice upper triangular
    # probably not needed, but it makes debug output pretty
    L = matrix(ZZ,sorted(L,reverse=True))

    if debug:
        print("Bitlengths of matrix elements (before reduction):")
        print(L.apply_map(lambda x: x.nbits()).str())

    L = L.LLL()

    if debug:
        print("Bitlengths of matrix elements (after reduction):")
        print(L.apply_map(lambda x: x.nbits()).str())

    roots = []

    for i in range(L.nrows()):
        if debug:
            print("Trying row {}".format(i))

        # i'th row converted to polynomial dividing out X and Y
        pol2 = P(sum(map(mul, zip(L[i],monomials)))(x/X,y/Y))

        r = pol.resultant(pol2, y)

        if r.is_constant(): # not independent
            continue

        for x0, _ in r.univariate_polynomial().roots():
            if x0-xoffset in [i[0] for i in roots]:
                continue
            if debug:
                print("Potential x0:",x0)
            for y0, _ in pol(x0,y).univariate_polynomial().roots():
                if debug:
                    print("Potential y0:",y0)
                if (x0-xoffset,y0) not in roots and pol(x0,y0) == 0:
                    roots.append((x0-xoffset,y0))
    return roots

def main():
    pbits = 1042
    qbits = 1044

    a=182536
    b=732597
    n=3964970058588757148381961704143056706462468814335020245520977895524549102412775370911197710398920529632256746343939593559572847418983212937475829291172342816906345995624544182017120655442222795822907477729458438770162855927353619566468727681852742079784144920419652981178832687838498834941068480219482245959017445310420267641793085925693920024598052216950355088176712030006651946591651283046071005648582501424036467542988971212512830176367114664519888193885765301505532337644978456428464159474089450883733342365659030987687637355512103402573155030916404165387863932234088255017821889649456947853403395704387479968208359004918561

    pbar=int(sqrt((n*a)//b))

    lbits=510
    ln = 2^lbits
    p_length=1042
    q_length=1044
    p_high=pbar//ln
    
    p0=p_high
    print()
    print('Given:')
    print('n =',n)
    print('p0 =',p0)

    # Recovery starts here
    q0 = floor(n / (p0*ln))//ln
    print("q0 bit lengths: ", len(bin(q0))-2)
    X = Y = 2^(lbits+2) # bounds on x0 and y0
    P.<x,y> = PolynomialRing(ZZ)
    # Should have a root at (x0,y0) +/- some bits of q0
    pol = (x+p0*ln)*(y+q0*ln) - n

    x0_2, y0_2 = coron(pol, X, Y, k=2, debug=True)[0]
    p_2 = p0*ln + x0_2
    q_2 = q0*ln + y0_2

    print()
    print('Recovered:')
    print('x0 =',x0_2)
    print('y0 =',y0_2)
    print('p =',p_2)
    print('q =',q_2)

if __name__ == '__main__':
    main()

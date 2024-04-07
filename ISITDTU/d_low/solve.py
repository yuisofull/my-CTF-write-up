from Crypto.Util.number import *
from tqdm import tqdm
import itertools
# https://github.com/defund/coppersmith/blob/master/coppersmith.sage
#load('coppersmith.sage')


e = 12721
n = ...
c = ...
d_low = 0x4443b9e8a46a89efba588e8dca4608b9f8a74d836bdd57518556070703843499
p_high = 0x9e5675d8e41aa7ac7f05847aab69a685ebbe3d1c587139e3e4695d71dbe37ed7
p_mid = 0x7539d7ffd1cfada6e2bfb4905aa4e3cd782f2b0817c433003a5737fae8e82625f

t = len(bin(d_low)) - 2
for k in tqdm(range(1, e)):
    PR.<x> = PolynomialRing(Zp(2, t))
    f = x + k*(n*x - x**2 - n + x) - x*e*d_low 
    for p_low, _ in f.roots():
        p_low = ZZ(p_low)
        PR.<x0, x1> = PolynomialRing(Zmod(n), 2)
        f = p_low + 16**192*p_high + 16**95*p_mid + 16**64*x0 + 16**160*x1
        roots = small_roots(f, bounds=(16**32, 16**31), m=2, d=3)
        if roots == []:
            continue
        p = int(f(roots[0]))
        q = n//p
        d = pow(e, -1, (p-1)*(q-1))
        flag = int(pow(c, d, n))
        print(long_to_bytes(flag))
        quit()
        
def small_roots(f, bounds, m=1, d=None):
	if not d:
		d = f.degree()

	if isinstance(f, Polynomial):
		x, = polygens(f.base_ring(), f.variable_name(), 1)
		f = f(x)

	R = f.base_ring()
	N = R.cardinality()
	
	f /= f.coefficients().pop(0)
	f = f.change_ring(ZZ)

	G = Sequence([], f.parent())
	for i in range(m+1):
		base = N^(m-i) * f^i
		for shifts in itertools.product(range(d), repeat=f.nvariables()):
			g = base * prod(map(power, f.variables(), shifts))
			G.append(g)

	B, monomials = G.coefficient_matrix()
	monomials = vector(monomials)

	factors = [monomial(*bounds) for monomial in monomials]
	for i, factor in enumerate(factors):
		B.rescale_col(i, factor)

	B = B.dense_matrix().LLL()

	B = B.change_ring(QQ)
	for i, factor in enumerate(factors):
		B.rescale_col(i, 1/factor)

	H = Sequence([], f.parent().change_ring(QQ))
	for h in filter(None, B*monomials):
		H.append(h)
		I = H.ideal()
		if I.dimension() == -1:
			H.pop()
		elif I.dimension() == 0:
			roots = []
			for root in I.variety(ring=ZZ):
				root = tuple(R(root[var]) for var in f.variables())
				roots.append(root)
			return roots

	return []
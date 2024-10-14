import sympy

def gauss():

    b = 74 * 4
    half_b = b // 2

    m = [[0] * (b + 1) for _ in range(b + 10)]
    print("Col: ", len(m[0]))
    print("Row: ", len(m))

    with open("output.txt", "r") as f:
        for i, line in enumerate(f):
            bits = int(line, 16)

            ## example: 1101 -> [-1, -1, 1, -1], half_b = 2 -> cnt = 2 - 3 = -1
            cnt = half_b
            for j in range(b):
                if bits >> j & 1:
                    cnt -= 1
                    m[i][j] = -1
                else:
                    m[i][j] = 1
            m[i][-1] = cnt

            # +2 for safety
            # break if i = b + 2 = 298
            if i >= b + 2:
                break

    M = sympy.Matrix(m)
    # print("M: \n", M)
    M_rref = M.rref()

    # print("M_rref: \n", M_rref)
    for i in range(10):
        print(str(int(M_rref[0][i, -1])))

    s = []
    for i in range(b):
        s.append(str(int(M_rref[0][i, -1])))
    s = "".join(s[::-1])
    # binary to ascii
    print("".join(chr(int(s[i:i+8], 2)) for i in range(0, len(s), 8)))
    
gauss()


import sympy

def gauss():

    b = 74 * 4
    half_b = b // 2

    m = [[0] * (b + 1) for _ in range(b + 10)]


    with open("output.txt", "r") as f:
        for i in range(1000000):
            print(i)
            line = f.readline().strip()
            bits = int(line, 16)

            cnt = half_b
            for j in range(b):
                if bits >> j & 1:
                    cnt -= 1
                    m[i][j] = -1
                else:
                    m[i][j] = 1
            m[i][-1] = cnt

            # +2 for safety
            if i >= b + 2:
                i+=1
                break
            i+=1

    M = sympy.Matrix(m)
    M_rref = M.rref()

    for i in range(10):
        print(str(int(M_rref[0][i, -1])))

    s = []
    for i in range(b):
        s.append(str(int(M_rref[0][i, -1])))
    s = "".join(s)
    reverse_s = s[::-1]
    # binary to ascii
    print("".join(chr(int(s[i:i+8], 2)) for i in range(0, len(s), 8)))
    print("".join(chr(int(reverse_s[i:i+8], 2)) for i in range(0, len(reverse_s), 8))   )
    
gauss()


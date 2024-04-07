from Crypto.Util.number import *

def nextPrime(p, n):
    # p = kn + r
    # (n - p) % n = -p % n = -r % n = n - r
    p += (n - p) % n # p = kn + r + n - r = kn + n = n(k + 1)
    p += 1 # p = n(k + 1) + 1
    iters = 0
    while not isPrime(p):
        p += n
    return p

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


flag = bytes_to_long(open('flag.txt', 'rb').read().strip())
p = getPrime(512) # p = kn + r
q = nextPrime(p, factorial(90)) # q = kn + 1
N = p * q # N = (k1n + r)(k2n + 1) 
e = 65537
c = pow(flag, e, N)
print(N, e, c)
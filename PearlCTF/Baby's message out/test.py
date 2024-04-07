import sys
from Crypto.Util.number import getPrime, isPrime, bytes_to_long

n = pow(10, 5)
sys.setrecursionlimit(n)

def nextPrime(p):
    if isPrime(p):
        return p
    else:
        return nextPrime(p + 61)

p = getPrime(256) #p 
q = nextPrime(nextPrime(17*p + 1) + 3) #17p
r = nextPrime(29*p*q) #29*17*p^2
s = nextPrime(q*r + p) #29*17*17*p^3 + p 
t = nextPrime(r*s*q) #(29*17*17*p^3 + p)*29*17*17*p^3

n = p*q*r*s*t #29*17*17*p^4*(29*17*17*p^3 + p)*(29*17*17*p^3 + p)*29*17*17*p^3

print(n)
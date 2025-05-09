# **Mayday Mayday**

Difficulty: Medium

## Given

`source.py`

```python
from Crypto.Util.number import getPrime, GCD, bytes_to_long
from secret import FLAG
from random import randint

class Crypto:
    def __init__(self, bits):
        self.bits = bits
        self.alpha = 1/9
        self.delta = 1/4
        self.known = int(self.bits*self.delta) #512
    
    def keygen(self):
        while True:
            p, q = [getPrime(self.bits//2) for _ in '__']
            self.e = getPrime(int(self.bits*self.alpha))
            φ = (p-1)*(q-1)
            try:
                dp = pow(self.e, -1, p-1)
                dq = pow(self.e, -1, q-1)
                self.n = p*q
                break
            except:
                pass

        return (self.n, self.e), (dp, dq)

    def encrypt(self, m):
        return pow(m, self.e, self.n)

rsa = Crypto(2048)
_, (dp, dq) = rsa.keygen()

m = bytes_to_long(FLAG)
c = rsa.encrypt(m)

with open('output.txt', 'w') as f:
    f.write(f'N = 0x{rsa.n:x}\n')
    f.write(f'e = 0x{rsa.e:x}\n')
    f.write(f'c = 0x{c:x}\n')
    f.write(f'dp = 0x{(dp >> (rsa.bits//2 - rsa.known)):x}\n') #512
    f.write(f'dq = 0x{(dq >> (rsa.bits//2 - rsa.known)):x}\n') #512
```

`output.txt`

```
N = 0x...
e = 0x...
c = 0x...
dp = 0x...
dq = 0x...
```

## Analysis

This is clearly an RSA cryptosystem challenge with 2048-bit key size. As usual, we are given `n`, `c`, and `e`. Additionally, we are given the 512 most significant bits (MSB) of `dp` and `dq`.

## Solution

Compared to the challenge `grhkm’s babyRSA - Bauhinia CTF 2023`, which gave the least significant bits (LSB) of `dp` and `dq`, this one is easier since we have MSBs, as explained in [this paper](https://eprint.iacr.org/2022/271.pdf).

The idea is based on:

We know: `e * dp = 1 + k(p-1)` and `e * dq = 1 + k(q-1)`.

Section 3.1 of the paper gives this formula:
`kl = (2^(2*512) * e^2 * dp * dq) / N`

Also:
`k + l = 1 - kl(N - 1) mod e`

With `k + l` and `kl`, we can find `k` and `l` as the roots of:
`(x - k)(x - l) = 0`
=> `x^2 - (k + l)x + kl = 0 mod e`
=> `x^2 - (1 - kl(N - 1))x + kl = 0 mod e`

After finding `k` and `l`, Lemma 3 in section 3.3 allows us to recover the remaining bits of `dp`, and factor `N` using GCD.

We define:
`f(x) = x + ed_pM * 2^i + k - 1 mod (k * N)`
Then:
`p = gcd(f(dp_low), N)`

## Solve script

```python
from Crypto.Util.number import long_to_bytes

# [Paste the full values of n, e, c, dp_high, dq_high here]

kl = ((e**2) * dp_high * dq_high * 2**1024) // n + 1

R.<x> = PolynomialRing(GF(e))
f = x^2 - (1 - kl*(n - 1)) * x + kl
k = int(f.roots()[0][0])

R.<x> = PolynomialRing(Zmod(k * n))
i = 512
f = e * (dp_high * (2**i)) + e * x + k - 1

dp_low = f.monic().small_roots(X=2**i, beta=0.4)[0]
p = gcd(int(f(dp_low)), n)
q = n // p
d = pow(e, -1, (p - 1) * (q - 1))
flag = long_to_bytes(int(pow(c, d, n)))
print(flag.decode())

# HTB{f4ct0r1ng_w1th_just_4_f3w_b1ts_0f_th3_CRT_3xp0n3nts!https://eprint.iacr.org/2022/271.pdf}
```

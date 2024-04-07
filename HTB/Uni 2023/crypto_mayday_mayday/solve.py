import itertools
from Crypto.Util.number import long_to_bytes


n = 0x78fb80151a498704541b888b9ca21b9f159a45069b99b04befcb0e0403178dc243a66492771f057b28262332caecc673a2c68fd63e7c850dc534a74c705f865841c0b5af1e0791b8b5cc55ad3b04e25f20dedc15c36db46c328a61f3a10872d47d9426584f410fde4c8c2ebfaccc8d6a6bd1c067e5e8d8f107b56bf86ac06cd8a20661af832019de6e00ae6be24a946fe229476541b04b9a808375739681efd1888e44d41196e396af66f91f992383955f5faef0fc1fc7b5175135ab3ed62867a84843c49bdf83d0497b255e35432b332705cd09f01670815ce167aa35f7a454f8b26b6d6fd9a0006194ad2f8f33160c13c08c81fe8f74e13e84e9cdf6566d2f
e = 0x4b3393c9fe2e50e0c76920e1f34e0c86417f9a9ef8b5a3fa41b381355
c = 0x17f2b5a46e4122ff819807a9d92b6225c483cf93c9804381098ecd6b81f4670e94d8930001b760f1d26bc7aa7dda48c9e12809d20b33fdb4c4dd9190b105b7dab42e932b99aaff54023873381e7387f1b2b18b355d4476b664d44c40413d82a10635fe6e7322543943aed2dcfbe49764b8da70edeb88d6f63ee47f025be5f2f38319611ab74cd5db6f90f60870ecbb57a884f821d873db06aadf0e61ff74cc7d4c8fc1e527dba9b205220c6707f750822c675c530f8ad6956e41ab80911da49c3d6a7d27e93c44ba5968f2f47a9c5a2694c9d6da245ceffe9cab66b6043774f446b1b08ee4739d3cc716b87c8225a84d3c4ea2fdf68143d09f062c880a870554
dp_high = 0x59a2219560ee56e7c35f310a4d101061aa61e0ae4eae7605eb63784209ad488b4ed161e780811edd61bf593e2d385beccfd255b459382d8a9029943781b540e7
dq_high = 0x39719131fbfd8afbc972ca005a430d080775bf1a5b3e8b789aba5c5110a31bd155ff13fba1019bb6cb7db887685e34ca7966a891bfad029b55b92c11201559e5


kl=((e**2)*dp_high*dq_high*2**1024)//n+1
print(kl)


R.<x> = PolynomialRing(GF(e))

f=x^2-(1-kl*(n-1))*x+kl
k=int(f.roots()[0][0])
# print(f.roots())

R.<x> = PolynomialRing(Zmod(k*n))
i=512
f=e*(dp_high*(2**i))+e*x+k-1

dp_low=f.monic().small_roots(X=2**i,beta=0.4)[0]

p = gcd(int(f(dp_low)), n)
q = n//p
d = pow(e, -1, (p-1)*(q-1))
flag = long_to_bytes(int(pow(c, d, n)))
print(flag.decode())

# k=int((-b+sqrt(de))/2*a)

# l=int((-b-sqrt(de))/2*a)

# print(k,l)
# PR.<k, l> = PolynomialRing(Zmod(e))

# f = k+l-1+k*l*(n-1)

# k, l = defund_multivariate(f, bounds=(e,e), m=1, d=1)[0]
# k, l = int(k), int(l)

# print(k,l)

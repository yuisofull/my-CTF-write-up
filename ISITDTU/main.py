from Crypto.Util.number import *
from tqdm import tqdm
from sage.all import pari

def mod_nth_root(x, e, n):
    r, z = pari(f"r = sqrtn(Mod({x}, {n}), {e}, &z); [lift(r), lift(z)]")
    r, z = int(r), int(z)
    roots = [r]
    if z == 0:
        return roots
    t = r
    while (t := (t*z) % n) != r:
        roots.append(t)
    return roots

print(mod_nth_root(8,3,15))
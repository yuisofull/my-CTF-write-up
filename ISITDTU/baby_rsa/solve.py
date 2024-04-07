def mod_roots(x, e, p):
    return GF(p)(x).nth_root(e, all=True)

for r3 in tqdm(mod_roots(c, e3, p3)):
    for r2 in mod_roots(r3, e2, p2):
        for r1 in mod_roots(r2, e1, p1):
            try:
                print(long_to_bytes(int(r1)).decode())
            except:
                continue
for i in range(12):
    print(block1)
    block1 = block1[:i] + bytes(block1[i] ^ c[i]) + block1[i + 1 :]
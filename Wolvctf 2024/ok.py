from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16

def reverse():
    with open('eWolverine.bmp', 'rb') as w, open('eFlag.bmp', 'rb') as f, open('./wolverine.bmp', 'rb') as o:
        e_wolverine = w.read()
        e_flag = f.read()
        original_wolverine = o.read()

    with open('dFlag.bmp', 'wb') as d:
        d.write(e_flag[:55])

        for i in range(55, len(e_wolverine), BLOCK_SIZE):
            KEY = bytes(a^b for a, b in zip(e_wolverine[i:i+BLOCK_SIZE], original_wolverine[i:i+BLOCK_SIZE]))
            d.write(bytes(a^b for a, b in zip(e_flag[i:i+BLOCK_SIZE], KEY)))

reverse()
from PIL import Image
from itertools import cycle

def xor(a, b):
    return [i^j for i, j in zip(a, cycle(b))]

# f = open("original.png", "rb").read()
f = open("enc.txt", "rb").read()

# print(f[8],f[16],f[24])
# i=0
# while True:
#     if f[24]^i==f[16]^i:
#         print(i)
#         break
    
#print([f[i]^f[i+8] for i in range(8)])
key = [0x89,0x50,0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]

#key = [f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7]]

enc = bytearray(xor(f,key))

open('test.png', 'wb').write(enc)
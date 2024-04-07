import numpy as np
import random

# def encrypt(p,key):
#     return ''.join(chr(4*i*i+3*i+7) for i in key)

# polyc = [4,3,7]
# poly = np.poly1d(polyc)

# 1
# polyc = [4,3,7]
# poly = np.poly1d(polyc)

# def encrypt(key):
#     return ''.join(chr(4*i*i+3*i+7) for i in key)
# key = open('encoded_key.txt', 'rb').read()
# enc = encrypt(poly, key)
# print(enc)

from itertools import product
#from itsdangerous import base64_decode, base64_encode
from tqdm import tqdm
import numpy as np
import random

polyc = [4,3,7]
poly = np.poly1d(polyc)
def encrypt(p,key):
    # 
    return ''.join(chr(p(i)) for i in key)

dic={}
for new_key in tqdm(product(range(256))):
    key=bytes(new_key)
    enc = encrypt(poly,key)
    dic[enc] = key
#example_enc = "☞➭⥄⫣Ⲋ⸹⿰ㆯ㍶☞⒗☞☞☞➭☞⥄☞⫣☞Ⲋ☞⸹☞⿰☞ㆯ☞㍶➭⒗➭" #open('encoded_key.txt', 'rb').read()
p=b''
for i in range(1,20):#example_enc:
    p+=dic[i]
print(p)
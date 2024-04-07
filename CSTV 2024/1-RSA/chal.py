from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import sympy
from secret import FLAG


p = sympy.randprime(2**1023,2**1024)
q = sympy.nextprime(p)
n = p*q
e = 65537

publicKey = RSA.construct((n, e))
publicKey.export_key('PEM')


cipher = PKCS1_v1_5.new(publicKey)
ciphertext = cipher.encrypt(FLAG)

f = open('mykey.pem','wb')
f.write(publicKey.export_key('PEM'))
f.close()

c = open("ciphertext","wb")
c.write(ciphertext)
c.close()

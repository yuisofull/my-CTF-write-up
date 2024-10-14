from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import socketserver, signal, json, os, re, sys
from io import StringIO

def encrypt(key,iv,message):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher.encrypt(pad(message,16)).hex()


def decrypt(key,token):
	iv = bytes.fromhex(token[:32].decode())
	ct = bytes.fromhex(token[32:].decode())
	cipher = AES.new(key, AES.MODE_CBC, iv)
	dec = cipher.decrypt(ct)
	return dec

key = os.urandom(16)
iv = os.urandom(16)

msg = b"{'username':'guest_user','role':0}"
print(json.loads(decrypt(key, (iv.hex()+encrypt(key,iv,msg)).encode())))
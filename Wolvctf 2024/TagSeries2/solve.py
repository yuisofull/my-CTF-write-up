import pwn
def xor(x, y):
    return bytes(a ^ b for a, b in zip(x, y))

r=pwn.remote("tagseries2.wolvctf.io", 1337)
r.recv()
msg = b"GET: flag.txt" #len == 13

r.sendline(msg+b'a'*3)
# 1stblock = enc(iv ^ msg1)
# 2ndblock = enc(enc(iv ^ msg1) ^ 16.to_bytes())
r.sendline()
cipherBlock1 = r.recv()[:-1]
r.sendline(msg+b'b'*3)
# 1stblock = enc(iv ^ msg2)
# 2ndblock = enc(enc(iv ^ msg2) ^ 16.to_bytes())
r.sendline()
cipherBlock2 = r.recv()[:-1]
print(cipherBlock1)
print(cipherBlock2)
print(len(msg+b'a'*3 + b'\0'*16))
r.sendline(msg+b'a'*3 + len(msg+b'b'*3).to_bytes(16, "big") + b'\0'*16)
# 1stblock = enc(iv ^ msg1)
# 2ndblock = enc(enc(iv ^ msg1) ^ 16.to_bytes())
# 3rdblock = enc(enc(enc(iv ^ msg1) ^ 16.to_bytes()))
# 4thblock = enc(enc(enc(enc(iv ^ msg1) ^ 16.to_bytes())) ^ 48.to_bytes())
# -> 4thblock
r.sendline()
tag = r.recv()[:-1]
print(tag)
r.sendline(msg+b'b'*3 + len(msg+b'b'*3).to_bytes(16, "big") +xor(xor(cipherBlock1,cipherBlock2),b'\0'*16))
# 1stblock = enc(iv ^ msg2)
# 2ndblock = enc(enc(iv ^ msg2) ^ 16.to_bytes())
# xor = enc(enc(iv ^ msg1) ^ 16.to_bytes()) ^ enc(enc(iv ^ msg2) ^ 16.to_bytes())
# 3rdblock = enc(enc(enc(iv ^ msg2) ^ 16.to_bytes()) ^ xor)
# 4thblock = enc(enc(enc(enc(iv ^ msg2) ^ 16.to_bytes()) 
# ^ enc(enc(iv ^ msg1) ^ 16.to_bytes()) ^ enc(enc(iv ^ msg2) ^ 16.to_bytes())) ^ 48.to_bytes())
r.sendline(tag)
print(r.recv())
print(r.recv())
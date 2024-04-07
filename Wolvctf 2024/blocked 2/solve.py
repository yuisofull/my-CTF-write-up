from pwn import *
from Crypto.Util.strxor import strxor

#nc blocked2.wolvctf.io 1337
r=remote('blocked2.wolvctf.io',1337)
r.recvuntil(b'you have one new encrypted message:\n')
enc=r.recvline().strip().decode()

msg = bytes.fromhex(enc)
iv = msg[:16]
blocks1 = [msg[i:i+16] for i in range(0, len(msg), 16)]

r.recvuntil(b'> ')
r.sendline(iv.hex().encode())
flag=b""
for block in blocks1[1:]:
    enc2 = r.recvline().strip().decode()
    msg2 = bytes.fromhex(enc2)
    enc_iv=msg2[32:]
    de_block=strxor(enc_iv,block)
    flag+=de_block
    print(flag)
    r.recvuntil(b'> ')
    r.sendline(de_block.hex().encode())
    
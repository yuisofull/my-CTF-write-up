from pwn import *

p = remote("blocked1.wolvctf.io", 1337)
p.recvuntil(b"you are logged in as: ")
guest = p.recvline().strip().decode()

print(guest)

p.recvuntil(b"> ")
p.sendline(b"2")

check = p.recvline().decode().strip()
print(check)

token = bytes.fromhex(check)

iv = token[:16]
block1 = token[16:32]
blocks = token[32:]

ori=guest.encode()
want = b"doubledelete"
# print(block1)
new_block1 = b""
for i in range(12):
    new_block1 += (block1[i] ^ want[i] ^ ori[i]).to_bytes(1, byteorder='big')
    print(len(new_block1))

token = (iv + new_block1 + token[28:]).hex()

print(token.encode())

p.recvuntil(b"> ")
p.sendline(b"1")
p.recvuntil(b"token > ")

p.sendline(token.encode())

print(p.recvline())


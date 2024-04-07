from pwn import *

# nc tagseries1.wolvctf.io 1337
r = remote('tagseries1.wolvctf.io', 1337)

print(r.recvline())

# Send the message
r.sendline(b'GET FILE: flag.txt'+b'x'*14+b'o'*16 + b't'*16)
r.sendline(b'x'*16)

tag=r.recvline().strip()
print(tag)

# Send the message
r.sendline(b'GET FILE: flag.txt'+b'x'*14 + b't'*16)
r.sendline(tag)

print(r.recvline())
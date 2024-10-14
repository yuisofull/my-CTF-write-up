from pwn import *
from Crypto.Util.Padding import pad
r = remote("chal.competitivecyber.club", 6001)

flag =b"zf58}"
len_flag = 13
while True:
    payload = b"A" * 5 + b"A" * len(flag)
    r.recvuntil(b"Send challenge > ")
    r.send(payload)
    r.recvuntil(b"Response > ")
    ct = r.recvline().strip().strip(b'\n')
    ct = ct.decode()
    for j in range(32, 128):
        for i in range(32, 128):
            print(i, j)
            payload = bytes([i, j]) + flag
            payload = pad(payload, 16)
            r.recvuntil(b"Send challenge > ")
            print(payload)
            r.send(payload)
            r.recvuntil(b"Response > ")
            ct2 = r.recvline().strip().strip(b'\n')
            ct2 = ct2.decode()
            if ct2[:32] == ct[32:64]:
                flag = bytes([i, j]) + flag
                print("flag:", flag)
                break
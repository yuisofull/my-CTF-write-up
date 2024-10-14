from pwn import *
from Crypto.Util.Padding import pad

r = remote('chal.competitivecyber.club', 6001)
flag = b"zf58}"
len_flag = 13
found_bytes = 0

# while found_bytes < len_flag:
#     payload = b"a"*4 + b"a"*(found_bytes) + b"a"*(len_flag - found_bytes)
#     r.recvuntil(b"Send challenge > ")
#     r.send(payload)
#     r.recvuntil(b"Response > ")
#     ct = r.recvline().strip()
#     ct = bytes.fromhex(ct.decode())

#     for j in range(256):
#         print(j)
#         payload = bytes([j]) + flag
#         payload = pad(payload, 16)
#         r.recvuntil(b"Send challenge > ")
#         r.send(payload)
#         r.recvuntil(b"Response > ")
#         ct2 = r.recvline().strip()
#         ct2 = bytes.fromhex(ct2.decode())

#         if ct2[:16] == ct[16:32]:
#             flag = bytes([j]) + flag
#             print(flag)
#             found_bytes += 1
#             break
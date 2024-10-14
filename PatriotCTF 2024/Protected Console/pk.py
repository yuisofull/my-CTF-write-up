from pwn import *
# from tqdm import tqdm, trange
context.log_level = 'debug'
# context.timeout = 100000000
# Connect to the server
# nc chal.competitivecyber.club 6002
r = remote("chal.competitivecyber.club", 6002)
# r=remote('localhost',1337)
# r.settimeout(1000000)
# Receive the initial message
r.recvuntil(b"Guest: ")
ct = r.recvline().strip().decode()
iv = bytes.fromhex(ct[:32])
ct = bytes.fromhex(ct[32:])

# message recieved: {'username':'gue st_user','role': 0}\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e
# target:           {'username':'adm inistrative_user ','role':1}\x05\x05\x05\x05\x05
# c2 ^ d3 = p3
block1 = ct[0:16]
block2 = ct[16:32]
block3 = ct[32:48]


def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


# target block2
target_block2 = xor(
    xor(
    block2, 
    b'","role":1}\x05\x05\x05\x05\x05'),
    # b"','role':1}\x05\x05\x05\x05\x05"),
    b"0}\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e")

# p2 = c1 ^ d2
# we want to find d2 using oracle padding attack
d2 = b""
r.recvuntil(b"): ")

# pbar = tqdm(total=32)
while len(d2) < 16:
    for i in range(256):
        current_block1 = (
            block1[: 16 - len(d2) - 1]
            + bytes([i])
            + xor(bytes([len(d2) + 1] * len(d2)), d2)
        )
        r.send((iv.hex() + current_block1.hex() + target_block2.hex()).encode())
        try:
            # sleep(0.1)
            ok = r.recvuntil(b"): ")
        except:
            print("Timeout: ", d2)
            exit()
        # print(ok)
        if b"Error!" not in ok:
            d2 = bytes([i ^ (len(d2) + 1)]) + d2
            # Double check
            # print("Check: ")
            # print(xor(current_block1[16-len(d2):], d2))
            # pbar.update(1)
            break
        if i == 255:
            print("Error: ", d2)
            exit()

print("d2: ", d2)

# p2 = c1 ^ d2
#  we want p2 = inistrative_user
# so c1 = c1 ^ p2 ^ inistrative_user
current_p2 = xor(block1, d2)
target_block1 = xor(xor(
    current_p2,
    b"inistrative_user"),
    block1)

# we want to find d1 using oracle padding attack
# r.recvuntil(b"): ")
d1 = b""
while len(d1) < 16:
    for i in range(256):
        current_iv = (
            iv[: 16 - len(d1) - 1]
            + bytes([i])
            + xor(bytes([len(d1) + 1] * len(d1)), d1)
        )
        r.send((current_iv.hex() + target_block1.hex()).encode())
        try:
            # sleep(0.1)
            ok = r.recvuntil(b"): ")
        except:
            print("Timeout: ", d1)
            exit()
        if b"Error!" not in ok:
            d1 = bytes([i ^ (len(d1) + 1)]) + d1
            # pbar.update(1)
            # Double check
            # print("Check: ")
            # print(xor(current_iv[16-len(d1):], d1))
            break
        if i == 255:
            print("Error: ", d1)
            exit()
# pbar.close()
print("d1: ", d1)
current_p1 = xor(iv, d1)
target_iv = xor(xor(
    current_p1,
    b'{"username":"adm'),
    # b"{'username':'adm"),
    iv)
print("target_iv: ", target_iv)

r.send((target_iv + target_block1 + target_block2 + block3).hex().encode())
r.recvuntil(b"Example: ")
ct = r.recvline().strip().decode()
iv = bytes.fromhex(ct[:32])
ct = bytes.fromhex(ct[32:])

# given print(1337)
# wanted print(flag)

iv = iv[:6] + xor(xor(iv[6:10], b"1337"), b"flag") + iv[10:]
r.recvuntil(b": ")
r.send((iv + ct).hex().encode())
print(r.recvall().decode())
r.interactive()

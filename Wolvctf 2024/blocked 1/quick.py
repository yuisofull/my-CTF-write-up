from pwn import *

token = bytes.fromhex(
    "f483fcce0dd4ac4a5a420509883783ea00f8af70b720f9cad48ec153db518c9d91f1cd8a5bd7cfdadd0135f722a9febd"
)

iv = token[:16]
block1 = token[16:32]
block2 = token[32:48]
blocks = token[48:]

original = f"password reset: guest_280031".encode() + b"\0" * 4
target = "password reset: doubledelete".encode() + b"\0" * 4

# for i in range(16, 28):
#     iv[]
ori=b"guest_280031"
want = b"doubledelete"
# print(block1)
new_block1 = b""
for i in range(12):
    new_block1 += (block1[i]^ori[i]^want[i]).to_bytes(1, byteorder='big')#(block1[i] ^ want[i] ^ ori[i]).to_bytes(1, byteorder='big')
    print(len(new_block1))
    
#new_block1 = xor(block1, block2, target)
print(len(iv + new_block1 + token[28:]))
token = (iv + new_block1 + token[28:]).hex()

print(token)

# nc 2024.ductf.dev 30020
from pwn import *

# Set up the target host and port
host = "2024.ductf.dev"
port = 30020

# Establish a connection to the target
conn = remote(host, port)
respone = ""
current = b""
key = b""

for i in range(0, 8):
    for j in range(0, 256):
        conn.recvuntil(b"ct: ")
        conn.sendline(current + f"{j:02x}".encode())
        response = conn.recvline().decode().strip()
        print(current.decode() + f"{j:02x} " + response)
        if "invalid" not in response:
            print("Found: " + current.decode() + f"{j:02x}")
            print(response)
            current = current + f"{j:02x}".encode()
            # Step 1: Convert the hexadecimal strings to bytes
            response_bytes = response.encode()
            current_bytes = bytes.fromhex(current.decode())
            while len(response_bytes) < len(current_bytes):
                response_bytes = response_bytes + b" "
            key_bytes = bytes(a ^ b for a, b in zip(response_bytes, current_bytes))

            # Step 3 (Optional): Convert the result back to a hexadecimal string if needed
            key_hex = key_bytes.hex()
            key = key_bytes

            print(f"Key in bytes: {key_bytes}")
            print(f"Key in hex: {key_hex}")
            break
tmp = "FLAG".encode()
while len(tmp) < len(key):
    tmp = tmp + b" "
xor_result = bytes(a ^ b for a, b in zip(tmp, key))
xor_result_hex = xor_result.hex().encode()
conn.recvuntil(b"ct: ")
print(f"XOR result in bytes: {xor_result}")
conn.sendline(xor_result_hex)
print(conn.recvall())
conn.close()

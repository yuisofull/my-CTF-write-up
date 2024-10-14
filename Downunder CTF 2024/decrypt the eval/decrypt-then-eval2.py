from Crypto.Cipher import AES
import os
import io
import sys

KEY = b'\x07\x90h\xd2\xc20`\x90\xdf\xcb\tE\x9b\xb1\x01\xd4'
IV = b'D\xc9\xc2\xc9|\x99\xd6{\x11\xd4\xb1`\x9c\xe0\xdc\x9a'
FLAG =  "DUCTFtestflag"

def main(ct):
    while True:
        ct = bytes.fromhex(ct)
        aes = AES.new(KEY, AES.MODE_CFB, IV, segment_size=128)
        try:
            output = io.StringIO()
            sys.stdout = output
            print(eval(aes.decrypt(ct)))
            sys.stdout = sys.__stdout__
            print("OK")
            print(output.getvalue())
            return output.getvalue()
        except Exception:
            print('invalid ct!')
            return "invalid ct!"

respone = ""
current = b""
key = b""

for i in range(0, 8):
    for j in range(0, 256):
        ct = current.decode() + f"{j:02x}"
        response = main(ct)
        print(current.decode() + f"{j:02x} " + response)
        if "invalid" not in response:
            print("Found: " + current.decode() + f"{j:02x}")
            print(response)
            current = current + f"{j:02x}".encode()
            response_bytes = response.encode()
            current_bytes = bytes.fromhex(current.decode())
            while len(response_bytes) < len(current_bytes):
                response_bytes = response_bytes + b" "
            key_bytes = bytes(a ^ b for a, b in zip(response_bytes, current_bytes))

            key_hex = key_bytes.hex()
            key = key_bytes

            print(f"Key in bytes: {key_bytes}")
            print(f"Key in hex: {key_hex}")
            break
tmp = "FLAG".encode()
print("current: ", current)
while len(tmp) < len(key):
    tmp = tmp + b" "
xor_result = bytes(a ^ b for a, b in zip(tmp, key))
xor_result_hex = xor_result.hex().encode()
print(f"XOR result in bytes: {xor_result}")

print(main(xor_result_hex.decode()))


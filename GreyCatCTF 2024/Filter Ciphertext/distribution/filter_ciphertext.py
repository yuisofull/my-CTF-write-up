from Crypto.Cipher import AES
import os

with open("flag.txt", "r") as f:
    flag = f.read()

BLOCK_SIZE = 16
iv = os.urandom(BLOCK_SIZE)

xor = lambda x, y: bytes(a^b for a,b in zip(x,y))

key = os.urandom(16)

def encrypt(pt):
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    blocks = [pt[i:i+BLOCK_SIZE] for i in range(0, len(pt), BLOCK_SIZE)]
    tmp = iv
    ret = b""
    
    for block in blocks:
        res = cipher.encrypt(xor(block, tmp))
        ret += res
        tmp = xor(block, res)
        
    return ret
# secret: 5 blocks
# tmp = iv
# secret_enc_1 = ecb(secret[0]^iv)
# tmp = secret[0]^secret_enc_1
# secret_enc_2 = ecb(secret[1]^secret[0]^secret_enc_1)
# tmp = secret[1]^secret_enc_2
# secret_enc_3 = ecb(secret[2]^secret[1]^secret_enc_2)
# tmp = secret[2]^secret_enc_3
# secret_enc_4 = ecb(secret[3]^secret[2]^secret_enc_3)
# tmp = secret[3]^secret_enc_4
# secret_enc_5 = ecb(secret[4]^secret[3]^secret_enc_4)
    
def decrypt(ct):
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    blocks = [ct[i:i+BLOCK_SIZE] for i in range(0, len(ct), BLOCK_SIZE)]

    for block in blocks:
        if block in secret_enc:
            blocks.remove(block)
    
    tmp = iv
    ret = b""
    
    for block in blocks:
        res = xor(cipher.decrypt(block), tmp)
        ret += res
        tmp = xor(block, res)
    
    return ret
    
secret = os.urandom(80)
secret_enc = encrypt(secret)

print(f"Encrypted secret: {secret_enc.hex()}")

print("Enter messages to decrypt (in hex): ")

while True:
    res = input("> ")

    try:
        enc = bytes.fromhex(res)

        if (enc == secret_enc):
            print("Nice try.")
            continue
        
        dec = decrypt(enc)
        if (dec == secret):
            print(f"Wow! Here's the flag: {flag}")
            break

        else:
            print(dec.hex())
        
    except Exception as e:
        print(e)
        continue

    



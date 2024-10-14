from Crypto.Cipher import AES 
from random import randint 
from os import urandom 

def calculate_Ek_y0(key, nonce):
    assert len(nonce) == 12, "Nonce must be 12 bytes (96 bits) long"
    y0 = nonce + b'\x00\x00\x00\x01'
    cipher = AES.new(key, AES.MODE_ECB)
    Ek_y0 = cipher.encrypt(y0)
    return Ek_y0

def decrypt_y0_and_extract_nonce(key, ek_y0):
    cipher = AES.new(key, AES.MODE_ECB)
    y0 = cipher.decrypt(ek_y0)
    nonce = y0[:12]
    return nonce

def encrypt_gcm(plaintext, key, nonce, aad=None):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    if aad:
        cipher.update(aad)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    return nonce, ciphertext, tag
# TAG:  6a2aec02f5de51c15b5d8a247392fcbd
# AAD:  6669eb30569b79e1cb5832aa7703a3e1
# Require Message:  9744af4f7c63b956c5abf7f4e92d757fd98ad6d309023a2d948c7472fdc28663e39fe9c10af8f38fa989b3203e9c4d3a3fa4c721ee2ee0e60cbf6a7251dfa0ba5a63178249fd1699c0577d4b556f470980af93431cf46bac28c8024b18911ca0a5af9294195668f0169499edc07e2b7884080d3fd0ef47dbca58243224ff39c82e2ab6afad01f88bc184d025363696f6914d4e7892e8c17dd9c35862524d85b4aa16eeba4d41f4a5e2745c29bc7b582b0e5008deb94519499a42cc2a96ec280cfddbb821126eb5b6e8951dd77c21e1abcf2aca7e62e3b42c35399db735566a1d42c91cc55e7e9705ba9d1e178fa130c8a4cbaaad9fb28d5681bc590e110ad7e83e8ba5ad5d65b0681e3113cd55c2415a6166d4b19370be2a46e4127849affd44586ab869fa8bb9e0930be4fb1859a3699534f6ea870e637fc7b81471fcfd0c0d5e987a2958444bde92e1692b271124411ff164af2f26165a1ddd318ecb8d29a21d4d970a3843402f085e8d17f7d27e2a672299763215cd381594fad89bc71ae784e7431d57cba5bccfd6224d1a27f0a53c52c98d27dfc7e479b2f0aa329d9ee75ed33eb9c7127ff78f6f52b8c9e75a06f19ccb4ed32c6bda9cb094f107c049a83b16

aad = bytes.fromhex("6669eb30569b79e1cb5832aa7703a3e1")
msg = bytes.fromhex("9744af4f7c63b956c5abf7f4e92d757fd98ad6d309023a2d948c7472fdc28663e39fe9c10af8f38fa989b3203e9c4d3a3fa4c721ee2ee0e60cbf6a7251dfa0ba5a63178249fd1699c0577d4b556f470980af93431cf46bac28c8024b18911ca0a5af9294195668f0169499edc07e2b7884080d3fd0ef47dbca58243224ff39c82e2ab6afad01f88bc184d025363696f6914d4e7892e8c17dd9c35862524d85b4aa16eeba4d41f4a5e2745c29bc7b582b0e5008deb94519499a42cc2a96ec280cfddbb821126eb5b6e8951dd77c21e1abcf2aca7e62e3b42c35399db735566a1d42c91cc55e7e9705ba9d1e178fa130c8a4cbaaad9fb28d5681bc590e110ad7e83e8ba5ad5d65b0681e3113cd55c2415a6166d4b19370be2a46e4127849affd44586ab869fa8bb9e0930be4fb1859a3699534f6ea870e637fc7b81471fcfd0c0d5e987a2958444bde92e1692b271124411ff164af2f26165a1ddd318ecb8d29a21d4d970a3843402f085e8d17f7d27e2a672299763215cd381594fad89bc71ae784e7431d57cba5bccfd6224d1a27f0a53c52c98d27dfc7e479b2f0aa329d9ee75ed33eb9c7127ff78f6f52b8c9e75a06f19ccb4ed32c6bda9cb094f107c049a83b16")

key=b"A"*16
nonce=b"A"*12
print(encrypt_gcm(msg, key, nonce, aad))

ct=b'\xd1\xe5J\x84\xb3\xa0C\xc8\xc6\xb9\x1f\x9e\x02\xf9)\xee3\xa4\x00&\xa5\x02\xa3o\x8c\x01\x8a\x0e\xe8\xe0\x99#Y\x90\xafzD=@\xed\x8c\x93\x04\xb0\x81\xd1X\xd8\t\xf4\x03vV~eo~\xe3h\xfaa\xc1=\xae\xf6J\xf3\x0fb\xba)8J\x7f\xfb\x80dH\xed\x01\x1a\xc8"<\xf9\xf7\x13cQ\x9c\xcc\xd0\x13aH\xf4W\x97\xbd\xe1\xc7\xad^\xc0.0\xc8\xbbIg=\xd4\xa6\x12\x9c\x82\x06\x1d9l\xa7\xe0U\xb4x\xef\xa7\xa9\xa7\xd0\xc4\xc0Bul\xf3\xca\x03\xa7fC\x0c\x89\xa1\xaeQCqe\x89\xf7\xbbEY\xe8\xe9\x1d\x86O\xa7\x16\xabl\'xb\xce\xf1$\x1a\xfd\xa1)\x86\xcb\x14T\xc6](\x1e\x89\x0b\x92\xd8M"\xa7\xe7n\xac\xb2\xbc\xd9\x8c\x93\xa7\x14\x94~a\xdf\x86~\xac\x1a\x03^Z&\xa4\x94\x04\xaaT\xe8\x0bW&\xb1\xf5\xf9>\x0eO\x8au\xa32\xf7@\xe0\xde\xad|\xa2U\xe5\xe6D\xae\xdb\xe0\x89\xf1Shw\xd7r\x0e\\\xeeu\xd1)\x96\x14\x82\xa5\x11-\x93+\x1838zJO\xb9i%\xbc\xb2\xbf\x07\xfe]\xebf\xb7N\x02m\xf8|*>\x11\x91\xd3\xbd\x82_\xd8\x9d\x8a\xe4x\x99$\xaa\xcel\x05\x02p5E\xd0\xd1\xc2/\xb77S9N\x1dc\x16\xa9p\xc0\xb0 \xf7O\xa0\xd3\x02\x9cU,I\\l\xabv\xe6\xbb\x17\x94\xd3\xed0\xd7A\xf3\xd0SFn\xa0JX\x9d\xf9Zt\x0c\xe1\xc6x*\xc1\xcdK\xfd\xe9\xc4\x91\x13\x8e5\xee\xf3\xf9#Q/ \xa0\xb5\xf1%\x93|%\\\xcc\xacN\xa7\xdc\xfa\x1d<\xf6\x1a\x85\x18-\x7fj\xfa\x02i\x1b\xd7}\x97\xa6\xae\x11\x92\xcb6\xf3\xd8\r\xe1]\xbe\x14\xf6\xfa\x85\xcd\x0c\x95:/\xc9\x902.\x82F\xbd\xd6\xb0\xf6_\xaa\x03y\xfbT'

current_tag= b',[+e\x04#ky\xef\x83\xcf}\x8f\xd6\xe8\xb8'
print(current_tag, aad, msg)
target_tag = bytes.fromhex("6a2aec02f5de51c15b5d8a247392fcbd")

# T = Q ⊕ Ek(y0) = (U0 ⨂ Hn+1) ⊕ ... ⊕ (Un ⨂ H) ⊕ Ek(y0)

current_Ek_y0 = calculate_Ek_y0(key, nonce)
wanted_Ek_y0 = bytes([a ^ b ^ c for a, b, c in zip(current_tag, target_tag, current_Ek_y0)])
new_nonce = decrypt_y0_and_extract_nonce(key, wanted_Ek_y0)

def decrypt_gcm(key, nonce, ct, tag, aad=None): 
    try: 
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce) 
        if aad: 
            cipher.update(aad) 
        pt = cipher.decrypt_and_verify(ct, tag) 
        return pt 
    except ValueError as e: 
        print(f"Decryption failed: {e}") 
        return None 

#test if the new nonce is correct
answer = decrypt_gcm(key, new_nonce, ct, target_tag, aad) 
if answer == None: 
    exit(0) 
elif msg in answer: 
    print(f"Correct! Here is your flag: ok") 
    exit(0) 
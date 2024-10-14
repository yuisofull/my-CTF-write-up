from Crypto.Cipher import AES 
from random import randint 
from os import urandom 
FLAG = b'BKISC{XXXXXXXXXXXXXXXXXXXXXXXX}' 


def encrypt_gcm(plaintext, key, nonce, aad=None):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    if aad:
        cipher.update(aad)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    return nonce, ciphertext, tag
  
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
 
# T = Q ⊕ Ek(y0) = (U0 ⨂ Hn+1) ⊕ ... ⊕ (Un ⨂ H) ⊕ Ek(y0)

# given tag, aad, need_message
# must find key, nonce, ciphertext
def main(): 
    print("AES-GCM 101:") 
    tag = urandom(16) 
    aad = urandom(16) 
    need_message = urandom(randint(5,500)) 
    print("TAG: ", tag.hex()) 
    print("AAD: ", aad.hex()) 
    print("Require Message: ", need_message.hex()) 
    print("Provide the key, nonce and ciphertext to get the flag:") 
    key = input("Key> ") 
    nonce = input("Nonce> ") 
    ciphertext = input("Ciphertext> ") 
    key = bytes.fromhex(key) 
    nonce = bytes.fromhex(nonce) 
    ciphertext = bytes.fromhex(ciphertext) 
     
    answer = decrypt_gcm(key, nonce, ciphertext, tag, aad) 
    if answer == None: 
        exit(0) 
    elif need_message in answer: 
        print(f"Correct! Here is your flag: {FLAG}") 
        exit(0) 
     
     
main()
#!/bin/python3
from hashlib import md5
from Crypto.Util.number import long_to_bytes, bytes_to_long
from secret import sk, flag
import time
import base64
import signal

def alarm(second):
    # This is just for timeout.
    # It should not do anything else with the challenge.
    def handler(signum, frame):
        print('Timeout!')
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(second)

BLOCK_SIZE = 16
def bytes_xor(a, b):
    assert len(a) == len(b)
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

def block_cipher(key, last_block, pt):
    key.update(last_block)
    ct = bytes_xor( key.digest(), pt )
    return ct

def pad(message):
    pad_len = (16 - len(message) % 16) if len(message) % 16 else 16
    message += chr( pad_len ).encode() * pad_len
    return message

def unpad(message):
    pad_len = int(message[-1])
    return message[:-pad_len]

def encrypt(sk, message):
    message = pad(message)
    key = md5()
    last_block, cipher_text = sk, b""
    for i in range(0, len(message), 16):
        pt = message[i:i+16]
        cipher_text += block_cipher(key, last_block, pt)
        last_block = pt
    
    return cipher_text

# def decrypt(sk, cipher_text):
#     key = md5()
#     last_block, message = sk, b""
#     for i in range(0, len(cipher_text), 16):
#         ct = cipher_text[i:i+16]
#         last_block = block_cipher(key, last_block, ct)
#         message += last_block
    
#     message = unpad(message).decode()
#     return message

if __name__ == "__main__":
    alarm(300)
    print("""
*******************************************************
I know MD5 is not an encryption but a hash algorithm.
But I love MD5, so I still want to use it to encrypt
my data. Let me show you how!!
------------------------------------------------------
1) Encrypt a data.
2) Decrypt a data.
3) Bye!
********************************************************
    """)
    assert len(sk) == BLOCK_SIZE
    for _ in range(3):
        try:
            option = input("Option: ")
            if int(option) == 1:
                data = input("Give me your data (in base64 encoded):")
                data = base64.b64decode(data.encode())
                test = time.time()
                data = f"TimeStamp: {test} || User:CTF_Player || data: ".encode() + data + f" || Flag: {flag}".encode()
                print(base64.b64encode(encrypt(sk, data)))

            elif int(option) == 2:
                print("Sorry~ Not implemented yet ._.")
            
            else:
                print("Bye~~~~~")
                break
        except:
            print("Something wrong?")
            exit()

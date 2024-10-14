#!/bin/python3
import random
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from hashlib import sha256
from base64 import b64encode, b64decode
from secret import flag
import signal

def alarm(second):
    # This is just for timeout.
    # It should not do anything else with the challenge.
    def handler(signum, frame):
        print('Timeout!')
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(second)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keypair(keysize):
    p = getPrime(keysize)
    q = getPrime(keysize)
    n = p * q
    phi = (p-1) * (q-1)
    
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = pow(e, -1, phi)
    # for CRT optimize
    dP = d % (p-1)
    dQ = d % (q-1)
    qInvP = pow(q, -1, p)
    return ((e, n), (dP, dQ, qInvP, p, q))

def verify(pk, message: bytes, signature: bytes):
    e, n = pk
    data = bytes_to_long(sha256(message).digest())
    return data == pow(bytes_to_long(signature), e, n)

bug = lambda : random.randrange(0, 256)
def sign(sk, message: bytes):
    dP, dQ, qInvP, p, q = sk
    data = bytes_to_long(sha256(message).digest())
    # use CRT optimize to sign the signature,
    # but there are bugs in my code QAQ
    a = bug()
    mP = pow(data, dP, p) ^ a
    b = bug()
    mQ = pow(data, dQ, q) ^ b
    k = (qInvP * (mP - mQ)) % p
    signature = mQ + k * q
    return long_to_bytes(signature)


if __name__ == "__main__":
    alarm(300)

    public, private = generate_keypair(512)
    print("""
***********************************************************
Have you heard CRT optimization for RSA? I have implemented
a CRT-RSA signature. However, there are bugs in my code...
---------------------------------------------------------
1) Print public key.
2) Sign a message.
3) Give me flag?
4) Bye~
***********************************************************
    """)

    for _ in range(5):
        try:
            option = input("Option: ")
            if int(option) == 1:
                print('My public key:')
                print(f"e, n = {public}")

            elif int(option) == 2:
                message = input("Your message (In Base64 encoded): ")
                message = b64decode(message.encode())
                if b"flag" in message: 
                    print(f"No, I cannot give you the flag!")
                else:
                    signature = sign(private, message)
                    signature = b64encode(signature)
                    print(f"Signature: {signature}")
            
            elif int(option) == 3:
                signature = input("Your signature (In Base64 encoded): ")
                signature = b64decode(signature.encode())
                message = b64encode(b"Give me the flag!")
                if verify(public, message, signature):
                    print(f"Well done! Here is your flag :{flag}")
                else :
                    print("Invalid signature.")

            else:
                print("Bye~~~~~")
                break
        except Exception as e:
            print(e)
            print("Something wrong?")
            exit()


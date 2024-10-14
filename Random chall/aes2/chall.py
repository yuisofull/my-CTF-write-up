import random
import string
for i in range(1,32):
    
    if(len(str(i))==1):
        i='0'+str(i)
        
    seed1=str(i)+'122022'
    print("s:",seed1)
    random.seed(seed1)
    allowed_chars = string.ascii_letters + string.digits
    key = ''.join(random.choices(allowed_chars, k=43))
    # key='xa9Ah1fqCMX3YxoUoUwOBDhi3TMlhBPVjJdHhpM8hBr'
    hexx="5e04610a22042638723c571e1a5436142764061f39176b4414204636251072220a35583a60234d2d28082b"
    byte_string = bytes.fromhex(hexx)  
    decrypted_string = byte_string.decode()
    for i in range(43):
        decrypted_char = chr(ord(decrypted_string[i]) ^ ord(key[i]))
        decrypted_string += decrypted_char
    if "0CTF" in decrypted_string:
        print("decr",decrypted_string)
        break
print("findished")
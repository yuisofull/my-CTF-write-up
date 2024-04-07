# encrypt = AES(iv + msg)
# => encrypt[0] = key(iv ^ iv)
# => encrypt[1] = key(msg[0] ^ iv)

# encrypt2 = encrypt[n - 1] ^ msg[n]
# encrypt3= iv + encrypt2


# we have
# encrypt2 = encrypt3[16:]
# iv = encrypt3[:16]

import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor

# we have
s="2ae8ccc7aaaacc1967cbff875bf51c7887b7b3cabb19b9903b37fc497d1e5ed3245edd59f1ce495d2e2766cb83df97fb"
msg = bytes.fromhex(s)
iv = msg[:16]

print("iv", iv.hex())

s2="32d3e2ec71dd5dcd9107df240e4f5d68142bd99ff80a0863745c0c5789a6039de4d8ddadc978cde55756882012702df2"
msg2 = bytes.fromhex(s2)
# print("len(msg2)", len(msg2))

# enc_iv=msg2[16:32]
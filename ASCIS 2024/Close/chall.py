from Crypto.Util.number import getPrime, bytes_to_long
import random
import os

e = 65537
p = getPrime(1024)
while (p - 1) % e == 0:
    p = getPrime(1024)

Ns = []
while len(Ns) < 4:
	q = getPrime(2048)
	N = p * q
	if (q - 1) % e != 0 and N not in Ns:
		Ns.append(N)

# size N = 3072 bits

flag = open("flag.txt", "rb").read()
flag += os.urandom(3072 // 8 - 2 - len(flag)) # 382-len(flag) bytes

flag = bytes_to_long(flag)

cts = [pow(flag, e, N) for N in Ns] # flag^e mod N = ct
Ns = [N + int(os.urandom(32).hex(), 16) for N in Ns] # 256 bits of randomness

# p*q1 + a= N1=>N1 >> 256 = p*q1>>256
# p*q2 + b= N2
# p*q3 + c= N3
# p*q4 + d= N4


random.shuffle(Ns)

f = open("output.txt", "w")
f.write(f"{Ns = }\n")
f.write(f"{cts = }\n")
f.close()
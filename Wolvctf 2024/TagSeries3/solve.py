from pwn import *
import hlextend

r=remote('tagseries3.wolvctf.io', 1337)
r.recvline()
mac = r.recvline().strip().decode()
print(mac)
SECRET_LENGTH = 1200

sha = hlextend.new('sha1')
appendData=b"flag.txt"
knownData=b"GET FILE: "
command=sha.extend(appendData, knownData, SECRET_LENGTH, mac)

r.sendline(command)
r.sendline(sha.hexdigest())
print(r.recvall())
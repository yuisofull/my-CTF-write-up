import hlextend
from hashlib import sha1
import HashTools
import os
import sys

MESSAGE = b"GET FILE: "
SECRET = os.urandom(1200)

_sha1 = sha1()
_sha1.update(SECRET)
_sha1.update(MESSAGE)

mac= _sha1.hexdigest()
mac = "18608261ef65c2b44e66ecb31e8e6e94c74db6a7"
SECRET_LENGTH = 1200
#command = b"GET FILE: flag.txt"
# _sha1.update(SECRET)
#_sha1.update(command)
# print("target hash: ", _sha1.hexdigest())

sha = hlextend.new('sha1')
appendData=b"flag.txt"
knownData=b"GET FILE: "
command=sha.extend(appendData, knownData, SECRET_LENGTH, mac)

print(command)

_sha1 = sha1()
_sha1.update(SECRET)
_sha1.update(command)
print("target hash: ", _sha1.hexdigest())

print("My hash: ", sha.hexdigest())
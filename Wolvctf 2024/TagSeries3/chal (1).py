import sys
import os
from hashlib import sha1

MESSAGE = b"GET FILE: "
SECRET = os.urandom(1200)


def main():
    _sha1 = sha1()
    _sha1.update(SECRET)
    _sha1.update(MESSAGE)
    sys.stdout.write(_sha1.hexdigest() + '\n')
    
    # we recive sha1(secret + message)
    
    # we can put message=b"GET FILE: flag.txt"
    # and hash 
    # make sure that hash == sha1(secret+message)

    sys.stdout.flush()
    _sha1 = sha1()
    command = sys.stdin.buffer.readline().strip()
    print("command: ", command)
    hash = sys.stdin.buffer.readline().strip()
    _sha1.update(SECRET)
    _sha1.update(command)
    while True:
        if command.startswith(MESSAGE) and b"flag.txt" in command:
            print("done step 1")
            if _sha1.hexdigest() == hash.decode():
                print("success")
                with open("flag.txt", "rb") as f:
                    sys.stdout.buffer.write(f.read())
            else:
                print("fail")
                _sha1 = sha1()
                hash = sys.stdin.buffer.readline().strip()
                _sha1.update(SECRET)
                _sha1.update(command)


if __name__ == "__main__":
    main()

enc = bytearray(xor(f,key))

open('test.png', 'wb').write(enc)
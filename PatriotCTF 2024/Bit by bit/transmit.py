import sys

blocksize = 16

def loadMessage():
    message = ""
    with open("message.txt","r",encoding='utf-8') as file:
        for line in file:
            message += line
    while len(message) % blocksize != 0:
        message += '0'
    return message

def encode(chunk):
    start = 120
    encoded = 0
    for c in chunk:
        encoded = encoded | (ord(c)<<start)
        start -= 8
    return encoded

def transmit():

    # Test key
    key = 0xadbeefdeadbeefdeadbeef00

    iv = 0
    msg = loadMessage()
    chunks = [msg[i:i+16] for i in range(0,len(msg), 16)]

    send = ''
    for chunk in chunks:
        iv = (iv+1) % 255
        curr_k = key+iv
        encoded = encode(chunk)
        enc = encoded ^ curr_k
        foo = hex(enc)[2:]
        while len(foo) != 32:
           foo = '0'+foo
        send += foo
    print(send)
    sys.exit(0)

# def encrypt(message):
#     # Test key
#     while len(message) % blocksize != 0:
#         message += '0'
#     key = 0xadbeefdeadbeefdeadbeef00
#     iv = 0
#     msg = message
#     chunks = [msg[i:i+16] for i in range(0,len(msg), 16)]

#     send = ''
#     for chunk in chunks:
#         iv = (iv+1) % 255
#         curr_k = key+iv
#         encoded = encode(chunk)
#         enc = encoded ^ curr_k
#         foo = hex(enc)[2:]
#         while len(foo) != 32:
#            foo = '0'+foo
#         send += foo
#     return send

def decode(chunk):
    start = 120
    decoded = b''
    for i in range(16):
        decoded += bytes((chunk>>start) & 0xff)
        start -= 8
    return decoded
def recover():
    key = 0xadbeefdeadbeefdeadbeef00
    iv = 0
    with open("out.txt","r") as file:
        for line in file:
            line = line.strip("\n")
            chunks = [int(line[i:i+32],16) for i in range(0,len(line),32)]
            decoded_msg = b""
            for chunk in chunks:
                iv = (iv+1) % 255
                curr_k = key+iv
                decoded = chunk ^ curr_k
                decoded = decode(decoded)
                decoded_msg += decoded
            # Double check
            print(decoded_msg)
            #save to file out2.txt
            with open("out2.txt","w") as file:
                file.write(decoded_msg)
            print(encrypt(decoded_msg))
                
recover()
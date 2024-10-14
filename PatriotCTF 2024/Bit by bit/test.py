def decode(encoded):
    start = 120
    decoded = b''
    while start >= 0:
        byte = (encoded >> start) & 0xFF
        # print(byte)
        # to byte
        decoded += bytes([byte])
        start -= 8
    return decoded

def receive(transmitted):
    key = 0xadbeefdeadbeefdeadbeef00
    iv = 0
    received = b''
    for i in range(0, len(transmitted), 32):
        iv = (iv + 1) % 255
        foo = transmitted[i:i+32]
        enc = int(foo, 16)
        curr_k = key + iv
        encoded = enc ^ curr_k
        chunk = decode(encoded)
        received += chunk
    return received
def transmit():
    msg = ''
    with open("out.txt","r") as file:
        for line in file:
            msg += line.strip("\n")
    return msg
        
# Example usage:
transmitted = transmit()  # assuming transmit() returns the transmitted message
original_msg = receive(transmitted)
print(original_msg)


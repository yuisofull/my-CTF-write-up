import hlextend
from math import ceil

def split_bytes_in_blocks(x, blocksize):
    nb_blocks = ceil(len(x)/blocksize)
    return [x[blocksize*i:blocksize*(i+1)] for i in range(nb_blocks)]

sha = hlextend.new('sha1')
msg = b"GET FILE: flag.txt"
orihash="bbed7c6bf1a84f830ebceb0e9fe7cc8f58f7f5b7"
mac=orihash.encode()
secretLength=1200


print(H)

appendData=b"flag.txt"
knownData=b"GET FILE: "
print(sha.extend(appendData, knownData, secretLength, orihash))

print(sha.hexdigest())
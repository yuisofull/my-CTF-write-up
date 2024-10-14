import hashlib

# String to hash
input_string = "Hello, World!"

# Convert the string to bytes
input_bytes = input_string.encode('utf-8')

# Hash the bytes using SHA-256
hash_object = hashlib.sha256(input_bytes)

# Get the hexadecimal digest of the hash
hash_hex = hash_object.hexdigest()

print(f"SHA-256 hash: {hash_hex}")

def hash(input_bytes: bytes) -> str:
    hash_object = hashlib.sha256(input_bytes)
    return hash_object.hexdigest()

from ctypes import *
import itertools

# Load the shared library containing the encryption function
lib = CDLL("./encryption.so")

# Define the function signature for the encryption function
encryption = lib._encryption
encryption.restype = POINTER(c_ulong)
encryption.argtypes = [c_void_p, c_ulong]

# Define the encrypted string to match
encrypted_target = "188d1f2f13cd5b601bd6047f4496ff74496ff74496ff7"

# Check if the target string is a valid hexadecimal string
if len(encrypted_target) % 2 != 0 or not all(c in '0123456789abcdefABCDEF' for c in encrypted_target):
    print("Invalid hexadecimal string:", encrypted_target)
    exit()

# Convert the target string to a bytes object
encrypted_target_bytes = bytes.fromhex(encrypted_target)

# Define the character set to generate possible input strings
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Define the maximum length of the input string to consider
max_length = 6

# Brute-force loop to generate all possible input strings
for length in range(1, max_length + 1):
    for combination in itertools.product(charset, repeat=length):
        # Convert the combination to a string
        input_string = "".join(combination)

        # Convert the input string to a bytes object
        input_bytes = input_string.encode()

        # Encrypt the input string
        encrypted_data = encryption(input_bytes, len(input_bytes))

        # Convert the encrypted data to a hexadecimal string
        encrypted_string = "".join(format(x, 'x') for x in encrypted_data[:length])

        # Check if the encrypted string matches the target
        if encrypted_string == encrypted_target:
            print("Match found:")
            print("Input:", input_string)
            print("Encrypted:", encrypted_string)
            break

# Free the memory allocated by the encryption function
lib.free(encrypted_data)

# conv function as given
def conv(array1: bytes, array2: bytes) -> bytes:
    len1, len2 = len(array1), len(array2)
    res = [0] * (len1 + len2 - 1)
    for i in range(len1 + len2 - 1):
        csum = 0
        for j in range(max(0, i - len2 + 1), min(len1, i + 1)):
            csum += array1[j] * array2[i - j]
        res[i] = csum % 256
    return bytes(res)

# Byte-by-byte brute force for plain1
def brute_force_plain1_step_by_step(ct: bytes, key: bytes):
    plain1 = bytearray()  # Initialize plain1 as an empty array
    for i in range(len(ct) - len(key) + 1):
        print(f"Brute-forcing byte {i + 1}/{len(ct) - len(key) + 1}")
        for candidate_byte in range(256):
            # Try adding this candidate byte to plain1
            test_plain1 = plain1 + bytes([candidate_byte])
            # Compute the convolution for the current part of plain1
            test_conv = conv(test_plain1, key)[:i + len(key)]
            # Compare with the corresponding part of the ciphertext
            if test_conv == ct[:i + len(key)]:
                # If it matches, add this byte to plain1
                plain1.append(candidate_byte)
                print(f"Matched byte {i + 1}: {candidate_byte}")
                break
        else:
            print(f"Failed to match byte {i + 1}")
            return None
    return bytes(plain1)

# Ciphertext (given as a hex string)
ct = bytes.fromhex("17c080c00398a06e4661e403b2b571b578221bba83e235a0feece7213ad4d65c1d89c2a3afae5ef91bf7f2181f0c797505b7bd55c62d1edf2614b17f88f85eac674fbd6d7be4e2a617605c68e1baf8603cb9b1d32b2bc1ab60d8c62b20be0bc0fb73a546b5641988a3bf8eeb778731e048970308d941a8bd5f6cb56159069364c93b5429afdb85f9dfb5f5b0ca44d314af68bc9d56b39321fe5cc072c9508978693ee60a9bffff5b52f6aa0ca37f9b421eb402a4886b742570926b7479d2b89528caceb7121a338c233164c33a120b9813bc56b855c914124ecb30df3d4a14c92788faa7c9e32b544e24d9d9fe2a5539a280c28466dc6b276ba4b089fa26f8bace95f43f6c5d491e14e5fa09a853fff2dfd73a8cf8d7b54d3d8d693db7b182789f47e343e9cf56f8663e181a1e98276aface8b1052e3ee9c6630d69ad479bfe1106ec1ab585a030ca130a6d849f9c4bed9d0b16f46890f1efa66c8f21f078088f426ef0e1f9af315ae3b2356123df174bb4095ad2361237bedc3e62c294f8ccc135f9766f0ec2a462087cd2648")

# Key (as given)
key = b'\xab\xec\xe9<\xaaC\x7fr\xeb\x8dgQ\xc0\x94\x01\x1d\xc03\x14\x97\xe2\x91\x97\xcf\x8b\x13?\x1d24w|'

# Perform byte-by-byte brute-force search
plain1 = brute_force_plain1_step_by_step(ct, key)

if plain1:
    print(f"Found plain1: {plain1}")
else:
    print("No valid plain1 found")

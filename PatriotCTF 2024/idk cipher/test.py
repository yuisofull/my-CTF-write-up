import base64

def encode_input(usr_input, srt_key):
    rsv_input = usr_input[::-1]  # Reverse the user input
    output_arr = []
    for i in range(int(len(usr_input) / 2)):
        c1 = ord(usr_input[i])
        c2 = ord(rsv_input[i])
        enc_p1 = chr(c1 ^ ord(srt_key[i % len(srt_key)]))
        enc_p2 = chr(c2 ^ ord(srt_key[i % len(srt_key)]))
        output_arr.append(enc_p1)
        output_arr.append(enc_p2)
    encoded_val = ''.join(output_arr)
    b64_enc_val = base64.b64encode(encoded_val.encode())
    return b64_enc_val.decode()

def brute_force_known_output(srt_key, known_output, max_length=10):
    # Brute force all combinations of 'usr_input'
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    # Try combinations of increasing lengths
    for length in range(1, max_length + 1):
        # Generate all possible combinations of the allowed characters with the given length
        def generate_combinations(current):
            if len(current) == length:
                # Try to encode the input and check if it matches the known output
                if encode_input(current, srt_key) == known_output:
                    print(f"Found match: {current}")
                    return True
                return False
            else:
                for char in chars:
                    if generate_combinations(current + char):
                        return True
            return False
        
        if generate_combinations(''):
            break

# Known base64 output
known_output = "QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I="
# Secret key
srt_key = "secretkey"

# Call brute-force function (you can adjust max_length as necessary)
brute_force_known_output(srt_key, known_output)

from collections import Counter

# Read the hex results from output.txt
def read_output_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Convert hex output to binary string
def hex_to_bin(hex_string, bit_length):
    return bin(int(hex_string, 16))[2:].zfill(bit_length)

# Hamming distance function to compare two binary strings
def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# Reconstruct the flag using brute-force analysis of Hamming distances
def reconstruct_flag(binary_results, bit_length):
    initial_guess = list(binary_results[0])

    # For each bit position, count how often it's the same across all results
    for i in range(bit_length):
        bit_counts = Counter([res[i] for res in binary_results])
        
        # If the bit is more often 1 than 0, assume it's a '1' in the original flag
        # Similarly, if it's more often 0, assume it's a '0' in the original flag
        if bit_counts['1'] > bit_counts['0']:
            initial_guess[i] = '1'
        else:
            initial_guess[i] = '0'
    
    # Return the binary string as the best guess
    return ''.join(initial_guess)

# Convert binary back to the original string (flag)
def binary_to_flag(binary_string):
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    flag = ''.join([chr(int(char, 2)) for char in chars])
    return flag

# Main brute-force solver
def brute_force_solver(output_file, bit_length):
    # Read hex results from the file
    hex_results = read_output_file(output_file)
    
    # Convert hex results to binary
    binary_results = [hex_to_bin(res, bit_length) for res in hex_results]
    
    # Reconstruct the flag using Hamming distance analysis
    reconstructed_binary = reconstruct_flag(binary_results, bit_length)
    
    # Convert the binary back into the original flag string
    reconstructed_flag = binary_to_flag(reconstructed_binary)
    
    return reconstructed_flag

# Example usage:
output_file = "output.txt"

# Calculate the bit length (assuming the flag is e.g. 16 characters long)
# Modify this based on the actual flag length or output length
flag_length = 37  # Example flag length, adjust as needed
bit_length = flag_length * 8

# Reconstruct the flag
reconstructed_flag = brute_force_solver(output_file, bit_length)
print(f"Reconstructed flag: {reconstructed_flag}")

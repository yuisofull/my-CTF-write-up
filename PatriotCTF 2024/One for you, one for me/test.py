import numpy as np

# Load the outputs from the share_bits_with_you function
outputs = []
with open('output.txt', 'r') as f:
    for line in f:
        outputs.append(line.strip())

# Convert the outputs to binary and construct the augmented matrix
n = len(outputs[0]) * 4  # number of bits in the flag
A = np.zeros((len(outputs), n), dtype=float)
b = np.array([int(output, 16) for output in outputs])
for i, output in enumerate(outputs):
    binary_output = bin(int(output, 16))[2:].zfill(n)
    for j, bit in enumerate(binary_output):
        A[i, j] = int(bit)

# Perform Gaussian elimination
for i in range(n):
    # Search for the row with the largest absolute value in the current column
    max_row = i
    for k in range(i + 1, len(outputs)):
        if abs(A[k, i]) > abs(A[max_row, i]):
            max_row = k
    # Swap the rows
    A[[i, max_row]] = A[[max_row, i]]
    b[[i, max_row]] = b[[max_row, i]]
    # Eliminate the current column
    for k in range(i + 1, len(outputs)):
        factor = A[k, i] / A[i, i]
        A[k, :] -= factor * A[i, :]
        b[k] -= factor * b[i]

# Back-substitute to find the flag bits
flag_bits = np.zeros(n, dtype=int)
for i in range(n - 1, -1, -1):
    flag_bits[i] = int(b[i] % 2)
    for j in range(i + 1, n):
        flag_bits[i] -= int(A[i, j]) * flag_bits[j]
    flag_bits[i] = int(flag_bits[i] % 2)

# Convert the flag bits to the original flag
flag = ''.join(chr(int(''.join(map(str, flag_bits[i*8:(i+1)*8])), 2)) for i in range(n // 8))
print(flag)
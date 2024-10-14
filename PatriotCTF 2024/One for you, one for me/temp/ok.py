import numpy as np

# Load the output.txt file
with open('output.txt', 'r') as f:
    outputs = [line.strip() for line in f.readlines()]

# Convert each output to a binary string
bin_outputs = [bin(int(o, 16))[2:].zfill(37 * 8) for o in outputs]

# Create a matrix to store the coefficients of the linear equations
A = np.zeros((len(outputs), 37 * 8))

# Create a vector to store the right-hand side of the linear equations
b = np.ones(len(outputs)) * (37 * 8) // 2

# Populate the matrix
for i, output in enumerate(bin_outputs):
    for j, bit in enumerate(output):
        if bit == '0':
            A[i, j] = 1
        else:
            A[i, j] = -1

# Solve the system of linear equations using NumPy
x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

# Convert the solution to the original flag
flag = ''.join(chr(int(''.join(str(int(round(y))) for y in x[i*8:(i+1)*8]), 2)) for i in range(37))

print(flag)
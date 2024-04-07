# Python3 program for the above approach 

# Function to convert Decimal to BCD 
def BCDConversion(n) : 

	# Base Case 
	if (n == 0) : 
		print("0000")
		return

	# To store the reverse of n 
	rev = 0

	# Reversing the digits 
	while (n > 0) : 
		rev = rev * 10 + (n % 10)
		n = n // 10

	# Iterate through all digits in rev 
	while (rev > 0) : 

		# Find Binary for each digit 
		# using bitset 
		b = str(rev % 10)
		
		# Print the Binary conversion 
		# for current digit 
		print("{0:04b}".format(int(b, 16)), end = " ") 

		# Divide rev by 10 for next digit 
		rev = rev // 10

# Given Number 
N =  89627
# Function Call 
BCDConversion(N)

# This code is contributed by divyeshrabadiya07

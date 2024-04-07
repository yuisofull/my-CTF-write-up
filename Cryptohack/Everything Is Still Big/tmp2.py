# Python3 code to convert BCD to its 
# decimal number(base 10). 

# Function to convert BCD to Decimal 
def bcdToDecimal(s): 

	length = len(s);
	check = 0;
	check0 = 0;
	num = 0;
	sum = 0;
	mul = 1;
	rev = 0;
	
	# Iterating through the bits backwards
	for i in range(length - 1, -1, -1):
		
		# Forming the equivalent 
		# digit(0 to 9)
		# from the group of 4.
		sum += (ord(s[i]) - ord('0')) * mul;
		mul *= 2;
		check += 1;
		
		# Reinitialize all variables
		# and compute the number
		if (check == 4 or i == 0):
			if (sum == 0 and check0 == 0):
				num = 1;
				check0 = 1;
				
			else:
				
				# Update the answer
				num = num * 10 + sum;
				
			check = 0;
			sum = 0;
			mul = 1;
			
	# Reverse the number formed.
	while (num > 0):
		rev = rev * 10 + (num % 10);
		num //= 10;
		
	if (check0 == 1):
		return rev - 1;
		
	return rev; 

# Driver Code 
if __name__ == "__main__": 

	s = "010010010010"
	
	# Function Call
	print(bcdToDecimal(s));
	
# This code is contributed by AnkitRai01

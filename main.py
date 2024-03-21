import string

def validate_input(line):
	try:
		i1, i2, base = line.split()
		# The split was successful
	except ValueError:
		# Handle the specific exception (ValueError in this case)
		print("Error: Invalid input format. Expected three integers separated by spaces.")
		# Stop program execution by raising an exception
		raise SystemExit()
	
	if not (i1.isdigit() and i2.isdigit() and base.isdigit()):
		print("Error: Non-digit characters found.")
		raise SystemExit()
	
	if len(i1) > 100 or len(i2) > 100:
		print("Error: Integer inputs are too large. Enter integers up to 100 digits long.")
		raise SystemExit()
	
	base = int(base)
	if base < 2 or base > 10:
		print("Error: Base must be in the range 2-10.")
		raise SystemExit()
	
	return i1, i2, base

def big_num_addition(i1, i2, base):
	
	# Get max length of integer - put zeros at the front of the shorter one
	max_len = max(len(i1), len(i2))

	# Front fill with zeros so that lengths are equal
	a, b = map(lambda element: element.zfill(max_len), [i1, i2])

	# Create an array initated to zeros
	#   --> max_len + 1 as the result can extend one beyond
	result = [0] * (max_len + 1) 

	# Set c0 to 0
	carry = 0

	# Loop through digits
	for i in range(max_len - 1, -1, -1):
		sum = int(a[i]) + int(b[i]) + carry
		result [i + 1] = sum % int(base)
		carry = sum // int(base)
	result[0] = carry

	if result[0] == 0:
		result.pop(0)
	
	# Map array to an int
	result_int = int(''.join(map(str, result)))

	return result_int

def k_split(num):
 	# Find k (half of n digits)
    k = len(num) // 2

    # Find second half (i.e. greater half) of num
    num1 = num[:k]

    # Find first half (i.e. lesser half) of num
    num0 = num[k:]

    return num1, num0

# Base cases
    if n == 0: return 0
    if n == 1: return int(X[0])*int(Y[0])

def karatsuba(i1, i2, base):

	# Small input consideration

	if (len(i1) == 1 or len(i2) == 1):
		return int(i1) * int(i2)

	# Get max length of integer - put zeros at the front of the shorter one
	n = max(len(i1), len(i2))
	#print(max_len)

	# Front fill with zeros so that lengths are equal
	# a, b = map(lambda element: element.zfill(max_len), [i1, i2])
	a = i1.zfill(n)
	b = i1.zfill(n)
	
	k = n // 2
	a1, a0 = a[:k], a[k:]
	b1, b0 = b[:k], b[k:]

	# Solve three sub-problems
	p0 = karatsuba(a0, b0, base)
	p1 = karatsuba((a0+a1), (b0+b1), base)
	p2 = karatsuba(a1, b1, base)
	
	# Combine the sub-problems
	return p2*pow(base, 2*k) + ((p1-p2-p0)*pow(base, k) + p0)

# Take a line of input as string
line = input()

# Check that its made up of digits between 0-9 and only has x2 white spaces - this a thing in and of itself
i1, i2, base = validate_input(line)

# School method addition of big numbers
result_sum = big_num_addition(i1, i2, base)

result_mult = karatsuba(i1, i2, base)

print (result_sum, result_mult)
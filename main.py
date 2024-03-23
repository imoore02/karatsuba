import string
import math

def validate_input(line):
	try:
		i1, i2, base = line.split()
		# The split was successful
	except ValueError:
		# Handle the specific exception (ValueError in this case)
		print("Error: Invalid input format. Expected three integers separated by spaces.")
		# Stop program execution by raising an exception
		raise SystemExit()
	
#	if not ( int(i2) == 1i1.isdigit() and i2.isdigit() and base.isdigit()):
#		print("Error: Non-digit characters found.")
#		raise SystemExit()
	
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
	max_len = max(len(str(i1)), len(str(i2)))

	# Front fill with zeros so that lengths are equal
	a, b = map(lambda element: element.zfill(max_len), [str(i1), str(i2)])

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
	
	# Map array to an int# Map array to an int
	result_int = int(''.join(map(str, result)))

	return result_int

def karatsuba(i1, i2, base):

	# Small input consideration
	if (len(str(i1)) == 1 or len(str(i2)) == 1):
		#print ("mult_base: ", mult_base(i1, i2, base))
		return mult_base(i1, i2, base)

    # Get max length of integer - put zeros at the front of the shorter one
	n = max(len(str(i1)), len(str(i2)))

    # Front fill with zeros so that lengths are equal
	a = str(i1).zfill(n)
	b = str(i2).zfill(n)
	
	k1 = (n + 1) // 2
	k = n // 2

	#print ("BASE:   ", base)
	a1, a0 = a[:k], a[k:]
	b1, b0 = b[:k], b[k:]
	#print("a1: ", a1, " a0: ", a0)
	#print("b1: ", b1, " b0: ", b0)
	#print("a1+a0: ", big_num_addition(a1, a0, base), " b1+b0: ", big_num_addition(b1, b0, base))
    # Solve three sub-problems
	p0 = karatsuba(a0, b0, base)
	p1 = karatsuba(a1, b1, base)
	p2 = karatsuba(big_num_addition(a1, a0, base), big_num_addition(b1, b0, base), base)
	
	#print("p0: ", p0)
	#print("p1: ", p1)
	#print("p2: ", p2)

    # Combine the sub-problems
	#print("\n")
	sub = sub_base(p2, p1, base)
	sub = sub_base(sub, p0, base)
	res = big_num_addition(p1*pow(10, 2*k1), (sub)*pow(10, k1), base)
	res = big_num_addition(res, p0, base)
	return res

def base_10_to_base_x(decimal_num, base):
    if decimal_num == 0:
        return "0"

    result = ""
    while decimal_num > 0:
        remainder = decimal_num % base
        result = str(remainder) + result
        decimal_num //= base

    return result

def sub_base(a, b, base):
	base = int(base)
	a_dec = base_x_to_base_10(a, base)
	b_dec = base_x_to_base_10(b, base)
	res_base = base_10_to_base_x(a_dec-b_dec, base)
	return int(res_base)

def mult_base(a, b, base):
     base = int(base)
     a_dec = base_x_to_base_10(a, base)
     b_dec = base_x_to_base_10(b, base)
     res_base = base_10_to_base_x(a_dec*b_dec, base)
     return int(res_base)

def base_x_to_base_10(num, base):
    num_str = str(num)
    result = 0
    
    for digit in num_str:
       digit_value = int(digit, base)
       result = result * base + digit_value
    
    return result

# Take a line of input as string
line = input()

# Check that its made up of digits between 0-9 and only has x2 white spaces - this a thing in and of itself
i1, i2, base = validate_input(line)

# School method addition of big numbers
result_sum = big_num_addition(i1, i2, base)

result_mult = karatsuba(i1, i2, base)

print (result_sum, result_mult)
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

	#		print("max_len: ", max_len)

	# Front fill with zeros so that lengths are equal
	a, b = map(lambda element: element.zfill(max_len), [i1, i2])

	#		print("a:", a)
	#		print("b:", b)

	# Create an array init to zero 
	#   --> max_len + 1 as the result can extend one beyond
	result = [0] * (max_len + 1) 

	#		print("result:", result)

	# Set c0 to 0
	carry = 0

	# Loop through digits
	for i in range(max_len - 1, -1, -1):
		#		print("i:", i)
		sum = int(a[i]) + int(b[i]) + carry
		#		print("sum:", sum)
		result [i + 1] = sum % int(base)
		#		print("result[i+1]:", result[ i + 1])
		carry = sum // int(base)
		#		print("carry:", carry)
	result[0] = carry

	if result[0] == 0:
		result.pop(0)
	
	return result



# Take a line of input as string
line = input()

# Check that its made up of digits between 0-9 and only has x2 white spaces - this a thing in and of itself
i1, i2, base = validate_input(line)

# School method addition of big numbers
result = big_num_addition(i1, i2, base)

print (result)
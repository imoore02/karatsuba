# Function to add two integers using the school method
def school_addition(num1, num2, base):
    carry = 0
    result = ""
    
    while num1 or num2 or carry:
        digit1 = int(num1[-1]) if num1 else 0
        digit2 = int(num2[-1]) if num2 else 0
        
        sum_ = digit1 + digit2 + carry
        carry = sum_ // base
        sum_ %= base
        
        result = str(sum_) + result
        
        if num1:
            num1 = num1[:-1]
        if num2:
            num2 = num2[:-1]
    
    return result

# Function to multiply two integers using Karatsuba algorithm
def karatsuba_multiplication(num1, num2, base):
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    
    n = len(num1)
    
    if n == 0:
        return "0"
    if n == 1:
        return str(int(num1) * int(num2))
    
    half = n // 2
    
    a = num1[:half]
    b = num1[half:]
    c = num2[:min(len(num2), half)]
    d = num2[min(len(num2), half):]
    
    ac = karatsuba_multiplication(a, c, base)
    bd = karatsuba_multiplication(b, d, base)
    
    a_plus_b = school_addition(a, b, base)
    c_plus_d = school_addition(c, d, base)
    ad_plus_bc = school_addition(karatsuba_multiplication(a_plus_b, c_plus_d, base),
                                 school_addition(ac, bd, base), base)
    
    zeros1 = '0' * half
    zeros2 = '0' * n
    
    return school_addition(school_addition(ac + zeros2, ad_plus_bc + zeros1, base), bd, base)

# Function to perform integer division
def integer_division(num1, num2, base):
    quotient = "0"
    remainder = num1
    
    while len(remainder) >= len(num2):
        shift = len(remainder) - len(num2)
        temp = num2 + '0' * shift
        
        if remainder < temp:
            temp = temp[:-1]
            shift -= 1
        
        subtracted = school_addition(remainder, temp, base)
        
        if subtracted == "0":
            break
        
        quotient = school_addition(quotient, '1' * shift, base)
        remainder = subtracted
    
    return quotient

# Main function
if __name__ == "__main__":
    num1, num2, base = input().split()
    base = int(base)
    
    # School Method Addition
    sum_ = school_addition(num1, num2, base)
    
    # Karatsuba Multiplication
    product = karatsuba_multiplication(num1, num2, base)
    
    # Integer Division
    division = integer_division(num1, num2, base)
    
    print(sum_, product, division)

#Write function to compute gcd ,km of two numbers 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute LCM using the formula
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function to compute both GCD and LCM
def gcd_lcm(a, b):
    return gcd(a, b), lcm(a, b)

# Example usage
num1 = 15
num2 = 20

gcd_result, lcm_result = gcd_lcm(num1, num2)
print(f"GCD of {num1} and {num2}: {gcd_result}")
print(f"LCM of {num1} and {num2}: {lcm_result}")

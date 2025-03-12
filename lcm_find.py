import math

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Finding LCM
lcm = abs(a * b) // math.gcd(a, b)
print("3sha-31")

# Output result
print(f"LCM of {a} and {b} is {lcm}")

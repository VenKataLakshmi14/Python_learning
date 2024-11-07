import math

# User inputs
num1 = float(input("Enter a number for square root: "))
num2 = float(input("Enter the base number for power calculation: "))
num3 = float(input("Enter the exponent for power calculation: "))
num4 = float(input("Enter a number for absolute value: "))
num5 = float(input("Enter a decimal number for ceiling and floor calculations: "))

# 1. Square Root
sqrt_result = math.sqrt(num1)

# 2. Power
power_result = math.pow(num2, num3)

# 3. Absolute Value
abs_result = math.fabs(num4)

# 4. Ceiling
ceil_result = math.ceil(num5)

# 5. Floor
floor_result = math.floor(num5)

# Display results
print(f"\nResults:")
print(f"1. Square Root of {num1}: {sqrt_result}")
print(f"2. {num2} raised to the power of {num3}: {power_result}")
print(f"3. Absolute value of {num4}: {abs_result}")
print(f"4. Ceiling of {num5}: {ceil_result}")
print(f"5. Floor of {num5}: {floor_result}")

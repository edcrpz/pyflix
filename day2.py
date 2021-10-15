# Data Types:
# String -- "Hello"
print("Hello"[4])  # Called Subscripting - this will output fifth (0 is first) character of Hello

# print("123" + "345")  -- this will not do mathematical operation, only concatenate
# For numbers, it should be Integer --- write only a number with nothing else
print(12_346+456_789)  # _ has no effect, only to be human readable

# Decimal number - Float
print(1.34)
# Boolean  (no double quotes ")
# True
# False

# len(1234)   # ---> this will not work, len() is only for string
print("\n--------------------------------------\n")
# print("Function type() -- checks type")
# data = input("Enter a data: ")
# print(type(data))            # check data type using type()
# converted_data = int(data)   # convert string "data" to integer using int()
# print("Converting to integer...\n")
# print(type(converted_data))
print("\n--------------------------------------\n")
print("Exercise 2.1 - Data Type manipulation")
two_digit_number = input("Type a two digit number: ")
# each digit should be added with each other
# Example:
# 39
# 3 + 9 = 12
digit1 = int(two_digit_number[0])
digit2 = int(two_digit_number[1])   # Use subscripting and then Convert to integer
print(digit1 + digit2)

print("\n--------------------------------------\n")

# Mathematical operations:
#  1 + 2
#  2 - 1
#  3 * 2
#  4 / 2  --> always end up with float output
#  2 ** 2 --> Exponent
# PEMDAS --> Parenthesis, Exponent, Multiplication/Division (Most left), Addition/Subtraction (Most left)
print("\n--------------------------------------\n")

print("Exercise 2.2 - BMI Calculator")
# BMI = weight (kg) / height ^2 (m^2)

height = input("enter your height in m: ")   # static
weight = input("enter your weight in kg: ")  # static

height_int = float(height)   # height needs to be float
weight_int = float(weight)   # convert str to float/int

bmi = weight_int / height_int ** 2

print("Your BMI is: " + str(bmi))
# Needs whole number, so convert again to integer (cuts and not round off)

# Rounding Off Numbers
# Use round()
print("Rounded: " + str(round(bmi, 2)))  # rounding to 2 decimal places

# Instead of converting to integer, can also use:
#  8 // 3   --> will cut off all decimal points, output is integer not float
print("\n--------------------------------------\n")

# More operations:
# Manipulate value from previous value
# score = 0
# score = score +1  ==== score += 1
#  += , -= , /= , *=

# F-Strings -- can easily print without converting data types to string
print("Using fstrings:")
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, and it's {isWinning} that you're winning.")

print("\n--------------------------------------\n")

print("Exercise 2.3 - Life in weeks")

age = input("What is your current age? ")  # static
age_int = int(age)

age_left = 90 - age_int   # How many years remaining
days = age_left * 365  # 365 in a year
weeks = age_left * 52  # 52 weeks in a year
months = age_left * 12  # 12 months in a year

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

print("\n--------------------------------------\n")

# Conditional statements
# IF-ELSE
#
# print("This is a test if else:")
# age = int(input("What is your age? "))
# if age >= 18:
#     print("You are at legal age.")
# else:
#     print("You are still minor.")

# > + =   greater than or equal to
# < + =   less than or equal to
# = + =   is equal to ( One '=' is assignment, not conditional)

# -------------------------------------------------
print("\n--------------------------------------\n")

print("Exercise 3.1 - Odd or Even exercise")

number = int(input("Which number do you want to check? "))              # MODULO - outputs the remainder
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

print("\n--------------------------------------\n")

# Nested IF-ELSE statement

# print("This is a test if else:")
# age = int(input("What is your age? "))
# if age >= 18:
#     print("You are at legal age.")
#     drive = input("Do you know how to drive a car? ")
#     if drive == 'yes':
#         print("Alright, here's the key of my car.")
#     else:
#         print("Sorry, you can't drive my car!")
# else:
#     print("You are still minor.")

# ELIF -- more conditions
# if condition1:
#    do A
# elif condition2:   #if condition 1 is true, it will not check condition2
#    do B
# else:              # if all conditions are False, will do else
#    do this

print("\n--------------------------------------\n")
#
print("Exercise 3.2 - BMI Calculator 2.0")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

height_int = float(height)   # height needs to be float
weight_int = float(weight)   # convert str to float/int
bmi = weight_int / height_int ** 2
final_bmi = round(bmi)

if final_bmi < 18.5:
    interpret = "are underweight"
elif final_bmi < 25:
    interpret = "have a normal weight"
elif final_bmi < 30:
    interpret = "are overweight"
elif final_bmi < 35:
    interpret = "are obese"
else:
    interpret = "are clinically obese"

print(f"Your BMI is {final_bmi}, you {interpret}")

print("\n--------------------------------------\n")
#
print("Exercise 3.3 - Leap Year exercise")
# Leap year checker
# Leap year:
# on every year that is evenly divisible by 4 EXCEPT
# every year that is evenly divisible by 100 UNLESS the year
# is evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:     # except 100
        if year % 400 == 0:   # unless 400
            print("It's a leap year.")
        else:
            print("It's NOT a leap year.")
    else:
        print("It's a leap year.")
else:
    print("It's NOT a leap year.")

print("\n--------------------------------------\n")

# Multiple IFs
# if condition1:
#    do A
#  ELSE is not required, this is just to check for additional conditions
# if condition2:
#    do B

print("\n--------------------------------------\n")

print("Exercise 3.4 - Pizza Order Practice")

# Small pizza: $15
# Medium pizza: $20
# Large pizza: $25
# Pepperoni for small: + $2
# Pepperoni for Medium or Large: + $3
# Extra cheese for any size: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? (S, M, L) ")
add_pepperoni = input("Do you want pepperoni? ")
extra_cheese = input("Do you want extra cheese? ")

final_bill = 0
if size == 'S':
    final_bill = 15
    if add_pepperoni == 'Y':
        final_bill += 2
elif size == 'M':
    final_bill = 20
    if add_pepperoni == 'Y':
        final_bill += 3
elif size == 'L':
    final_bill = 25
    if add_pepperoni == 'Y':
        final_bill += 3
else:
    print("You should choose a valid size for your pizza!")

if extra_cheese == 'Y':
    final_bill += 1

print(f"Your final bill is: ${final_bill}")

print("\n--------------------------------------\n")

# Logical Operators
# A and B   ---> should both be True
# C or D    ---> True if either is true
# not E    ---> reverse, true becomes false

print("\n--------------------------------------\n")

print("Exercise 3.5 - Love Calculator")

# Function <string>.lower() -- converts string to lower case
# Function <string>.count(n) -- counts the number of n occurrence

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2

T = (combined_name.lower()).count("t")
R = (combined_name.lower()).count("r")
U = (combined_name.lower()).count("u")
E = (combined_name.lower()).count("e")
L = (combined_name.lower()).count("l")
o = (combined_name.lower()).count("o")
V = (combined_name.lower()).count("v")

first_digit = T + R + U + E
second_digit = L + o + V + E

final_score = str(first_digit) + str(second_digit)
final_score_int = int(final_score)  # need to convert to int again to compare:

if final_score_int < 10 or final_score_int > 90:
    print(f"Your love score is {final_score_int}, you go together like Coke and Mentos.")
elif 50 >= final_score_int >= 40:
    print(f"Your love score is {final_score_int}, you are alright together.")
else:
    print(f"Your love score is {final_score_int}.")

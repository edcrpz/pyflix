# Function with INPUT

# def my_function(name):
#     print(f"Hi {name}!")
#
#
# my_function("Eduard")

# Parameter = name  (name of data being passed in)
# Argument = Eduard (actual value of data)

# Multiple Inputs:
#
# print("\n--------------------------------------\n")
#
#
# def my_function(name, location):
#     print(f"Hi {name}!")
#     print(f"Your location is: {location}")
#
#
# my_function("Eduard", "Philippines")


print("\n--------------------------------------\n")

# Positional arguments depend on the position of the
# arguments

# def my_function(name, location):
#     print(f"Hi {name}!")
#     print(f"Your location is: {location}")
#
#
# my_function("Eduard", "Philippines")  name = Eduard, location = Philippines


# Keyword arguments: disregard the position because it assigns

# def my_function(name, location):
#      print(f"Hi {name}!")
#      print(f"Your location is: {location}")
#
#
# my_function(location="Eduard", name="Philippines")

print("\n--------------------------------------\n")

# Exercise 8.1 - Area Calculator
import math  # to round UP

# In this case, we should round UP not round only
# round() round off 2.3 to 2
# math.ceil round off 2.3 to 3
#
# def paint_calc(height, width, cover):
#     no_of_cans = math.ceil((height * width)/cover)  # round UP e.g. 2.2 should be 3
#     print(f"You need to buy {no_of_cans} cans.")
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

print("\n--------------------------------------\n")

# Exercise 8.2 - Prime Number Checker


def prime_checker(number):
    prime = True                # checker
    for num in range(2, number):   # checks 2 to (n-1) (since n and n-1 should only be the factors/ divisible)
        if number % num == 0:    # checks if number / (2 to n-1) has a remainder
            prime = False            # if there's no remainder, meaning it's divisible = NOT PRIME

    if prime:
        print("It's a prime number")
    else:
        print("It's NOT a prime number")


i = 0
while i == 0:
    n = int(input("Check this number: "))
    prime_checker(number=n)

print("\n--------------------------------------\n")


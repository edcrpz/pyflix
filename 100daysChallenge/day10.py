# Functions with Output

# def my_function():
#     result = 3 * 2
#     return result
#
#
# output = my_function()
# print(output)    # outputs 6 as returned by function

# print("\n--------------------------------------\n")

# Name convert to TITLE CASE

# def format_name(f_name, l_name):
#     formatted_first = f_name.title()
#     formatted_last = l_name.title()
#     return f"{formatted_first} {formatted_last}"  # returns the desired formatted string
# #   print("test") # this will not be exectued
# # return tells the function it's the end of the function
#
#
# formatted_string = format_name('eDuArd', 'CORPUZ')  # save to variable the returned output
# print(formatted_string)

# print("\n--------------------------------------\n")

# Exercise 10.1 -- DAYS IN MONTH

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 # print("Leap year.")
#                 return True
#             else:
#                 # print("Not leap year.")
#                 return False
#         else:
#             # print("Leap year.")
#             return True
#     else:
#         # print("Not leap year.")
#         return False
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # january to december
#     if month > 12 or month < 1:
#         return "Invalid input for month."
#     if is_leap(year) and month == 2:   # february and a leap year
#         return 29    # February has 29 days in leap year
#     return month_days[month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(f"Number of days: {days}")

# print("\n--------------------------------------\n")

# DOCSTRINGS

# Documentation for your function
# When you hover to the function, it will show description
# of function

def format_name(f_name, l_name):
    """
    This function takes a first and last name and format it to return
    the title case version of the name.
    """
    formatted_first = f_name.title()
    formatted_last = l_name.title()
    return f"{formatted_first} {formatted_last}"  # returns the desired formatted string


formatted_string = format_name('eDuArd', 'CORPUZ')  # save to variable the returned output
print(formatted_string)












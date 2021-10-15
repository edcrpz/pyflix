# -----------------------------
print("\nExercise 1.1 - Print\n")
# -----------------------------
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")  # ' and " is the same, but should be use interchangeably
print("\n--------------------------------------\n")
# Use \n for new line
# print("This is a test\nThis is a test\nThis is a test\n\n")
#
# # Concatenation
# print("This is" + "how " + "to concatenate") # take note of spaces
# # Indentation is also important (start code in beginning of the line)
# # Don't forget the double quotes or it will get Syntax error
print("\n--------------------------------------\n")

#-----------------------------
print("Exercise 1.2 - Fix the code\n")
# -----------------------------
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')  # make "+" as text and not as concatenation
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print("\n--------------------------------------\n")
#
# print("Input Functions\n")
# input("Do you want to proceed?\n") # ask for Input
# print("Hello " + input("What is your name? ") + "!")  #print asked Input
# # OR
# name = input("What is your name again? ")  # Used Variable "name"
# print("Cool! Hello "+ name + "!")
print("\n--------------------------------------\n")


# -----------------------------
print("Exercise 1.3 - Return length of name\n")
# -----------------------------
name = input("Hi, what is your name?:")
print("Your name has " + str(len(name)) + " characters!")
# Convert integer to string using str(), calculate length using len()
print("\n--------------------------------------\n")

# -----------------------------
print("Exercise 1.4 - Switching values\n")
# -----------------------------

a = input("a: ")  # this should not be changed
b = input("b: ")  # this should not be changed
c = a    # acts as temporary container
a = b
b = c
print("a = " + a)  # this should not be changed
print("b = " + b)  # this should not be changed



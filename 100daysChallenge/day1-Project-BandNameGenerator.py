import time
# need to import time module for the time() function

# 1. Create a greeting for your program
print("\n\n----------------------------------------------")
print("|      Welcome to Band Name Generator!        |")
print("----------------------------------------------\n\n")

# 2. Ask the user for the city that they grew up in.

city = input("From which city did you grow up in?\n")
# 3. Ask the user for the name of a pet.
pet = input("What is the name of your pet?\n")
# 5. Make sure the input cursor shows on a new line

print("Please wait while the band name is being generated...")
time.sleep(3)

# 4. Combine the name of their city and pet and show them their band name.
print("\n\nYour band name could be ---> " + city + " " + pet)


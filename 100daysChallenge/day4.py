# Randomisation

# Random module
# Module - large piece of code, responsible for specific functionality
import random

# import test_module  # my own module - test_module.py
# print(test_module.name)
#
# test = random.randint(1, 10) # random integer between 100 and 200
# print(test)

# random.random()  ---> 0.00000000 - 0.999999999
# If we want 0 - 5:
# random.random() * 5  --> 0.00000 - 4.999999999
# print(random_float)
print("\n--------------------------------------\n")

# print("Exercise 4.1 - Heads or Tails exercise")
#
# coin = random.randint(0, 1)
# if coin == 1:
#     print("Heads")
# else:
#     print("Tails")

print("\n--------------------------------------\n")

# Python Lists (Data structure)
# Organizing and storing data in Python

# fruits = [item1, item2]
# fruits = ["Cherry", "Apple", "Orange"]

# Order is important
# print(states_of_america[0]) -- (0) is first in order
# Negative index starts counting from end -- (-1) is the last
#
# states_of_america = ["Delaware", "Pennsylvania", "New Mexico", "Washington"]
# print(states_of_america[2])
# print(states_of_america[-1])
#
# # Write into data:
# states_of_america[2] = "Old Mexico"
#
# # Add item in end of the list:
# states_of_america.append("Momoland")
# print(states_of_america)
#
# # Extend (add a set of items or list, just like add but more)
# states_of_america.extend(["California", "Manila"])

print("\n--------------------------------------\n")

# print("Exercise 4.2 - Banker Roulette")
#
# # Example input:  Angela, Ben, Jenny, Michael, Chloe
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# # <string>.split("<delimiter>")
# names = names_string.split(", ")    # puts into list after splitting
#
# number_of_names = len(names) - 1  # - 1 as lists starts from 0
# payer = names[random.randint(0, number_of_names)]
# print(f"{payer} is going to buy the meal today!")

# random.choice(<list>) --- chooses a random choice from list

print("\n--------------------------------------\n")

# Nested Lists
# dirty_dozen = ["Strawberries", "Nectarines", "Apples", "Grapes", "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Instead:

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# We can make nested list:
# dirty_dozen = [fruits, vegetables]
# print output shall have [[list1], [list2  ]]--- nested list

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][2])   ----> this will choose vegetables ([1]) first, then Tomatoes ([2])

print("\n--------------------------------------\n")

# print("Exercise 4.3 - Treasure map")
#
# # column, row
# # Sample input: 23  -- column 2, row 3
#
# row1 = ["🟫", "🟫", "🟫"]
# row2 = ["🟫", "🟫", "🟫"]
# row3 = ["🟫", "🟫", "🟫"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}\n")
# position = input("Where do you want to put the treasure? ")
#
# column = int(position[0]) - 1  # sample input = 2, this is index 1
# row = int(position[1]) - 1     # sample input = 3, this is index 2
#
# map[row][column] = "❌"
#
# print(f"\n{row1}\n{row2}\n{row3}")

print("\n--------------------------------------\n")



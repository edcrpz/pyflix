
# FOR Loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:   # do something for each item in list
#     print(fruit)
#     print(fruit + "pie")

print("\n--------------------------------------\n")
#
# print("Exercise 5.1 - Average Height")
#
# # Calculate average height in heights stored in list
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):    # range(1, 10)  gives 1,2,3,4,5,6,7,8,9 (before specified number 10)
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# # -----------------------
# total_height = 0
# no_of_heights = 0
#
# for i in student_heights:
#     total_height += i     # adds each items
#     no_of_heights += 1    # counter how many heights
#
# average = round(total_height / no_of_heights)
# print(f"The average height is: {average}")

print("\n--------------------------------------\n")

# print("Exercise 5.2 - Highest score in the class")
#
# # Don't use:
# # Function max() -- gets the highest value in a list
# #  min() == lowest value
#
# student_scores = input("Input a list of student scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # ------------
# highest = 0
# for score in student_scores:
#     if score > highest:
#         highest = score
# print(f"The highest score in the class is : {highest}")

print("\n--------------------------------------\n")

# Range function -- range of numbers
# for number in range(1, 10)  --- 1 up to number BEFORE 10
#    print(number)

# range(1, 10, 3) ---> step is 3
# for number in range(1, 10, 3):
#     print(number)   # --- > this will output 1, 4, and 7

print("\n--------------------------------------\n")

print("Exercise 5.3 - Adding even numbers")

total = 0
for num in range(2, 101, 2):
    total += num

print(f"The total is: {total}")

print("\n--------------------------------------\n")

print("Exercise 5.4 - FizzBuzz Job Interview")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:  # this should be checked first as it will be skipped if 3 or 5 is True
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)



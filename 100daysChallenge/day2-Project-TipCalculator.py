import time

print("\n\n----------------------------------------------")
print("|      Welcome to Tip Calculator!        |")
print("----------------------------------------------\n\n")

total_bill = float(input("What was the total bill? $"))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_people = int(input("How many people to split the bill? "))

final_bill = total_bill+(total_bill*percent/100)  # total bill + tip
cost = final_bill / no_people

# final_cost = round(cost, 2)
final_cost = "{:.2f}".format(cost)   # to have 2 decimal places even if data has only 1 decimal (e.g. 33.6)

print("Calculating...")
time.sleep(1)
print(f"Each person should pay: ${final_cost}")

# If result is exactly 1 decimal places but we want 2,
# example: 33.6 but we want to have 33.60
# Sample: $150, 12, 5
# We can use:
# "{:.2f}".format()
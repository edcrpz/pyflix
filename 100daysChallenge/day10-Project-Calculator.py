import calculator_art

print(calculator_art.logo)
# Calculator


# Addition
def add(n1, n2):
    return n1 + n2


# Substraction
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2
# Division


def divide(n1, n2):
    rounded = round(n1 / n2, 2)
    return rounded


operations = {
    '+': "add",
    '-': "subtract",
    '*': "multiply",
    '/': "divide"
}


def calculator():
    start = True   # loop for whole calculator
    while start:
        num1 = float(input("What's the first number?: "))

        for operation in operations:
            print(operation)

        run_calc = True  # this is loop for continuous calculation
        while run_calc:
            chosen_operation = input("Pick an operation: ")
            if chosen_operation not in operations:
                print("You entered an invalid operation. Please try again.")
            else:    # valid operation
                num2 = float(input("What's the next number?: "))

                    # we need something like:
                    # add(num1, num2)
                    # we get "add" from operations dictionary -- operations['+']
                    # use eval() to use string as function
                    # eval(<function_in_string> + "()")
                result = eval(operations[chosen_operation] + "(num1, num2)")
                print(f"\n\n{num1} {chosen_operation} {num2} = {result}\n")

                prompt_question = True
                while prompt_question:
                    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n").lower()
                    if choice == 'y':
                        num1 = result
                        prompt_question = False    # exit the loop to go back to line 37
                    elif choice == 'n':
                        # clear screen
                        prompt_question = False    # exit the 'prompt_question' loop
                        run_calc = False
                        calculator()# exit the loop run_calc to go back to 'start' loop
                    else:
                        print("Invalid input. Please try again.")
                        # continue to ask and stay in the loop


calculator()

# OR
# create function calculator()
# put all the code
# if prompt_question = n:
# call calculator() to start again from start
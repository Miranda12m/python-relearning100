# Functions as a variables and while loops using functions 

# Define the operation functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
# Set the functions as variables using the dicctionary 
operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}

#Set a new function "calculate( )" to perform the calculations
def calculate():
    should_accumulate = True
    num1 = float(input('Type the first number: ')) #Outside of the while loop 

    #Define a while loop to make the operations
    while should_accumulate: 
        for i in operations:
            print(i)
        operation_symbol = input('Type the operation symbol: ')
        num2 = float(input('Type the second number: '))
        prev_result = (operations[operation_symbol](num1, num2))
        print(f"{num1} {operation_symbol} {num2} = {prev_result}")

        choice = input(f"Type 'y' to continue calculating with {prev_result}, or type 'n' to start a new calculation: ")

        # If statement to continue the loop w the previous result as a num1 variable
        # To keep the prev result as num1 we set the "num1" variable outside the while loop
        if choice == 'y': 
            num1 = prev_result
            continue
        else: 
            should_accumulate = False
            print('\n' * 20)

            # Call the function inside of the function to continue with the loop
            calculate()
""" 
This file is the "app/calculator.py" file. It contains a simple calculator that can add, subtract, multiply, 
and divide numbers based on what the user types.
"""

from app.operations import Operations

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""
    
    print("Welcome to the calculator REPL! Type 'exit' to quit")
    
    while True:
        # Now we ask the user to type something, like "add 5 3". 
        # This will get the operation (like "add") and two numbers from the user.
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")

        # This part checks if the user typed "exit". If they did, we print a message and stop the calculator.
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break  # This "break" command tells the program to stop running the loop and exit.

        try:
            # Now we split the input into three parts: the operation (add, subtract, etc.) and the two numbers.
            operation, num1, num2 = user_input.split()
            # We have to make sure the numbers are actually numbers, so we convert them to floats.
            num1, num2 = float(num1), float(num2)
        except ValueError:
            # If the user doesn't type something correctly, like typing letters where numbers should be, we show an error.
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue 

        # Now we check what operation the user asked for and call the right function (addition, subtraction, etc.).
        if operation == "add":
            result = Operations.addition(num1, num2)  
        elif operation == "subtract":
            result = Operations.subtraction(num1, num2)  
        elif operation == "multiply":
            result = Operations.multiplication(num1, num2)
        elif operation == "divide":
            try:
                result = Operations.division(num1, num2)
            except ValueError as e:
                # This part handles the case where someone tries to divide by zero, which we can't do.
                # The division function will throw an error if someone tries dividing by zero, and we catch that error here.
                print(e)  # Show the error message.
                continue  # Go back to the top of the loop and try again.
        else:
            # If the user types an operation we don't understand, we show them a message.
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
            continue  # Go back to the top of the loop and try again.

        # Finally, we print the result of the operation (for example, "Result: 8").
        print(f"Result: {result}")


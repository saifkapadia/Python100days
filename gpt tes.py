# 1. Basic Input and Output
# Write a Python program that:
# Asks the user for their name.
# Greets the user with a message like "Hello, [Name]! Welcome to Python."
# What would your code look like?

# 2. Simple Calculation
# Write a program that:
# Asks the user to input a number.
# Doubles the number and prints the result.
# What would your code look like?

# 3. Error Handling
# What happens if the user enters a non-numeric value in the calculator program you just learned? How would you modify the program to handle such an error gracefully?
# (Hint: Use a try and except block.)

print("Please enter your name ")

name1 = input()

print(f"Hello, {name1} Welcome to Python.")

print("it was nice meeting you , let me make you a calculator which will take inputs from you and double the output" )

try :

    num1 = float(input("please enter first choice of  number" ))
    num2 = float(input("please enter second choice of  number" ))

    num3 = num1*2
    num4 = num2*2

    print(f"The numbers are {num3} and {num4}" )

except ValueError:

    print("Wrong input")


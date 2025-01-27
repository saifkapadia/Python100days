# print("Welcome")

# number = int (input("Please enter a number"))


# print (number%2)
# while True :

#     try :
#         if number % 2 ==0  :

#         print("The number is Even")

#         else :
#         print("The number is Odd")

#         break

#     except ValueError :
#         print("wrong input") 

print("Welcome")

# Ask the user for a number
while True:  # Keep asking until valid input is provided
    try:
        number = int(input("Please enter a number: "))  # Input converted to integer
        print (number%2)
        # Check if the number is even or odd
        if number % 2 == 0:
            print("The number is Even")
        else:
            print("The number is Odd")
        
        break  # Exit the loop after a valid input is processed
    except ValueError:
        # Handle invalid input
        print("Wrong input! Please enter a valid number.")
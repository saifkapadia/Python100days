# Task: Number Guessing Game
# Write a Python program that:
# Randomly picks a number between 1 and 10.
# Asks the user to guess the number.
# Tells the user if their guess is too high, too low, or correct.
# Keeps asking until the user guesses the correct number.


import random

secret_num = random.randint(1,10)

attempts = 0

while True :

    try:

        guess = int(input("Please enter your guess"))

        attempts +=1

        if guess < secret_num :
            print("Low")
        
        elif guess > secret_num :
            print("high")

        else:
            print(f"Sahi Jawab in {attempts}")
            
            break 
    
    except ValueError :
        print("wrong input")        


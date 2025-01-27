# import random
# # random_integer = random.randint(1,10)
# # print(random_integer)

# # random_floatinteger = random.random()
# # print(random_floatinteger)

# print("Wecome to Rock,paper,scissors ")

# human = int(input("Please choose your choice , for rock use 0 , for paper use 1 , for scissors use 2 "))
# print (human)

# # print(human_input)

# # random_rps = ["rock","paper","scissors"]

# computer = random.randint(0,2)
# print(computer)
# # computer = random.choice(random_rps)

# # if human_input =1 & random_rps

# # print(computer)

# if human == 0 and computer == 2 :
#     print ("You Won")

# elif computer > human :
#     print("you loose ")

# elif computer == human :
#     print("Draw ")

import random

print("Welcome to Rock, Paper, Scissors!")

# Map numbers to choices
choices = ["rock", "paper", "scissors"]

# Prompt the user for input
human = int(input("Please choose your choice: 0 for rock, 1 for paper, 2 for scissors: "))

# Validate the input
if human not in [0, 1, 2]:
    print("Invalid choice! Please restart the game and select 0, 1, or 2.")
    exit()

# Display human choice
print(f"You chose: {choices[human]}")

# Computer makes a random choice
computer = random.randint(0, 2)
print(f"Computer chose: {choices[computer]}")

# Determine the result
if human == computer:
    print("It's a draw!")
elif (human == 0 and computer == 2) or (human == 1 and computer == 0) or (human == 2 and computer == 1):
    print("You won!")
else:
    print("You lost!")
import random
# random_integer = random.randint(1,10)
# print(random_integer)

# random_floatinteger = random.random()
# print(random_floatinteger)

rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Wecome to Rock,paper,scissors ")

game_images = [rock,paper,scissors]

human = int(input("Please Enter your choice ,for rock -0 ,for paper-1 , for scissors - 2 \n" ))

computer = random.randint(0,2)

if human>=0 and human <=2 :
    print(game_images[human])

# print(f"human chose {human}")
print(f"computer chose:")
print(game_images[computer])

# if human > computer :
if human >=3 or human<= 0 :
    print("you typen an invalid number , you loose !")

elif human ==0 and computer == 2 :
    print("you won")

elif computer > human :
    print("you loose")

elif human > computer :
    print("You won")

elif human == computer :
    print("draw")

# if computer ==0 and human == 2 :
#     print("you loose")

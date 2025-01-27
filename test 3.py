
print("Welcome to the Robot")
while True :
    try :
        num = int(input("please enter a number"))

        if num % 2 == 0 :
            print("Your number is even")

        else :
            print ("Your number is odd ")
        break 
    except ValueError :

            print("Please enter a number")
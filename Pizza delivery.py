print("Welcome to python pizza delivery!!!")
size = input("Please selcet a size, S , M , L :-")
pepperoni = input("Do you want pepperoni?Y or N : ")
cheese = input("Do you want cheese ?Y or N : ")

bill = 0 

if size == 'S' :
    print("Cost of small pizza is $ 5")
    bill +=5

elif size == 'M' :
    print("Cost of small pizza is $ 15")
    bill +=15

elif size == 'L' :
    print("Cost of small pizza is $ 25")
    bill +=25

else:
    print("Invalid size selected. Please restart and choose S, M, or L.")

if pepperoni == 'Y' :

    bill = bill + 3

    print("you have added extra pepperoni")

if cheese == 'Y' :
    bill = bill + 2
    print("you have added extra cheese")


    print(f"Your final bill is: ${bill}")
    print("Thank you for visiting us!")

else :
    print("Thank you for visiting us ")
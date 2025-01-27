print("Welcome to the roller coaster")

height = int (input("Please enter your height"))
age = int (input("Please enter your age"))
bill = 0
if height >= 120 :

    print("You can ride")

    if age <7 :
        bill = 5 
        print("Please pay 5$")

    elif 7 < age <= 18 :
        print("Please pay 9$")
        bill = 9
    elif 18 < age <= 36 :
        print("Please pay 18$")
        bill = 18

    elif age >= 45 and age <= 55 :
        print("your ride is on us ")
        bill += 0
        
    
    

    wants_photo = input("Do you want a photo ? Type y for Yes and n for No ")    
    if wants_photo == "y" :
        bill = bill +3 
        print(f"Yor total bill is {bill} $")

    else:
        print(f"Yor total bill is {bill} $")
else :
    print("Come back when your height is 120")






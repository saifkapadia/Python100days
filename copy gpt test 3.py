
attempts = 0 

while True :

    try:

        guess = int(input("Please enter your guess"))

        attempts +=1

        if guess <= 0 :
            print("Please enter the right password ")
        
        

        else:
            print(f"The right password was a psitive number which you gave in  {attempts}")
            
            break 
    
    except ValueError :
        print("wrong input")       
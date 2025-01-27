height = float(input("Please enter height in meter"))
weight = float(input("Please enter your weight in Kg"))

bmi = weight / (height ** 2)

print (f"your BMI is {bmi:.2f}")

if bmi < 18 :
    print("you are underweight")

elif 18.5 <= bmi < 24.9:
    print("you have normal weight")

elif 25 <= bmi < 29.9:
    print("you are Overweight")

else :
    print("You are obese")
# print("Hello to water stopper")

#  waterLevel = int(input("Please enter the level at which you wabt the water to stop"))

# try :
#     if waterLevel <= 80 :
#     print ("Let the water flow")

#     else:
#         print("Start draining the water ")

print("Hello to water stopper")

# Ask the user to input the water level
try:
    waterLevel = int(input("Please enter the level at which you want the water to stop: "))

    # Check the water level and take appropriate action
    if waterLevel <= 80:
        print("Let the water flow")
    else:
        print("Start draining the water")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
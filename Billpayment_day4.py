import random

friends = ["Saif","Bilal","Saif Q","Tanveer","Ammar"]
friendsrizvi = ["Riyaz","Afaque","Wasi","Junnu","Kazi","SaifK"]

all_friends = [friends,friendsrizvi]

# print(len(all_friends))

print(all_friends[0][1])

print(len(friends))

bill_payment = random.choice(friends)

print(bill_payment)

payment_bill = random.randint(0,4)

print(friends[payment_bill])
hours = int(input("How many hours did you park? "))

if hours <= 2:
    print("You have to pay 5 PLN.")
elif hours <= 6:
    print("You have to pay 15 PLN.")
else:
    print("You have to pay 20 PLN.")
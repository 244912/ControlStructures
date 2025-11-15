# Program to check PIN code with 3 attempts
correct_pin = "0805"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter the PIN code: ").strip()
    attempts += 1
    
    if pin == correct_pin:
        print("Correct PIN! Access granted.")
        break
    else:
        print("Incorrect...")
        if attempts == max_attempts:
            print("Sorry, your payment card has been blocked.")
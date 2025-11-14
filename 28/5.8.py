balance = 1000
pin = "1234"

# Check PIN
while True:
    entered = input("Enter PIN: ")
    if entered == pin:
        print("PIN correct")
        break
    else:
        print("Wrong PIN!")

# ATM Menu
while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")
    
    choice = input("Choose: ")

    if choice == "1":
        print(f"Balance: {balance}")
    
    elif choice == "2":
        amount = float(input("How much to deposit? "))
        balance += amount
        print("Deposited!")
    
    elif choice == "3":
        amount = float(input("How much to withdraw? "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn!")
        else:
            print("Not enough money!")
    
    elif choice == "4":
        old = input("Enter old PIN: ")
        if old == pin:
            new = input("Enter new PIN: ")
            pin = new
            print("PIN changed!")
        else:
            print("Wrong old PIN!")
    
    elif choice == "5":
        print("Goodbye!")
        break
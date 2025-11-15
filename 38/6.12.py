# Calculate amount to pay with discount for more than 2 products

quantity = int(input("Number of products purchased: "))
price = float(input("Product price: "))

total = 2 * price

if quantity > 2:
    remaining = quantity - 2
    total += remaining * price * 0.75

print(f"Amount to pay: {total:.2f}")
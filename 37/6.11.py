# Check if product price dropped by at least 10%

current_price = float(input("Current product price: "))
previous_price = float(input("Previous product price: "))
drop_percent = ((previous_price - current_price) / previous_price) * 100
if drop_percent >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(drop_percent)}%")
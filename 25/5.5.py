###
# Sums numbers entered by user and calculates the arithmetic mean
#
total_sum = 0
count = 0  # Counts how many numbers were entered (excluding 0)

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1  
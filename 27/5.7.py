###
# Timer that counts down from a given number to zero
# Last five seconds are printed in words
#
import time

# Dictionary to convert numbers 1-5 to words
word_numbers = {
    5: 'five',
    4: 'four',
    3: 'three',
    2: 'two',
    1: 'one'
}

# Get starting number from user
n = int(input("Enter the starting number: "))

# Countdown loop
while n > 0:
    if n <= 5 and n in word_numbers:
        print(word_numbers[n])
    else:
        print(n)
    
    time.sleep(1)  # Wait 1 second
    n -= 1

print("Time's up!")
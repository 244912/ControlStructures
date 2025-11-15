age = int(input("How old are you? "))

if age < 13:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teen.")
elif age <= 64:
    print("You are an Adult.")
else:
    print("You are a Senior.")
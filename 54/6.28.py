a, b = 0, 1
count = 0
max_terms = 20

print("0", end=' ')
count += 1

while count < max_terms:
    print(b, end=' ')
    a, b = b, a + b
    count += 1

print("...")
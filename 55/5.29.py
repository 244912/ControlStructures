N = int(input("How many prime numbers do you want to see? "))

number = 2          
found = 0           

while found < N:
   
    is_prime = True
    
    for i in range(2, number):  
        if number % i == 0:     
            is_prime = False
            break               
    
    if is_prime:
        print(number, end=' ')
        found += 1              
    
    number += 1  

print()
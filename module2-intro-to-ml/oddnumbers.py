numbers = list(range(1,11))
prime_numbers = [ ]
even_numbers = [ ]
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    if num > 1:
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Numbers from 1 to 10:", numbers)
print("Even numbers:", even_numbers)
print("Prime numbers:", prime_numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(2,16):
    if i == 2:
        primes.append(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            break
        else:
            is_prime = False
    if is_prime:
        not_primes.append(i)
    else:
        primes.append(i)
print(f"Primes: {primes}") # простые
print(f"Not Primes: {not_primes}") # сложные









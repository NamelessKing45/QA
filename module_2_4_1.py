
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    while is_prime is True:
        try:
            primes.append(num)
            break
        except ValueError:
            pass
    while is_prime is False:
        try:
            not_primes.append(num)
            break
        except ValueError:
            pass
print(f'{primes}\n{not_primes}')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 120, 101]
primes = []
not_primes = []
print(f'Исходный список: {numbers}')
for i in numbers:
    if i > 1:  # т.к. 1 не является ни простым, ни непростым числом, то его пропускаем
        is_prime = True

        for j in range(2, i):
            if i % j == 0:  #проверяем на простое число
                is_prime = False
                break

        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)


print(f'Простые числа: {primes}')
print(f'Непростые числа: {not_primes}')
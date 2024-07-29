from random import randint

# генерируем случайное число из диапазона от 3 до 20
n = randint(3, 20)
print(f'Число из первой вставки: {n}')
finish_code = ''
for i in range(1, n):
    for j in range(1, i):
        if n % (i + j) == 0:
            finish_code = finish_code + str(j) + str(i)  # преобразовываем в строку нашу пару и добавляем к уже имеющимся
            continue

print(f'Нужный код: {finish_code.replace(" ", "")}')

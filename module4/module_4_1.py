from fake_math import divide as fake_
from true_math import divide as true_

while True:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(f'Выполнение функции fake_math - {fake_(a, b)}')
    print(f'Выполнение функции true_math - {true_(a, b)}')

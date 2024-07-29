first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('Все введенные числа равны -', 3)
elif first == second or first == third or second == third:
    print('Два введенных числа равны между собой -', 2)
else:
    print('Среди введенных чисел нет равных чисел - ', 0)

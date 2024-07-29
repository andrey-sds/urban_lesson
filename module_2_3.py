my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(f'Мой список: {my_list}')
my_list_idx = 0
while my_list_idx < len(my_list):
    if my_list[my_list_idx] > 0:
        print(f'Положительные числа списка: {my_list[my_list_idx]}')
        my_list_idx += 1
        continue
    elif my_list[my_list_idx] < 0:
        print(f'Встретили отрицательное число - выход: {my_list[my_list_idx]}')
        break
    elif my_list[my_list_idx] == 0:
        print('Встретили 0, продолжаем работу')
        my_list_idx += 1
        continue
    else:
        print('Достигнут конец списка')
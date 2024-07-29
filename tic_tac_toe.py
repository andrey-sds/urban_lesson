def check_winner(area):
    # Проверяем строки
    for row in area:
        if row[0] == row[1] == row[2] and row[0] != '*':
            return row[0]

    # Проверяем столбцы
    for col in range(3):
        if area[0][col] == area[1][col] == area[2][col] and area[0][col] != '*':
            return area[0][col]

    # Проверяем диагонали
    if area[0][0] == area[1][1] == area[2][2] and area[0][0] != '*':
        return area[0][0]
    if area[0][2] == area[1][1] == area[2][0] and area[0][2] != '*':
        return area[0][2]

    # Если победителя нет
    return None


def draw_area():
    for i in area:
        print(*i)
    print()


area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print("Добро пожаловать в игру крестики-нолики")
print("----------------------------------------")
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = 'O'
        print('Ходят нолики!')
    else:
        turn_char = 'X'
        print('Ходят крестики!')
    row = int(input("Введите номер строки (1,2,3): ")) - 1
    column = int(input("Введите номер столбца (1,2,3): ")) - 1
    if row > 2 or column > 2:
        print('Вы вышли за пределы поля. Пропускаете ход')
        draw_area()
        continue
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Ячейка уже занята. Вы пропускаете ход.')
        draw_area()
        continue
    draw_area()
    winner = check_winner(area)
    if winner:
        print(f"Победитель: {winner}")
        break
    elif turn == 9:
        print("Ничья")
        break
    else:
        print("Продолжаем игру")

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        n_row = []
        for j in range(m):
            n_row.append(value)
        matrix.append(n_row)
    return matrix


n_val = int(input('Введите количество строк: '))
m_val = int(input('Введите количество столбцов: '))
val = int(input('Введите числовое значение: '))
matrix = get_matrix(n_val, m_val, val)
print('Полученная матрица', matrix)


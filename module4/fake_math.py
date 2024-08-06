def divide(x, y):
    if y == 0:
        return (f'Ошибка! На {y} делить нельзя!')
    else:
        return x/y

if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(10, 0))
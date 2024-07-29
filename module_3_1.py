calls = 0


def counts_calls():
    global calls
    calls += 1


def string_info():
    string_ = input('Введите строку: ')
    cort1 = [len(string_), string_.upper(), string_.lower()]
    print(cort1)
    counts_calls()


def is_contains(a: str, b: list):
    print(b)
    print(a.lower() in (j.lower() for j in b))
    counts_calls()


string_info()
string_info()

i = 0
b = []
a = input('Ведите строку для поиска в списке: ')

while i < 3:
    b.append(input(f'Введите {i + 1} элемент списка: '))
    if i == 3:
        break
    i += 1
is_contains(a, b)

b = []
i = 0
a = input('Введите строку для поиска в списке: ')

while i < 3:
    b.append(input(f'Ведите {i + 1} элемент списка: '))
    if i == 3:
        break
    i += 1
is_contains(a, b)
print(calls)

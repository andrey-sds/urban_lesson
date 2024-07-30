def print_params(a=1, b='string', c=True):
    print(f'Значения a, b, c:\r\n{a} {b} {c}')


values_list = ['Apple', 22, 13.5]
values_dict = {'a': 44, 'b': False, 'c': 'BaNan'}
print('Вывод с параметрами по умолчанию.')
print_params()
print('Вывод с передачей именнованого параметра.')
print_params(b=25)
print('Вывод с передачей именнованого параметра 2.')
print_params(c=[1,2,3])

print(f'Распаковка списка.')
print_params(*values_list)
print(f'Распаковка словаря.')
print_params(**values_dict)

values_list2 = [4, 'Кокос']

print(f'Распаковка + отдельные параметры.')
print_params(*values_list2, 42)

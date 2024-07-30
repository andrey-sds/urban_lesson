def print_params(a=1, b='string', c=True):
    print(f'Вывод параметров \r\na, b, c:\r\n{a} {b} {c}')


values_list = ['Apple', 22, 13.5]
values_dict = {'a': 44, 'b': False, 'c': 'BaNan'}
print_params()
print_params(b=25)
print_params(c=[1,2,3])

print(f'Распаковка списка и словаря:')
print_params(*values_list)
print_params(**values_dict)

values_list2 = [4, 'Кокос']

print(f'Распаковка + отдельные параметры:')
print_params(*values_list2, 42)

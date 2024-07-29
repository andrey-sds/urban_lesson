# my_dict = {"Andrey": 2000, "Vika": 2003, "Lena": 1998, "Sergey": 2005, "Oleg": 1990}
# print(f'Словарь: {my_dict}')
# print(f'Значение из словаря: {my_dict["Vika"]}')
# print(f'Значение из словаря  с помощью get: {my_dict.get("Sergey")}')
# name = input('Введите имя для поиска в словаре: ')
# print(f'Проверка имени в словаре get: {my_dict.get(name,"Имя отсутствует в словаре")}')
# my_dict.update({"Denis": 1992, "Oksana": 2007, "Alisa": 2010})
# print(f'Добавленные пары: {my_dict.items()}')
# pop_from_dict = input('Введите имя для извлечения из словаря: ')
# print(f'Удаление из словаря:  {pop_from_dict}. Удаленное значение - {my_dict.pop(pop_from_dict)} \r\n Новый словарь: {my_dict}')


# Множество
List_ = ["dog", "cat", "wolf", "bear", 1, 16, 16, 22, 1]
my_set = set(List_)
print(f'Полученное множетсво: {my_set} - проверка типа: {type(my_set)}')

add_el1 = input('Введите первый элемент для добавления в множество: ')
my_set.add(add_el1)
add_el2 = input('Введите второй элемент для добавления в множество: ')
my_set.add(add_el2)
print(f'Полученное множество: {my_set}')

del_str = input('Введите строку для удаления из множества, если хотите удалить число нажмите Enter: ')
del_ = input('Введите число для удаления из множества, иначе нажмите Enter: ')
my_set.discard(del_str)

if del_ != '':
    del_int = int(del_)
    my_set.discard(del_int)
else:
    pass
print(f'Удаленный элемент: {del_str} {del_}. Полученное множество: {my_set}')



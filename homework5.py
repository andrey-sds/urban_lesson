# Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
#
# Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#
# Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

immutable_var = (23, "cherry", "tomato", "pineapple", 5, "44")
print(f'Кортеж: {immutable_var}')
print(44 in immutable_var)
# immutable_var[5] = 44  # в отличие от списков кортежи не поддерживают изменения элементов.  /
                         # Поэтому кортежи удобно использовать для хранения настроек. /
                         # но можем изменить элементы списка внутри кортежа
immutable_var_ex = (23, ["cherry", "tomato", "pineapple"], 5, "44")
print(f'Кортеж: {immutable_var_ex}')
immutable_var_ex[1][1]="apple"
print(f'Измененный элемент в списке кортежа: {immutable_var_ex}')
mutable_list = ["cherry", "tomato", "pineapple", False]
print(f'Начальный список: {mutable_list}')
mutable_list.append("True")
print(f'Добавление элемента в список: {mutable_list}')
mutable_list.remove(False)
print(f'Удаление элемента в списке: {mutable_list}')
mutable_list.extend([40, "potato"])
print(f'Добавление элементов в список: {mutable_list}')
mutable_list[4] = "apple"
print(f'Изменение элемента в списке: {mutable_list}')
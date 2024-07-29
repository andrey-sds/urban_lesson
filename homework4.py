# my_string = input("Введите строку: ")
#
# print("Вы ввели", len(my_string), "символов")
#
# print("Введенная строка в вернем регистре:", my_string.upper())
# print("Введенная строка в нижнем регистре:", my_string.lower())
# print("Удаление пробелов:", my_string.replace(' ',''))
# print("Первый символ введенной строки:",my_string[0])
# print("Последний символ введенной строки:",my_string[-1])

my_string = input("Введите имя: ")
current_year = 2024
birth_of_year = int(input("Введите год Вашего рождения:"))
age = current_year - birth_of_year
text_age = str(age)[-1]

if 1 < abs(int(text_age)) < 5 or 10 <= age <= 19:
    text_age = 'год/а'
else:
    text_age = 'лет'

print("Здравствуйте,", my_string)
print("В это году Вам", age, text_age)




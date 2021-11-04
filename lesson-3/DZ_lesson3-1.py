#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""
Функция возвращает результат математического деления или None и ошибку в случае деления на 0.
    my_devision(dividend, devisor)
    где  dividend - делимое
         devisor - делитель
         div_type = тип деления (не обязательный параметр):
            1 - математическое (по умолчанию)
            2 - получение целой части деления
            3 - получение остатка от деления
"""
def my_devision(dividend, devisor, div_type = 1):

    if div_type == 1:
        try:
            return(dividend / devisor)
        except ZeroDivisionError:
            print('Ошибка деления на 0!')
            pass
    elif div_type == 2:
        try:
            return(dividend // devisor)
        except ZeroDivisionError:
            print('Ошибка деления на 0!')
            pass
    elif div_type == 3:
        try:
            return(dividend % devisor)
        except ZeroDivisionError:
            print('Ошибка деления на 0!')
            pass


my_div = float(input('Ведите делимое число: ')) # Порлучаем от пользователя делимое
my_dev = float(input('Ведите делитель: ')) # Получаем от пользователя делитель

print('Результат деления:', my_devision(my_div, my_dev)) # Выводим результат математического деления
print('Целая часть деления:', my_devision(my_div, my_dev, 2)) # Выводим результат целой части деления
print('Остаток от деления:', my_devision(my_div, my_dev, 3)) # Выводим результат остаток от деления
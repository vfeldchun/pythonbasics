# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.
##################################################################################################################
"""
Клас MyDivExeption являеться потомком класа Exception и предназначен для обработки ошибки деления на 0
Клас имеет следующие атрибуты:
    my_exeption_msg - Собственноое сообщение об ошибке деления на 0
Клас имеет следующие методы:
    __init__(self, exeption_msg) - инициализирует обьект класа
    где:
        exeption_msg - заданное при инциализации сообщение об ошибке
    __str__(self) - перегружает строку при выводи на экран обьекта класа
"""
class MyDivExeption(Exception): #Обьявляем клас потомок класа Exception
    my_exeption_msg = '' # обьявляем глобальную переменую класа содержащую собственное сообщение об ошибке

    def __init__(self, exeption_msg): # Обьявляем метод класа
        self.my_exeption_msg = exeption_msg # Инициализируем сообщение об ошибке переданной строкой

    def __str__(self): # Обьявляем метод класа
        return self.my_exeption_msg # При выводе обьекта класа на экран выводим сообщение об ошибке

################################################################################################################
# Основное тело программы
################################################################################################################
print('Программа деления двух чисел.\nДля выхода нажмите q!')
while True: # Открываем бесконечный цикл
    while True: # Открываем бесконечный цикл на ввода первого числа
        a = input('Введите первое число: ') # Получаем первое введенное пользователем число
        if a == 'q': # Если вместо ччисла ввели q
            exit() # Выходим из программы
        else: # в противном случае
            try: # пробуем
                a = int(a) # преобразовать a в целое число
                break # выходим из цикла
            except ValueError: # если ошибка
                print(f'Вы ввели не число! Повторите ввод!') # выводим сообщение

    while True: # Открываем бесконечный цикл на ввода второго числа
        b = input('Введите второе число: ') # Получаем второе введенное пользователем число
        if b == 'q': # Если вместо ччисла ввели q
            exit() # Выходим из программы
        else: # в противном случае
            try: # пробуем
                b = int(b) # преобразовать a в целое число
                break # выходим из цикла
            except ValueError: # если ошибка
                print(f'Вы ввели не число! Повторите ввод!') # выводим сообщение

    try: # пробуем
        if b == 0: # Если второе число равно 0
            # Создаем обьект класа MyDivException c текстом ошибки и поднимаем ошибку
            raise MyDivExeption(f'Ошибка деления на 0 для {a}/{b}!') # Создаем обьект класа MyDivException c текстом
        else: # в противном случае
            print(f'Результат {a}/{b} = {round(a/b, 24)}')  # Выводим результат деления
    except MyDivExeption as my_excp: # если обьект поднят и ошибка поднята
        print(my_excp) # Выводим сообщение об ошибке

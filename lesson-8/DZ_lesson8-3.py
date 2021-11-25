# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

class MyValueErrorException(Exception):
    exception_msg = ''

    def __init__(self, msg_text):
        self.exception_msg = msg_text

    def __str__(self):
        return self.exception_msg

    @staticmethod
    def check_is_str(param):
        num_t = 0
        try:
            num_t = int(param)
            return num_t
        except ValueError:
            return -1
#############################################################################################################
#
#############################################################################################################

print('Программа формирования числового списка.\nДля выхода из программы нажмите q!')
only_number_list = []
while True: # Открываем бесконечный цикл
    a = input('Введите число: ') # Получаем первое введенное пользователем число
    if a == 'q': # Если вместо ччисла ввели q
           break # Выходим из программы
    else: # в противном случае
        a = MyValueErrorException.check_is_str(a)
        if a != -1:
            only_number_list.append(a)
        else:
            try:
                raise MyValueErrorException(f'Введеное значение не являеться числом!')
            except MyValueErrorException as val_err:
                print(val_err)

print(f'Вы ввели следующую последовательность чисел:\n'
      f'{only_number_list}')



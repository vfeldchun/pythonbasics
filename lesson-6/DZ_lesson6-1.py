#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
from time import sleep # импорт функции sleep из модуля time

"""
Класс TrafficLight предназначен для переключения цветов светофора как с контролем последовательности переключения 
так и без контроля последовательности. Возможные варианты цветов ('красный', 'желтый', 'зеленый').
В случае активации контроля последовательности возможный авриатнт переключения:
красный -> желтый -> зеленый -> красный -> желтый ...
По умолчанию контроль последовательности переключения отключен!
Так же можно изменять задержку в секундах для каждого цвета через глобальные переменные класса:
green_delay, red_delay, yellow_delay
"""
class TrafficLight(): #Обьявление класса
    sequence_control = False # Выключаем контроль последовательности переключения (по умолчанию)
    __color_list = ['красный', 'желтый', 'зеленый'] # Задаем приватный список цветов
    previos_color = __color_list[0] # Устанавливаем предидущий цвет в 'красный'
    green_delay = 5 # Задаем задержку в секундах для зеленого цвета
    red_delay = 7 # Задаем задержку в секундах для красного цвета
    yellow_delay = 2 # Задаем задержку в секундах для желтого цвета
    """
    Приватная функция __running выполняет переключение светофора на указанный цвет и формирует задержку на определенное
    число секунд для каждого цвета после переключения. Предназначена для использования только внутри обьекта класса.
        __running(self, selected_color)
        где:
            selected_color - Выбраный цвет для переключения
    """
    def __running(self, selected_color): #Обьявление приватной функции
        if selected_color == self.__color_list[0]: # Если переданый цвет красный
            print(f'На светофоре зажегся \033[31m{selected_color}\033[0m цвет на следующие {self.red_delay} секунд')
            sleep(self.red_delay) # Задержка на количество секунд указаных в red_delay (7 по умолчанию)
        elif selected_color == self.__color_list[1]: # Если переданый цвет желтый
            print(f'На светофоре зажегся \033[33m{selected_color}\033[0m цвет на следующие {self.yellow_delay} секунд')
            sleep(self.yellow_delay) # Задержка на количество секунд указаных в yellow_delay (2 по умолчанию)
        elif selected_color == self.__color_list[2]: # Если переданый цвет зеленый
            print(f'На светофоре зажегся \033[32m{selected_color}\033[0m цвет на следующие {self.green_delay} секунд')
            sleep(self.green_delay) # Задержка на количество секунд указаных в green_delay (5 по умолчанию)
    """
    Функция switch_color, доступная для вызова из вне для обьекта класса. Выполняет запуск функции переключения 
    светофора и в случае включенного контроля режима перекдчения отслеживает правильную последовательность 
    переключения цветов: красный -> желтый -> зеленый -> красный -> желтый ...
        switch_color(self, new_color)
        где:
            new_color -  Новый цвет сфетофора
    """
    def switch_color(self, new_color): # Обьявление функции
        if self.__color_list.count(new_color) == 0: # Если цвет отличаеться от трех заданых
            print(f'Разрешено использовать только цвета: ', self.__color_list)
            exit() # Выходим из программы
        if self.sequence_control: # Если включен режим контроля переключения
            # Если предыдущий цвет красный и новый цвет желтый
            if self.previos_color == self.__color_list[0] and new_color == self.__color_list[1]:
                self.__running(new_color) # Запускаем перекдючение цвета
                self.previos_color = new_color # Устанавливаем предидущий цвет в значение текущего
            # Если предыдущий цвет желтый и новый цвет зеленый
            elif self.previos_color == self.__color_list[1] and new_color == self.__color_list[2]:
                self.__running(new_color) # Запускаем перекдючение цвета
                self.previos_color = new_color # Устанавливаем предидущий цвет в значение текущего
            # Если предыдущий цвет зеленый и новый цвет красный
            elif self.previos_color == self.__color_list[2] and new_color == self.__color_list[0]:
                self.__running(new_color) # Запускаем перекдючение цвета
                self.previos_color = new_color # Устанавливаем предидущий цвет в значение текущего
            else: # Если последовательность переключения не соответствует заданной
                print(f'Вы нарушили режим последовательности переключений светофора!\n'
                      f'Правильный режим переключения {self.__color_list}, {self.__color_list} ...')
                exit() # Выходим из программы
        else: # Если режим контроля выключен
            self.__running(new_color) # Запускаем перекдючение цвета
            self.previos_color = new_color # Устанавливаем предидущий цвет в значение текущего
    """
    Функция вызываевамая при создании обьекта класса. По умолчанию переключает светофор в красный цвет.
        __init__(self)
    """
    def __init__(self):
        self.__running(TrafficLight.__color_list[0]) # Инициализируем и переключаем сфетофор в красный свет

###########################################################################################################
#Основное тело программы
###########################################################################################################

print('Программа использования класса севетофор!')

t_l1 = TrafficLight() # Создаем обьект класса TrafficLight
t_l1.switch_color('желтый') # Переключаем светофор на желтый цвет
t_l1.switch_color('зеленый') # Переключаем светофор на зеленый цвет
t_l1.switch_color('желтый') # Переключаем светофор на желтый цвет
t_l1.switch_color('красный') # Переключаем светофор на красный цвет

print('Изменяем задержки для цветов: красный - 2 сек., желтый - 1сек., зеленый - 2 сек.')
t_l1.red_delay = 2 # Устанавливаем задержку для красного цвета в 2 сек
t_l1.yellow_delay = 1 # Устанавливаем задержку для желтого цвета в 1 сек
t_l1.green_delay = 2 # Устанавливаем задержку для зеленого цвета в 2 сек
print('Включен контроль переключения цветов светофора!')
t_l1.sequence_control = True
t_l1.switch_color('желтый') # Переключаем светофор на желтый цвет
t_l1.switch_color('зеленый') # Переключаем светофор на зеленый цвет

# Переключаем светофор на желтый цвет, но будет выведено предупреждение о нарушении режима переключения и
# программа завершиться
t_l1.switch_color('желтый')



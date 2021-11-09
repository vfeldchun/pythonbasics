#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv # импортируем argv из модуля sys
from math import modf # импортируем функцию modf из модуля math

"""
Функция fte_calc для расчета заработной платы сотрудника в месяц включая премию
    fte_calc(work_hours, emp_rate, emp_perf)
    где:
        work_hours - выроботка в часах за месяц
        emp_rate - ставка в час
        emp_perf - производительность в процентах
"""
def fte_calc(work_hours, emp_rate, emp_perf):
    premium = 0.33 * (emp_perf/100) # Вычисляем процент премии на основе базы в 33% и реальной производительности
    result = float(work_hours * emp_rate) # Вычисляем заработную плату за месяц
    prem_value = float(result * premium) # Вычисляем премию за месяц
    result = result + prem_value # Вычисляем результирующую заработную плату за месяц включая премию
    return result, prem_value # Возвращаем общую заработную плату и премию

print('\nПрограмма расчета заработной платы сотрудников.\n')

try: # Если все параметры переданы скрипту
    script_name, name, emp_workhouгs, emp_rate_payment, emp_performance = argv # присваиваем праметры переменным
except ValueError: # Если параметры переданы не корректно выводим справку и завершаем программу
    print(f'Вы уакзали не все необходимые параметры для запуска скрипта {argv[0]}')
    print('Для работы программы необходимо указать следующие параметры поле имени скрипта:')
    print('\tpython DZ_lesson4-1.py <FIO> <workhours> <payment rate> <performance>')
    print('\t\tгде:')
    print('\t\t <ФИО>: Фамилия')
    print('\t\t <workhours>: выроботка в часах за месяц')
    print('\t\t <payment ratе>: ставка в рублях в час')
    print('\t\t <performance>: производительность сотрудника в % в месяц')
    exit()

# Вызываем функцию рачета общей заработной платы и премии
salary, premium = fte_calc(int(emp_workhouгs), float(emp_rate_payment), int(emp_performance))
sal_kop = modf(salary) # Получаем целую часть и копейки зарплаты
prem_kop = modf(premium) # Получаем целцю часть и копейки премии

#Выводим результаты расчета на экран
print(f'Заработная плата за месяц для сотрудника {name} состовляет:')
print(f'\t\t {int(salary)} рублей и {int(round(sal_kop[0], 2) * 100)} копеек, '
      f'включая премию {int(premium)} рублей и {int(round(prem_kop[0], 2) * 100)} копеек!')


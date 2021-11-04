#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

"""
Функция выводит имя, фамилию, год рождения, город проживания, email, телефон.
    user_data (name, surname, year_birt, city, email, telephone, print_type):
    где аргументы:
        name - Имя
        surname - Фамилия
        year_birt - год рождения
        city - город проживания
        email - адрес электронной почты
        telephone - телефон
        print_type - атрибут типа вывода на экран:
            oneline - вывод данных в одну строку
            multiline - вывод данных в отдельных строках
"""

def user_data(name, surname, year_birt, city, email, telephone, print_type):
    separator = ''
    if print_type == 'oneline': #если однострочный режим
        separator = ', '
    elif print_type == 'multiline': #если многострочный режим
        separator = '\n'

    print(f'ФИО: {name} {surname}{separator}'
          f'Год рождения: {year_birt}{separator}'
          f'Город проживания: {city}{separator}'
          f'e-mail: {email}{separator}'
          f'Телефон: {telephone}')
    pass

# Основное тело программы
# Сбор данных о пользователе и вывод данных на экран как в однострочном так и в многосстрочном режиме
new_name = input('Ведите имя: ')
new_surname = input('Ведите фамилию: ')
new_year_birth = input('Ведите год рождения: ')
new_city = input('Ведите город проживания: ')
new_email = input('Ведите e-mail: ')
new_telephone = input('Ведите телефон: ')

print('\nВывод данных пользователя в одну строку:')
user_data(name=new_name, surname=new_surname,
          year_birt=new_year_birth,
          email=new_email,
          city=new_city,
          telephone=new_telephone,
          print_type='oneline') # Односторочный режим

print('\nВывод данных пользователя в отдельных строках:')
user_data(surname=new_surname, name=new_name,
          year_birt=new_year_birth,
          city=new_city,
          email=new_email,
          telephone=new_telephone,
          print_type='multiline') # Многострочный режим


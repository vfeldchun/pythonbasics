#Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#Результат: [23, 1, 3, 10, 4, 11]

input_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11] #Задаем список для последующей обработки

print(f'Список цифр: {input_list}') #Выводим список на экран

# Для создание нового списка используем генератор с условием
# что записываеться только те элементы которые встречаються в списке 1 раз
output_list = [item for item in input_list if input_list.count(item) == 1]

print('Список элементов не имеющих повторений\n', output_list) # Выводим результат на экран
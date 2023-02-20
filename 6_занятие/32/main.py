"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
"""


minimum = int(input('Введите минимум: '))
maximum = int(input('Введите максимум: '))
n = int(input('Введите длинну массива: '))
array = []
result = []

for i in range(0, n - 1):
	array.append(int(input('Введите число: ')))

print('Исходный массив - ', array)

for index, value in enumerate(array):
	if value >= minimum and value <= maximum: 
		result.append(index)


print('Результат - ', result)

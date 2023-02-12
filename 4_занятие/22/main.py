"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

from array import *

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))

resultList = list()

for i in range(0, n):
	value = int(input('Введите число в первое множество: '))
	if not (value in resultList):
		resultList.append(value)

for i in range(0, m):
	value = int(input('Введите число во второе множество: '))
	if not (value in resultList):
		resultList.append(value)

resultList.sort()
result = ''
for value in resultList:
	result += str(value) + ' '

print(result)

"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
"""
from array import *
n = int(input('Введите количество элементов сюд: '))
# Создание массива
a = array('i')
for i in range(1, n):
	a.append(int(input('Введите ещё число: ')))
x = int(input('Введите число сюд: '))
j=a[0];
for i in a:
	if (abs(j-x)>abs(i-x)):
		j=i
print(j)
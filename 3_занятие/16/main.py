"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""

from array import *
n = int(input('Введите количество элементов сюд: '))
# Создание массива
a=array('i')
for i in range(1,n):
	a.append(int(input('Введите ещё число: ')))
x = int(input('Введите число сюд: '))
j=0
for i in a:
	if (i==x):
		j=j+1
print(j)
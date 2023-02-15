"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""


def sumAB(a, b):
	if b > 0:
		return sumAB(a + 1, b - 1)
	else:
		return a

valueA = int(input('Введите число А: '))
valueB = int(input('Введите число B: '))
if valueA > valueB:
	print('А + B = ', sumAB(valueA, valueB))
else:
	print('А + B = ', sumAB(valueB, valueA))

"""
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
"""

def powAB(a, b):
	if b > 0:
		return a * powAB(a, b - 1)
	else:
		return 1 


valueA = int(input('Введите число А: '))
valueB = int(input('Введите число B: '))

print('А в степени B = ', powAB(valueA, valueB))

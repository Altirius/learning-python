"""
Задача 2: - HARD необязательная, идет за 3 обязательных 
Найдите сумму цифр любого вещественного или целого числа. 
Можно использовать decimal. Через строку решать нельзя.
"""

number = float(input('Введите число: '))
while (number % 1 > 0):
    number = number*10
    sum = 0
while (number > 9):
    sum = sum+(number % 10)
    number = number//10
sum = int(sum+number)
print(sum)

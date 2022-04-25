'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).
'''

print("Вариант 1")
i = 0
totalten = 1
while i < 10:
    i +=1
    totalten = i * totalten
print(totalten) #3628800

print("Вариант 2")
totalten = 1
for i in range(1, 11):
    totalten *= i
    i +=1
print(totalten) #3628800

print("Вариант 3")
import math
n = math.factorial(10)
print(n) #3628800
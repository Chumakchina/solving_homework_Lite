'''
(!!!Подсказка на следующие 5 задач - превратите число в строку, а потом работайте с строкой)
Задача 6
Найти сумму цифр числа.
    Пример:
    254314
    Сумма цифр числа - 19(2+5+4+3+1+4)
'''


n = 254314
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print(sum)
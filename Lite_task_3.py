'''
Задача 3
Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

print("Вариант 1")
i = 0
totalhundred = 0
while i <= 100:
    totalhundred = i + totalhundred
    i +=1
print(totalhundred)

print("Вариант 2")
totalhundred = 0
for i in range(1, 101):
    totalhundred +=i
print(totalhundred)
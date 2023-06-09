"""Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
"""
from random import randrange

N = int(input("Enter N = "))
max1 = 0
max = 0
for i in range(N):
    a = randrange(-50, 50)
    print(a, end=" ")
    if a > 0:
        max1 += 1
    else:
        if max1 > max:
            max = max1
        max1 = 0
print(f"Максимальное количество дней в оттепели - {max}")

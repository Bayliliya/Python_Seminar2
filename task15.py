"""Найти вес самого легкого и самого тяжелого арбуза
"""
from random import randrange
N = int (input ( "Введите количество арбузов = "))
max = float('-inf')
min = float ('inf')
for i in range(N):
    a = randrange(0,20)
    print(a, end =" ")
    if a > max:
        max = a
    elif a < min:
        min = a
print (f"максимальный вес - {max}, Минимальный вес - {min}")        
#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = float(input("Введите положительное число N: "))
i = 0
while 2**i <= N:
    print(2**i, end =" ")
    i += 1
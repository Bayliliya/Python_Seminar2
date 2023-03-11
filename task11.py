"""Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A.
 Если А не является числом Фибоначчи, выведите число -1.
"""

A = int(input("A= "))
a1 = 0
a2 = 1
sum = 1
count = 2
while sum < A:
    sum = a1+a2
    a1 = a2
    a2 = sum
    count += 1
if sum == A:
    print (count)
else:
    print (-1)       
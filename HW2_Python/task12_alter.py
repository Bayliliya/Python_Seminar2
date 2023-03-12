x = int(input("Enter x: "))
y = int(input("Enter y: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)
            
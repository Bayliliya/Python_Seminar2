# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#  Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input("Введите сумму загаданных чисел: "))
P = int(input("Введите произведение загаданных чисел: "))
D = S**2-4*P
if D == 0:
    a = S/2
    b = S - a
elif D > 0:
    a1 = (S - D**(1/2))/2
    a2 = (S + D**(1/2))/2
    if a1 > 0:
        a = a1
    else:
        a = a2
    b = S - a    
else:
    print("По введенным значениям нет решений")
if (a - int(a)) != 0:
    print("Решений с натуральными числами нет")
else: 
    print (f"Первое число: {int(a)}, второе: {int(b)}")         



first = input('Введите число: first ')
second = input('Введите число: second ')
third = input('Введите число: third ')

if  first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second and first != third and second != third:
    print(0)
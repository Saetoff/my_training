first = int(input("Первое число:"))
second = int(input("Второе число:"))
third = int(input("Третье число:"))

if first == second == third:
    print(3, "одинаковых числа")
elif first == second or first == third or second == third:
    print(2, "одинаковых числа")
else:
    print(0, "одинаковых чисел")


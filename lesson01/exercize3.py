user_number = int(input("Введите любое число>>>"))
a = user_number
b = int("{}{}".format(a, a))
c = int("{}{}".format(a, b))
sum = a + b + c
print(sum)

# Вариант №1
def my_func(x, y):
    return x ** y
print(my_func(10, -2))

# Вариант №2
def power(a, n):
    if a == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return a
    elif n < 0:
        return 1 / (a * power(a, -n - 1))
    else:
        return a * power(a, n - 1)


a = float(input("Введите положительное число:"))
n = int(input("Введите отрицательное число:"))
print(power(a, n))

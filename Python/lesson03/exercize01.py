try:
    def dif_1():
        value_1 = int(input("Введите значение 1: "))
        value_2 = int(input("Введите значение 2: "))
        dif_2 = value_1 / value_2
        return dif_2
    dif = dif_1()
    print("Разность чисел:", dif)


except ZeroDivisionError:
    print("Делить на ноль нельзя, введите другое число")
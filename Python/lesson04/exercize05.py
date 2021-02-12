# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
from functools import reduce
my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(my_list)
def product_of_numbers(one_x, x):
    return one_x * x
print(reduce(product_of_numbers, my_list))


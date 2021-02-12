# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
my_list = [4, 94, 64, 22, 5, 78, 93, 73]
print(my_list)
new_list = [x for x in my_list if x > my_list[my_list.index(x) - 1]]
print(new_list)


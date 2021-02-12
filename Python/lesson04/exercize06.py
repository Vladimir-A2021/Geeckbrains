# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
from itertools import count
for x in count(3, 1):
    if x > 10:
        break
    print(x)

# итератор, повторяющий элементы некоторого списка, определённого заранее
from itertools import cycle
my_list = [2, 7, 23, 1]
iter = cycle(my_list)
i = 0
iteration = 3
while i < iteration:
        print(next(iter))
        i+=1
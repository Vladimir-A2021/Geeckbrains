# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
import sys
from lesson04 import exercize01_1

try:
    time, rate, bonus = sys.argv

except ValueError:
    print("Not a number")
    exit()

print(exercize01_1.salary())


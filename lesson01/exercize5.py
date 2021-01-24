proceeds = int(input("Введите значение выручки фирмы>>>"))
costs = int(input("Введите значение издержек фирмы>>>"))

profit = int(proceeds - costs)
profitability = int(profit / proceeds * 100)
if proceeds > costs:
    print(f"Фирма работает с прибылью. Рентабильность - {profitability}")
    staff = int(input("Введите количество сотрудников фирмы>>>"))
    proceeds_staff = proceeds / staff
    print(f"Прибыль фирмы в расчёте на одного сотрудника - + {proceeds_staff}")
else:
    print("Фирма работает с убытком")


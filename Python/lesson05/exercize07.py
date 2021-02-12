# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

import json
dictionary = {}
profit_average = {}
counter = 0
prof_average = 0
i = 0
with open("list_firm", "r", encoding="utf-8") as my_file:
    for line in my_file:
        name, view, proceeds, costs = line.split()
        dictionary[name] = int(proceeds) - int(costs)
        if dictionary.setdefault(name) >= 0:
            counter = counter + dictionary.setdefault(name)
            i += 1

    profit_average = {"average_profit": round(prof_average)}
    dictionary.update(profit_average)
    print(f"{dictionary}")

with open("file.json", "w") as write_js:
    json.dump(dictionary, write_js)


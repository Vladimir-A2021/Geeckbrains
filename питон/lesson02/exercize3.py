# C использованием list
# a = int(input("Введите число от 1 до 12>>>"))
# list = ["зима", "весна", "лето", "осень"]
# if a <= 2 or a == 12:
# print(list[0])

# if 2 < a <= 5:
#   print(list[1])

# if 5 < a <= 8:
#    print(list[2])

# if 9 < a <= 11:
# print(list[3])

# С использованием dict
a = int(input("Введите число от 1 до 12>>>"))
my_dict = {"time": ["зима", "весна", "лето", "осень"]}
if a <= 2 or a == 12:
    print(my_dict["time"][0])
if 2 < a <= 5:
    print(my_dict["time"][1])
if 5 < a <= 8:
    print(my_dict["time"][2])
if 9 < a <= 11:
    print(my_dict["time"][3])

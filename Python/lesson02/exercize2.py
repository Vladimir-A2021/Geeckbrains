a = input("Введите несколько цифр>>>")
print(list(a))
l = [int(x) for x in a]

for i in range(0, len(l), 2):
    l[i], l[i + 1] = l[i + 1], l[i]
print(l)


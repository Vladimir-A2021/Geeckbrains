a = input("Введите несколько слов через пробел>>>").split(" ")
length = len(a)
counter = 0
while counter < length:
    index = counter + 1
    print(f"{index}  {a[counter][:10]}")
    counter += 1


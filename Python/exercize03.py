# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Решите задание в одну строку.
print(f"{[x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0]}")


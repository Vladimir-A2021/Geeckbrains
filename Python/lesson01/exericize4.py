user_num = int(input("Введите любое положительное число, не менее 2-х цифр>>>"))
max = user_num%10
user_num = user_num//10
while user_num > 0:
    if user_num%10 > max:
        max = user_num%10
    user_num = user_num//10
print(max)


# Напишите программу, открывающую файл на чтение
# и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open("numbers.txt", "r+", encoding="utf-8") as my_file:
      for i in my_file:
        i = i.split(" ", 1)
        new_file.append(dict[i[0]] + "  " + i[1])


with open("numbers_1.txt", "w", encoding="utf-8") as my_file_1:
    my_file_1.writelines(new_file)

with open("numbers_1.txt", "r", encoding="utf-8") as my_file_1:
    for line in my_file_1:
        print(line)



# translater = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
# my_list = []
# result = []
# try:
#     file_obj = open("numbers.txt", 'r')
#     for line in file_obj:
#         tokens = line.split(" - ")
#         print(tokens)
#         if tokens[0] in translater:
#             word = translater[tokens[0]]
#             result.append(word +' - '+ tokens[1])
#     print(result)
#
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     file_obj.close()
# #
# # try:
# #     file_input = open("numbers_1.txt", "w")
# #     file_input.writelines(result)
# # except IOError:
# #     print("Произошла ошибка ввода-вывода!")
# # finally:
# #     file_input.close()
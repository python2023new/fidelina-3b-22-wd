# Напишите программу, которая запрашивает у пользователя число и проверяет, есть ли
# это число в массиве. Если число есть в массиве, программа выводит сообщение "Число
# найдено в массиве", иначе - "Число не найдено в массиве".

import random
arr_list=[]
for i in range(50):
    arr_list.append(random.randint(1,10))
print(arr_list)
print('Какое число найти?')
if (arr_list.count(int(input())) == 0):
    print("Число не найдено в массиве")
else:
    print("Число найдено в массиве")
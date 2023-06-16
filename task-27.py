# Создайте список чисел. Используя цикл `for`, выведите на экран только четные числа
# из этого списка.

import random


arr_list=[]

for i in range(10):
    arr_list.append(random.randint(1,100))
print(arr_list)
print("Четные числа массива: ")

for i in range(10):
    if (arr_list[i]%2==0):
        print(arr_list[i])
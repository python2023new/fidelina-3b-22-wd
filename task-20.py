# Напишите программу, которая создает массив размера 10 и заполняет его случайными
# числами от 1 до 100. Затем программа выводит максимальное и минимальное число в
# массиве.

import random

arr_list=[]
for i in range(10):
    arr_list.append(random.randint(1,100))
print(arr_list)
arr_list.sort()
print('Наименьшее - ', arr_list[0], ", наибольшее - ", arr_list[9])
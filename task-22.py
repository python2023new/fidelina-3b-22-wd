# Напишите программу, которая находит сумму всех элементов в массиве и выводит ее на
# экран. Массив заполняется случайными числами от 1 до 10.


import random

arr_list=[]
summ=0
for i in range(7):
    arr_list.append(random.randint(1,10))
    summ+=arr_list[i]
print(arr_list)
print(summ)
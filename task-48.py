# Дан массив: 5, 7, 11, 13, 15, 20, 25. Найти среднее арифметическое элементов
# массива, которые больше 10

from statistics import mean

arr_list = [5, 7, 11, 13, 15, 20, 25]
arr_list_mid = []

for i in range(len(arr_list)):
    if arr_list[i] > 10:
        arr_list_mid.append(arr_list[i])

sum = mean(arr_list_mid)
print("Среднее арифметическое элементов массива, больше 10: "+str(sum))
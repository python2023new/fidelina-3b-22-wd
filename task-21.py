# Напишите программу, которая создает массив, который состоит из двух других
# массивов, объединенных в один. Например, если массив 1 содержит `[1, 2, 3]`, а массив
# 2 содержит `[4, 5, 6]`, то новый массив должен содержать `[1, 2, 3, 4, 5, 6]`.


arr_first = [7,2,3]
arr_second = [4,9,6]
arr_first.extend(arr_second)
print(arr_first)
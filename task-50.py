# Дан массив: 1, 2, 3, 4, 5. Удалить заданный элемент из массива - 3.

arr_list = [1, 2, 3, 4, 5]
arr_list.remove(3)

print("Массив: " + ' '.join(str(el) for el in arr_list))
# Даны массивы: 24, 36, 48, 60; 12, 18, 24, 36, 72. Найти наибольший общий делитель
# двух массивов чисел.

from math import gcd
from functools import reduce


arr_list1 = [24, 36, 48, 60]
arr_list2 = [12, 18, 24, 36, 72]

arr_list1.extend(arr_list2)
result = reduce(gcd, arr_list1)

print("наибольший общий делитель двух массивов чисел: " + str(result));
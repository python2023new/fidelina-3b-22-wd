# Дан список кортежей с координатами точек (1, 2), (3, 4), (-1, 5), (6, -3).
# Отсортировать его по расстоянию от начала координат.

import math

myList = [(1, 2), (3, 4), (-1, 5), (6, -3)]

def sortByLength(element):
    return math.dist(element, (0,0))

sortedList = sorted(myList, key=sortByLength)

print ("Отсортировано по расстоянию от начала координат: ", sortedList)
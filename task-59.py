# Дан список строк "apple", "orange", "banana", "pineapple", "grape". Отсортировать
# его в порядке убывания длины строк.

newList = ["apple", "orange", "banana", "pineapple", "grape"]

newList = sorted(newList, key=len)
newList.reverse()

print("Отсортированный список: ",  newList)
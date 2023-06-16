# Напишите программу, которая открывает файл "text.txt" и выводит его содержимое на
# экран.

file = open('text.txt', 'r')
print(file.read())
file.close()
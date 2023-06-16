# Напишите программу, которая создает новый файл "new_file.txt" и записывает туда
# сообщение "Hello, world!".


file = open('new_text.txt', 'w')
file.write('Hello, world!')
file.close()
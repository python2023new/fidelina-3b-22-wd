# Напишите программу, которая принимает на вход имя файла и выводит на экран самое
# часто встречающееся слово в файле. Если файл не найден, программа должна вызывать
# исключение.

import os.path
from sys import argv

fileName = 'new_text.txt'
if not os.path.isfile(fileName):
    raise ValueError("Файл отсутствует")

newFile = open(fileName,'r')
text=newFile.read()
newFile.close()

notWords = [ '"', "'", '(', ')', '?', '_', '`', '=', '.', ':', ',', '!', '-', '—', '[', ']']
list = []
for word in text.lower().split():
    if not word in notWords:
        locWord = word

        if word[-1] in notWords:
            locWord = locWord[:-1]
        if word[0] in notWords:
            locWord = locWord[1:]
        list.append(locWord)

locDict = dict()
for word in list:
    locDict[word] = locDict.get(word, 0) + 1

locList = []
for key, value in locDict.items():
    locList.append((value, key))
    locList.sort(reverse=True)

print("самое часто встречающееся слово в файле: " + locList[0][1])

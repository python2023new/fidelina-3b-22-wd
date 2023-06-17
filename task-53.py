# Создать класс "Список домашних дел" с методами "добавить элемент", "удалить
# элемент" и "вывести на экран". При каждом добавлении элемента в список сохранять
# его в файл и при инициализации класса загружать сохраненный список из файла.

import os.path


class ToDoList(object):

    def __init__(self):
        self.list = []

        if os.path.isfile('out.txt'):
            with open('out.txt') as f:
                self.list = list(f)
        else:
            NewFile = open('out.txt', 'w')
            NewFile.close()
        pass

    def addElement(self, element):
        self.list.append(element)
        self.save()
        pass

    def removeElement(self, element):
        self.list.remove(element)
        self.save()
        pass

    def save(self):
        NewFile = open('out.txt', 'w')

        for element in self.list:
            NewFile.write(element)
            NewFile.write('\n')
        NewFile.close()
        pass

    def display(self):
        print(' '.join(str(el) for el in self.list))
        pass


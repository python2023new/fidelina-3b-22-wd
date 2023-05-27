# Создайте класс Dog, описывающий собаку со свойствами "имя", "порода", "возраст" и методом печати этой информации.

class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def about_dog(self):
        print("Вашему вниманию представлена собака по кличке {}, ее порода - {} и возраст - {}".format(self.name, self.breed, self.age))

dog_name = str(input('Введите кличку собаки: '))
dog_age = str(input('Введите возраст: '))
dog_breed = str(input('Введите породу: '))

my_dog = Dog(dog_name, dog_age, dog_breed)
my_dog.about_dog()
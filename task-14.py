# Создайте класс студент, который имеет свойства: имя, фамилию, возраст и специальность.
# Создайте метод, который водит информацию о студенте в формате: имя - фамилия, возраст лет, специальность.


class Student:

    def __init__(self, name, surname, age, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.profession = profession

    def student_info(self):
        print(f"{self.name} - {self.surname}, {self.age} лет, {self.profession}")


my_student = Student("Иван", "Котов", "25", "программист")
my_student.student_info()

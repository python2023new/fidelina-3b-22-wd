# Создайте класс студент, описывающий студента по параметрам "имя", "фамилия", "курс" и оценками по каждому предмету и методом расчета среднего балла

class Student:

    def __init__(self, name, surname, cours, grades):
        self.name = name
        self.surname = surname
        self.cours = cours
        self.grades = grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Александр", "Иванов", 1, [5, 4, 3, 4, 5])
print(f"{student.name} {student.surname}, {student.cours} курс, средний бал - {student.average_grade()}")

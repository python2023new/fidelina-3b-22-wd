# Создайте класс Книга, у которой есть свойства: "название", "автор", "жанр", "год издания";
# создайте метод который выводит информацию о книге в формате: "название, автор (год издания), жанр"

class Book:

    def __init__(self, name, author, yearOfRelease, genre):
        self.name = name
        self.author = author
        self.yearOfRelease = yearOfRelease
        self.genre = genre

    def book_info(self):
        print(f"{self.name}, {self.author} ({self.yearOfRelease}), {self.genre}")

my_book = Book("Война и мир", "Л.Н. Толстой", 1865,  "роман-эпопея")
my_book.book_info()

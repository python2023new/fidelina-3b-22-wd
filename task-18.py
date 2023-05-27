# Создайте класс "геометрическая фигура", у которого есть свойства площать и периметр.
# Создайте метод, который выводит информацию о фигуре в формате: "Площадь - Площадь, периметр - Периметр"

class GeometricFigure:
    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter


    def figure_info(self):
        print(f"площадь - {self.square}, периметр - {self.perimeter}")

my_fig = GeometricFigure(10, 20)

my_fig.figure_info()
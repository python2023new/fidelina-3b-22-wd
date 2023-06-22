# Создать класс "Робот" с атрибутами "имя", "скорость" и методом "движение", который
# выводит на экран, какой путь прошел робот за указанное время с учетом его скорости.
# Создать двух наследников класса "Робот": "Гусеничный робот" с атрибутом
# "территория" и "Робот на колесах" с атрибутом "марка автомобиля".


class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def movement(self, time):
        distance = self.speed * time
        print(f"{self.name} moved {distance} meters in {time} seconds.")


class TrackedRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory


class WheeledRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand



r1 = Robot("Robot 1", 5)
r1.movement(10)  # Output: Robot 1 moved 50 meters in 10 seconds.

r2 = TrackedRobot("Tracked Robot 1", 2, "Forest")
r2.movement(20)  # Output: Tracked Robot 1 moved 40 meters in 20 seconds.

r3 = WheeledRobot("Wheeled Robot 1", 10, "Tesla")
r3.movement(5)  # Output: Wheeled Robot 1 moved 50 meters in 5 seconds.
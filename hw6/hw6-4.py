message = "4. Реализуйте базовый класс Car.\n" \
        "у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).\n" \
        "А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);\n" \
        "опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;\n" \
        "добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;\n" \
        "для классов TownCar и WorkCar переопределите метод show_speed.\n" \
        "При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.\n" \
        "Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.\n" \
        "Вызовите методы и покажите результат.\n"
print(message)

class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, speed, color, name, is_police = False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Автомобиль {self.name} едет."

    def stop(self):
        return f"Автомобиль {self.name} остановлен."

    def turn(self, direction):
        return f"Автомобиль изменил направления: {direction}"

    def show_speed(self):
        return f"Текущая скорость автомобилья {self.name} составляет {self.speed} км/ч."


class TownCar(Car):
    __max_speed = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > self.__max_speed:
            print(f"Текущая скорость автомобилья {self.name} превышена.")
        return f"Текущая скорость автомобилья {self.name} составляет {self.speed} км/ч."


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    __max_speed = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > self.__max_speed:
            print(f"Текущая скорость автомобилья {self.name} превышена.")
        return f"Текущая скорость автомобилья {self.name} составляет {self.speed} км/ч."


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

car1 = TownCar(100, 'green', 'CarName1')
print(car1.go())
print(car1.turn('TownName1'))
print(car1.show_speed())
print(car1.stop())
print()

car2 = SportCar(20, 'yellow', 'CarName2')
print(car2.go())
print(car2.turn('TownName1'))
print(car2.show_speed())
print(car2.stop())
print()

car3 = WorkCar(70, 'white', 'CarName3')
print(car3.go())
print(car3.turn('TownName1'))
print(car3.show_speed())
print(car3.stop())
print()

car4 = PoliceCar(40, 'red', 'CarName4')
print(car4.go())
print(car4.turn('TownName1'))
print(car4.show_speed())
print(car4.stop())
print()

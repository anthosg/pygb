message = "2. Реализовать класс Road (дорога).\n" \
        "определить атрибуты: length (длина), width (ширина);\n" \
        "значения атрибутов должны передаваться при создании экземпляра класса;\n" \
        "атрибуты сделать защищёнными;\n" \
        "определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;\n" \
        "использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;\n" \
        "проверить работу метода.\n" \
        "Например: 20 м*5000 м*25 кг*5 см = 12500 т.\n"
print(message)

class Road:
    _length = None
    _width = None
    mass = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f"Длина асфальта: {self._length} м")
        print(f"Ширина асфальта: {self._width} м")

    def calculate(self):
        return (self._width * self._length * self.mass * self.thickness) / 1000

road = Road(5000, 20)
print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна: {road.calculate()} т")
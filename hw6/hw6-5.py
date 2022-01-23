message = "5. Реализовать класс Stationery (канцелярская принадлежность).\n" \
        "определить в нём атрибут title (название) и метод draw (отрисовка).\n" \
        "Метод выводит сообщение «Запуск отрисовки»;\n" \
        "создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);\n" \
        "в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;\n" \
        "создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.\n"
print(message)

class Stationery:
    title = None

    def __init__(self, title = None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f"Ручка великое изобретение. Сегодня наш инструмент: {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Карандаш великое изобретение. Сегодня наш инструмент: {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Маркер великое изобретение. Сегодня наш инструмент: {self.title}")

stationery = Stationery()
pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()

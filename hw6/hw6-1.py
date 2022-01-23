message = "1. Создать класс TrafficLight (светофор).\n" \
        "определить у него один атрибут color (цвет) и метод running (запуск);\n" \
        "атрибут реализовать как приватный;\n" \
        "в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;\n" \
        "продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;\n" \
        "переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);\n" \
        "проверить работу примера, создав экземпляр и вызвав описанный метод.\n"
print(message)

from time import sleep
from datetime import datetime

class TrafficLight:
    __color = None
    __steps = {
        'red': 7,
        'yellow': 2,
        'green': 5,
    }

    def running(self):
        for color, time_limit in self.__steps.items():
            self.__color = color
            print(f"{datetime.now()} - Цвет светофора: {self.__color}")
            sleep(time_limit)
            print(f"{datetime.now()} - Переключаем цвет светофора")

traffic = TrafficLight()
traffic.running()

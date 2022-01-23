message = "2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.\n" \
        "Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.\n" \
        "К типам одежды в этом проекте относятся пальто и костюм.\n" \
        "У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).\n" \
        "Это могут быть обычные числа: V и H, соответственно.\n" \
        "Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).\n" \
        "Проверить работу этих методов на реальных данных.\n" \
        "Реализовать общий подсчет расхода ткани.\n" \
        "Проверить на практике полученные на этом уроке знания:\n" \
        "реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.\n"
print(message)

from abc import ABC, abstractmethod

class Dress(ABC):
    parameter = None

    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def calculate(self):
        pass

class Coat(Dress):
    @property
    def calculate(self):
        return f"Расход ткани для пошива пальто: {round(self.parameter / 6.5 + 0.5, 2)}"

class Suit(Dress):
    @property
    def calculate(self):
        return f"Расход ткани для пошива костюма: {round(2 * self.parameter + 0.3, 2)}"

coat = Coat(50)
print(coat.calculate)

suit = Suit(50)
print(suit.calculate)

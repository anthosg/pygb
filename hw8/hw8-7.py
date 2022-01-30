message = "7. Реализовать проект «Операции с комплексными числами».\n" \
        "Создайте класс «Комплексное число».\n" \
        "Реализуйте перегрузку методов сложения и умножения комплексных чисел.\n" \
        "Проверьте работу проекта.\n" \
        "Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.\n" \
        "Проверьте корректность полученного результата.\n"
print(message)

class ComplexNumber:
    number1 = None
    number2 = None

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __add__(self, other):
        return ComplexNumber(self.number1 + other.number1, self.number2 + other.number2)

    def __mul__(self, other):
        number1 = self.number1 * other.number1 - self.number2 * other.number2
        number2 = self.number2 * other.number1 + self.number1 * other.number2
        return ComplexNumber(number1, number2)

    def __str__(self):
        return f"{self.number1}+{self.number2}j"


number1 = ComplexNumber(2, -1)
number2 = ComplexNumber(5, 3)

print(number1 + number2)
print(number1 * number2)

print(complex(2, -1) + complex(5,3))
print(complex(2, -1) * complex(5,3))

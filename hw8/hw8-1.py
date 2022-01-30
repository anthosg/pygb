message = "1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».\n" \
            "В рамках класса реализовать два метода.\n" \
            "Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».\n" \
            "Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).\n" \
            "Проверить работу полученной структуры на реальных данных.\n"
print(message)

class Date:
    date_string = None

    def __init__(self, date_string):
        self.date_string = str(date_string)

    @classmethod
    def parse(cls, date_string):
        try:
            day, month, year = map(int, date_string.split('-'))
        except ValueError as e:
            return f"Неправильный формат."
        return day, month, year

    @staticmethod
    def is_valid(date_string):
        try:
            day, month, year = map(int, date_string.split('-'))
        except ValueError as e:
            return "Неправильный формат."

        if 1 > day > 31:
            return "Неправильный формат дня."
        if 1 > month > 12:
            return "Неправильный формат месяца."
        if len(str(year)) != 4:
            return "Неправильный формат года."

        return True

date_string = "30-01-2022"
print(Date.parse(date_string))
print(Date.is_valid(date_string))

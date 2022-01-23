message = "3. Реализовать базовый класс Worker (работник).\n" \
        "определить атрибуты: name, surname, position (должность), income (доход);\n" \
        "последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {\"wage\": wage, \"bonus\": bonus};\n" \
        "создать класс Position (должность) на базе класса Worker;\n" \
        "в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);\n" \
        "проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.\n"
print(message)

class Worker:
    name = None
    surname = None
    position = None
    _income = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return ' '.join([self.surname, self.name])

    def get_total_income(self):
        return sum(self._income.values())

position = Position('Ivan', 'Ivanov', 'head', 1000, 5000)

print(f"Имя: {position.name}")
print(f"Фамилия: {position.surname}")
print(f"Должность: {position.position}")
print(f"Доход: {position._income}")
print()

print(f"Полное имя сотрудника: {position.get_full_name()}")
print(f"Доход с учетом премии: {position.get_total_income()}")

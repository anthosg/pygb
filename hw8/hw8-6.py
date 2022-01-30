message = "6. Продолжить работу над вторым заданием.\n" \
        "Реализуйте механизм валидации вводимых пользователем данных.\n" \
        "Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.\n" \
        "Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.\n"
print(message)

class Warehouse:
    items = {}

    @classmethod
    def add(self, name, count = 1):
        if name in self.items:
            self.items[name] = self.items[name] + count
        else:
            self.items[name] = count
        return f"Техника с наименованием {name} принята в склад. В складе {self.items[name]} шт."

while True:
    name = input(f"Введите производителя:")
    if len(name) == 0 or name == "stop":
        break
    count = int(input(f"Введите количество:"))
    print(Warehouse.add(name, count))

print("\n==========")
print("Техника на складе:", Warehouse.items)

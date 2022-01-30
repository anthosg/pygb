message = "5. Продолжить работу над первым заданием.\n" \
        "Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.\n" \
        "Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).\n"
print(message)

class Warehouse:
    items = {}

    def add(self, name, count = 1):
        if name in self.items:
            self.items[name] = self.items[name] + count
        else:
            self.items[name] = count
        return f"Техника с наименованием {name} принята в склад. В складе {self.items[name]} шт."

    def move(self, department, name, count = 1):
        if name not in self.items:
            return f"В складе нет техники с наименованием {name}"
        if self.items[name] <= count:
            removed = self.items[name]
            del self.items[name]
        else:
            self.items[name] = self.items[name] - count
            removed = self.items[name]
        return f"Техника с наименованием {name} передана в отдел {department} в количестве {removed} шт."

    def __str__(self):
        return f"Список товаров в складе: {self.items}"

warehouse = Warehouse()

print(warehouse.add("HP", 1))
print(warehouse.add("Canon", 1))
print(warehouse.move("IT Department", "HP", 2))
print(warehouse.move("Director", "Epson", 1))
print()

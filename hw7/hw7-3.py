message = "3. Реализовать программу работы с органическими клетками, состоящими из ячеек.\n" \
        "Необходимо создать класс Клетка.\n" \
        "В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).\n" \
        "В классе должны быть реализованы методы перегрузки арифметических операторов:\n" \
        "сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).\n" \
        "Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.\n" \
        "Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.\n" \
        "Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.\n" \
        "Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.\n" \
        "Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.\n" \
        "В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.\n" \
        "Данный метод позволяет организовать ячейки по рядам.\n" \
        "Метод должен возвращать строку вида *****\\n*****\\n*****..., где количество ячеек между \n равно переданному аргументу.\n" \
        "Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.\n" \
        "Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.\n" \
        "Тогда метод make_order() вернёт строку: *****\\n*****\\n**.\n" \
        "Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.\n" \
        "Тогда метод make_order() вернёт строку: *****\\n*****\\n*****.\n" \
        "Подсказка: подробный список операторов для перегрузки доступен по ссылке.\n"
print(message)

class Cell:
    count = 0

    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        sub = self.count - other.count
        if sub <= 0:
            return f'Разность количества ячеек двух клеток должна быть больше нуля.'
        return sub

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, row):
        result = self.count // row
        last = self.count % row
        return "\n".join(["*" * row] * result + (["*" * last] if last else []))

cell1 = Cell(15)
cell2 = Cell(12)

print(f"{cell1.count} + {cell2.count} = {cell1 + cell2}")
print(f"{cell1.count} - {cell2.count} = {cell1 - cell2}")
print(f"{cell1.count} / {cell2.count} = {cell1 / cell2}")
print(f"{cell1.count} * {cell2.count} = {cell1 * cell2}")
print()
print(cell1.make_order(5))
print()
print(cell2.make_order(5))
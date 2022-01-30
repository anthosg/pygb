message = "4. Начните работу над проектом «Склад оргтехники».\n" \
        "Создайте класс, описывающий склад.\n" \
        "А также класс «Оргтехника», который будет базовым для классов-наследников.\n" \
        "Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).\n" \
        "В базовом классе определите параметры, общие для приведённых типов.\n" \
        "В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.\n"
print(message)

class Warehouse:
    def __init__(self):
        print("Склад оргтехники")

class OfficeEquipment:
    manufacturer = None
    price = None
    inventory_number = None

    def __init__(self, manufacturer, price, inventory_number):
        self.manufacturer = manufacturer
        self.price = price
        self.inventory_number = inventory_number

class Printer(OfficeEquipment):
    cartridge = None

    def __init__(self, manufacturer, price, inventory_number, cartridge):
        super().__init__(manufacturer, price, inventory_number)
        self.cartridge = cartridge

    def __str__(self):
        return f"Производитель: {self.manufacturer}\nЦена: {self.price}\nИнвентарный номер: {self.inventory_number}\nКартридж: {self.cartridge}"

class Scanner(OfficeEquipment):
    sensor_type = None

    def __init__(self, manufacturer, price, inventory_number, sensor_type):
        super().__init__(manufacturer, price, inventory_number)
        self.sensor_type = sensor_type

    def __str__(self):
        return f"Производитель: {self.manufacturer}\nЦена: {self.price}\nИнвентарный номер: {self.inventory_number}\nТип сенсора: {self.sensor_type}"

class PhotocopyMachine(OfficeEquipment):
    is_double_sided = False

    def __init__(self, manufacturer, price, inventory_number, is_double_sided):
        super().__init__(manufacturer, price, inventory_number)
        self.is_double_sided = is_double_sided

    def __str__(self):
        return f"Производитель: {self.manufacturer}\nЦена: {self.price}\nИнвентарный номер: {self.inventory_number}\nДвухсторонная распечатка: {self.is_double_sided}"

printer = Printer("HP", 1000, 111111, "CP222")
print(printer)
print()

scanner = Scanner("Canon", 2000, 222222, "Tablet")
print(scanner)
print()

photocopy = PhotocopyMachine("Epson", 3000, 333333, True)
print(photocopy)
print()

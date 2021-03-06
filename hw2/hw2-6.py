message = "6. *Реализовать структуру данных «Товары».\n" \
        "Она должна представлять собой список кортежей.\n" \
        "Каждый кортеж хранит информацию об отдельном товаре.\n" \
        "В кортеже должно быть два элемента — номер товара и словарь с параметрами\n" \
        "(характеристиками товара: название, цена, количество, единица измерения).\n" \
        "Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.\n\n" \
        "Пример готовой структуры:\n" \
        "[\n" \
        "    (1, {\"название\": \"компьютер\", \"цена\": 20000, \"количество\": 5, \"eд\": \"шт.\"}),\n" \
        "    (2, {\"название\": \"принтер\", \"цена\": 6000, \"количество\": 2, \"eд\": \"шт.\"}),\n" \
        "    (3, {\"название\": \"сканер\", \"цена\": 2000, \"количество\": 7, \"eд\": \"шт.\"})\n" \
        "]\n\n" \
        "Необходимо собрать аналитику о товарах.\n" \
        "Реализовать словарь, в котором каждый ключ — характеристика товара,\n" \
        "например название, а значение — список значений-характеристик, например список названий товаров.\n\n" \
        "Пример:\n" \
        "{\n" \
        "    \"название\": [\"компьютер\", \"принтер\", \"сканер\"],\n" \
        "    \"цена\": [20000, 6000, 2000],\n" \
        "    \"количество\": [5, 2, 7],\n" \
        "    \"ед\": [\"шт.\"]\n" \
        "}\n"
print(message)

products = []

while (True):
    number = input("Введите номер товара: ")
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    count = input("Введите количество товара: ")
    unit = input("Введите единицу измерения товара: ")

    products.append(tuple([number, {"название": name, "цена": price, "количество": count, "eд": unit}]))

    if input("Хотите еще добавить (да/нет)?") != 'да':
        break
    print()

print("\nТекущий список товаров: ")
print(products)
print("\n")

analitics = {}
for product in products:
    for key, value in product[1].items():
        if key not in analitics:
            analitics[key] = []
        analitics[key].append(value)

print("Аналитика: ")
print(analitics)

message = "1. Создать список и заполнить его элементами различных типов данных.\n" \
        "Реализовать скрипт проверки типа данных каждого элемента.\n" \
        "Использовать функцию type() для проверки типа.\n" \
        "Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.\n"
print(message)

my_list = [111, 'text', 11.1, None, [1, 2]]

for el in my_list:
    print("{}: {}".format(el, type(el)))

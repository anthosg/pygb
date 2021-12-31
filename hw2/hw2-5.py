message = "5. Реализовать структуру «Рейтинг»,\n" \
        "представляющую собой не возрастающий набор натуральных чисел.\n" \
        "У пользователя необходимо запрашивать новый элемент рейтинга.\n" \
        "Если в рейтинге существуют элементы с одинаковыми значениями,\n" \
        "то новый элемент с тем же значением должен разместиться после них.\n" \
        "Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.\n" \
        "Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.\n" \
        "Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.\n" \
        "Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.\n" \
        "Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].\n"
print(message)

element = int(input("Введите новый элемент рейтинга: "))

my_list = [7, 5, 3, 3, 2]
ranged_list = list(reversed(range(min(my_list), element)))

if element > max(my_list):
    my_list.insert(0, element)
elif element in my_list:
    my_list.insert(my_list.index(element), element)
elif any(x in my_list for x in ranged_list):
    for r in ranged_list:
        if r in my_list:
            my_list.insert(my_list.index(r), element)
            break
else:
    my_list.append(element)

print(my_list)

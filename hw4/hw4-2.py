message = "2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.\n" \
        "Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.\n" \
        "Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].\n" \
        "Результат: [12, 44, 4, 10, 78, 123].\n"

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in old_list if el > old_list[old_list.index(el)-1]]

print(f'Старый список: {old_list}')
print(f'Новый список: {new_list}')

message = "5. Реализовать формирование списка, используя функцию range() и возможности генератора.\n" \
        "В список должны войти четные числа от 100 до 1000 (включая границы).\n" \
        "Необходимо получить результат вычисления произведения всех элементов списка.\n" \
        "Подсказка: использовать функцию reduce().\n"
print(message)

from functools import reduce

def my_func(el_p, el):
    return el_p * el

even_values = [el for el in range(100, 1001) if el % 2 == 0]
result_values = reduce(my_func, even_values)

print(f'Четные: {even_values}')
print(f'Результат: {result_values}')

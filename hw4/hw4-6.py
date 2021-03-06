message = "6. Реализовать два небольших скрипта:\n" \
        "итератор, генерирующий целые числа, начиная с указанного;\n" \
        "итератор, повторяющий элементы некоторого списка, определенного заранее.\n\n" \
        "Подсказка: использовать функцию count() и cycle() модуля itertools.\n" \
        "Обратите внимание, что создаваемый цикл не должен быть бесконечным.\n" \
        "Предусмотрите условие его завершения.\n" \
        "Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 - завершаем цикл.\n" \
        "Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.\n"
print(message)

from itertools import count,  cycle

print("итератор, генерирующий целые числа, начиная с указанного")

start = 3
end = 10

for el in count(start):
    if el > end:
        break
    else:
        print(el)

print("\nитератор, повторяющий элементы некоторого списка, определенного заранее")

old_list = [1, 2, 3, 2, 5, 6]
new_list = []
iter = cycle(old_list)

while True:
    try:
        n = next(iter)
    except StopIteration:
        break

    if n in new_list:
        break
    new_list.append(n)

print(old_list)
print(new_list)

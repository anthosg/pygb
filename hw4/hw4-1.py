message = "1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.\n" \
        "Используйте в нём формулу: (выработка в часах*ставка в час) + премия.\n" \
        "Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.\n"
print(message)

import sys

if len(sys.argv) < 4:
    print("Usage: python hw4-1.py time salary bonus")
    print("Example: python hw4-1.py 10 20 30")
    sys.exit()

filename, time, salary, bonus = sys.argv
try:
    res = (int(time) * int(salary)) + int(bonus)
    print(f'Заработная плата сотрудника: {res}')
except ValueError:
    print('Аргументы должны быть цифрами.')

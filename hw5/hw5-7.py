message = "7. Создать вручную и заполнить несколькими строками текстовый файл,\n" \
    "в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.\n" \
    "Пример строки файла: firm_1 ООО 10000 5000.\n" \
    "Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.\n" \
    "Если фирма получила убытки, в расчёт средней прибыли её не включать.\n" \
    "Далее реализовать список.\n" \
    "Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.\n" \
    "Если фирма получила убытки, также добавить её в словарь (со значением убытков).\n" \
    "Пример списка: [{\"firm_1\": 5000, \"firm_2\": 3000, \"firm_3\": 1000}, {\"average_profit\": 2000}].\n" \
    "Итоговый список сохранить в виде json-объекта в соответствующий файл.\n" \
    "Пример json-объекта: [{\"firm_1\": 5000, \"firm_2\": 3000, \"firm_3\": 1000}, {\"average_profit\": 2000}]\n" \
    "Подсказка: использовать менеджер контекста.\n"
print(message)

import json

firms = {}
profits = []

with open("hw5-7.txt", "r", encoding='utf-8') as file:
    for line in file:
        name, ownership, proceed, cost = line.split()
        firms[name] = int(proceed) - int(cost)
        if firms[name] > 0:
            profits.append(firms[name])

average_profit = {"average_profit": round(sum(profits) / len(profits))}

with open('hw5-7.json', 'w') as file2:
    json.dump([firms, average_profit], file2)
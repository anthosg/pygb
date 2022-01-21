message = "3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).\n" \
        "Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.\n" \
        "Выполнить подсчет средней величины дохода сотрудников.\n" \
        "Пример файла:\n" \
        "  Иванов 23543.12\n" \
        "  Петров 13749.32\n"
print(message)

file = open("hw5-3.txt", "r", encoding='utf-8')
text = file.readlines()
file.close()

salary = []
small_salary = []

for line in text:
    line_list = line.split()
    salary.append(float(line_list[1]))
    if float(line_list[1]) < 20000.0:
       small_salary.append(line_list)

if len(small_salary) > 0:
    print("Сотрудники с окладом менее 20 тыс.:")
    for line_list in small_salary:
        print(f"  {line_list[0]} - {line_list[1]}")

print(f"\nСредняя величина дохода сотрудников: {round(sum(salary) / len(salary), 2)}")

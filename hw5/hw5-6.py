message = "6. Сформировать (не программно) текстовый файл.\n" \
        "В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.\n" \
        "Сюда должно входить и количество занятий.\n" \
        "Необязательно, чтобы для каждого предмета были все типы занятий.\n" \
        "Сформировать словарь, содержащий название предмета и общее количество занятий по нему.\n" \
        "Вывести его на экран.\n" \
        "Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).\n" \
        "Физика: 30(л) — 10(лаб)\n" \
        "Физкультура: — 30(пр) —\n" \
        "Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}\n"
print(message)

lessons = {}

file = open("hw5-6.txt", "r", encoding='utf-8')

while True:
    line = file.readline()
    if not line:
        break

    subject, lecture, practice, laboratory = line.split()

    subject = subject.rstrip(":")

    lecture = ''.join([x for x in lecture if x.isdigit()])
    if not lecture:
        lecture = 0

    practice = ''.join([x for x in practice if x.isdigit()])
    if not practice:
        practice = 0

    laboratory = ''.join([x for x in laboratory if x.isdigit()])
    if not laboratory:
        laboratory = 0

    lessons[subject] = int(lecture) + int(practice) + int(laboratory)

file.close()
print(lessons)

message = "4. Создать (не программно) текстовый файл со следующим содержимым:\n" \
        "One — 1\n" \
        "Two — 2\n" \
        "Three — 3\n" \
        "Four — 4\n" \
        "Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.\n" \
        "При этом английские числительные должны заменяться на русские.\n" \
        "Новый блок строк должен записываться в новый текстовый файл.\n"
print(message)

translated_line = [];
translate = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

file = open("hw5-4.txt", "r", encoding='utf-8')

while True:
    line = file.readline()
    if not line:
        break
    line_list = line.split(" - ")
    if line_list[0] in translate:
        translated_line.append(translate[line_list[0]] + " - " + line_list[1])

file.close()

file2 = open("hw5-4-2.txt", "w", encoding='utf-8')
file2.writelines(translated_line)
file2.close()

print("Новый файл записан.")

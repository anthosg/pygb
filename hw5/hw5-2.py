message = "2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.\n"
print(message)

file = open("hw5-2.txt", "r")

text = file.readlines()
print(f"Всего строк: {len(text)}")

i = 1
for line in text:
    print(f"{i} строка содержить {len(line.split())} слов")
    i += 1

file.close()

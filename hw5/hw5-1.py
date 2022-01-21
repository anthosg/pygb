message = "1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.\n" \
        "Об окончании ввода данных свидетельствует пустая строка.\n"
print(message)

file = open("hw5-1.txt", "w")

while True:
    text = input("Введите текст: ")
    file.write(text + "\n")
    if not text:
        break

file.close()

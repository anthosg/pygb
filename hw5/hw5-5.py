message = "5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.\n" \
        "Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.\n"
print(message)

import random

file1 = open("hw5-5.txt", "w", encoding='utf-8')
file1.writelines([str(random.randint(1, 1000)) + " " for _ in range(20)])
file1.close()

file2 = open("hw5-5.txt", "r", encoding='utf-8')
total = sum([int(i) for i in file2.readline().split()])
print(f"Сумма чисел: {total}")
file2.close()

message = "4. Пользователь вводит целое положительное число.\n" \
        "Найдите самую большую цифру в числе.\n" \
        "Для решения используйте цикл while и арифметические операции.\n"
print(message)

number = input("Введите целое положительное число: ")
maximum = number[0]
count = len(number) - 1

while (count > 0):
    if maximum < number[count]:
        maximum = number[count]
    count = count - 1

print(f"\nСамая большая цифра - {maximum}")

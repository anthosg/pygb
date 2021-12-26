message = "3. Узнайте у пользователя число n.\n" \
        "Найдите сумму чисел n + nn + nnn.\n" \
        "Например, пользователь ввёл число 3.\n" \
        "Считаем 3 + 33 + 333 = 369.\n"
print(message)

number = input("Введите число: ")

result = int(number) + int(number + number) + int(number + number + number)

print(f"\nРезультат - {result}")

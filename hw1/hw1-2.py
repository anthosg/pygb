message = "2. Пользователь вводит время в секундах.\n" \
            "Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.\n" \
            "Используйте форматирование строк.\n"
print(message)

input_second = int(input("Введите время в секундах: "))

hour = input_second // 3600
minute = input_second % 3600 // 60
second = input_second % 60

print(f"\nВремя (чч:мм:сс) - {hour:02d}:{minute:02d}:{second:02d}")

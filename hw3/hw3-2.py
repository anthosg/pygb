message = "2. Реализовать функцию, принимающую несколько параметров,\n" \
        "описывающих данные пользователя: имя, фамилия, год рождения,\n" \
        "город проживания, email, телефон. Функция должна принимать\n" \
        "параметры как именованные аргументы.\n" \
        "Реализовать вывод данных о пользователе одной строкой.\n"
print(message)

def profile(first_name, last_name, birthyear, city, email, phone):
    return ', '.join([first_name, last_name, birthyear, city, email, phone])

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
birthyear = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите электронную почту: ")
phone = input("Введите телефон: ")

print(profile(first_name, last_name, birthyear, city, email, phone))

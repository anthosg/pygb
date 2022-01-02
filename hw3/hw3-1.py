message = "1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.\n" \
        "Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.\n"
print(message)

def division(number1, number2):
    try:
        return round(float(number1) / float(number2), 2)
    except ZeroDivisionError:
        return 0
    except ValueError:
        return None

number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")

print(f"{number1} / {number2} = {division(number1, number2)}")

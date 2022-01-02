message = "3. Реализовать функцию my_func(),\n" \
        "которая принимает три позиционных аргумента,\n" \
        "и возвращает сумму наибольших двух аргументов.\n"
print(message)

def my_func(number1, number2, number3):
    numbers = [number1, number2, number3]
    numbers.remove(min(number1, number2, number3))
    return sum(numbers)

number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите третье число: "))

print(f"Сумма наибольших двух чисел: {my_func(number1, number2, number3)}")

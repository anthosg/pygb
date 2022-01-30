message = "2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.\n" \
    "Проверьте его работу на данных, вводимых пользователем.\n" \
    "При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.\n"
print(message)

class ZeroDivision(Exception):
    def __init__(self, message="На ноль делить нельзя!"):
        self.message = message
        super().__init__(self.message)

while True:
    try:
        number = int(input("Введите число: "))
        if number == 0:
            raise ZeroDivision()
    except ValueError as e:
        print(e)
    except ZeroDivision as zd:
        print(zd)
    else:
        print(number)

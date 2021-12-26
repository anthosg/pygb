message = "5. Запросите у пользователя значения выручки и издержек фирмы.\n" \
        "Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).\n" \
        "Выведите соответствующее сообщение.\n" \
        "Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).\n" \
        "Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.\n"
print(message)

proceeds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
staffs = int(input("Введите численность сотрудников фирмы: "))
profit = proceeds - costs

if proceeds > costs:
    print("Выручка больше чем издержки.")
    print("Рентабельность выручки: ", round((profit / proceeds) * 100))
    print("Прибыль фирмы в расчете на одного сотрудника: ", round(profit / staffs))
elif proceeds < costs:
    print("Выручка меньше чем издержки.")
else:
    print("Выручка равно издержкам.")

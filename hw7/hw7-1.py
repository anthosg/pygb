message = "1. Реализовать класс Matrix (матрица).\n" \
        "Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.\n" \
        "Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.\n" \
        "Примеры матриц: 3 на 2, 3 на 3, 2 на 4.\n" \
        "31    32         3    5    32        3    5    8    3\n" \
        "37    43         2    4    6         8    3    7    1\n" \
        "51    86        -1   64   -8\n" \
        "Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.\n" \
        "Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).\n" \
        "Результатом сложения должна быть новая матрица.\n" \
        "Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.\n"
print(message)

class Matrix:
    matrix_list = None

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        matrix_list = [[0]* len(self.matrix_list[0]) for i in range(len(self.matrix_list))]
        for i1 in range(len(self.matrix_list)):
            for i2 in range(len(other.matrix_list[i1])):
                matrix_list[i1][i2] = self.matrix_list[i1][i2] + other.matrix_list[i1][i2]
        return Matrix(matrix_list)

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i2) for i2 in i1]) for i1 in self.matrix_list]))

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
matrix3 = matrix1 + matrix2

print(matrix3)
print()

print(matrix1)
print()

print(matrix2)

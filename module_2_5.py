"""
Объявите функцию get_matrix и напишите в ней параметры n, m и value.
Создайте пустой список matrix внутри функции get_matrix.
Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
В первом цикле добавляйте пустой список в список matrix.
Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
Во втором цикле пополняйте ранее добавленный пустой список значениями value.
После всех циклов верните значение переменной matrix.
Выведите на экран(консоль) результат работы функции get_matrix.
"""

def get_matrix(n, m, value):
    matrix: list = []
    for _ in range(n):
        row: list = []
        for _ in range(m):
            row.append(value)
        matrix.append(row)
    print(matrix)
    return matrix

get_matrix(2, 2, 10)


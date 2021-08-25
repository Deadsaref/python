# подсмотрел реализацию списка списков, т.к. у самого не получилось
from typing import List


class Matrix:

    def __init__(self, matrix: List[List]):
        self.__matrix = matrix

    def __add__(self, other):
        result = []
        for num in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*num)])

        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(m1 + m2)

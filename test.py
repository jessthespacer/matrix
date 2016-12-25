import matrix
a = matrix.matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = matrix.matrix(3, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(a)
print(a.determinant())
print(b)
print(b.determinant())
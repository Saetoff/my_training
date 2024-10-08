def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0:
        return matrix
    for i in range(n):
        mat = []
        matrix.append(mat)
        for _ in range(m):
            matrix[i].append(value)

    return matrix


matrix1 = get_matrix(2, 2, 10)
matrix2 = get_matrix(3, 5, 42)
matrix3 = get_matrix(4, 2, 13)
print(matrix1)
print(matrix2)
print(matrix3)


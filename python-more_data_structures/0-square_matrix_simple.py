def square_matrix_simple(matrix=[]):
    square_matrix = []

    for row in matrix:
        square_row = []

        for num in row:
            square_row.append(num ** 2)

        square_matrix.append(square_row)

    return square_matrix

        
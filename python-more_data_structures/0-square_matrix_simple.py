def square_matrix_simple(matrix=[]):
    # 1. Create an empty matrix to store the squared values
    square_matrix = []

     # 2. Iterate through each row in the input matrix
    for row in matrix:
        # Create an empty row to store the squared values of the current row
        square_row = []
         # Iterate through each element in the current row and square it
        for num in row:
            square_row.append(num ** 2)
          # Add the squared row to the squared matrix
        square_matrix.append(square_row)

    return square_matrix

            
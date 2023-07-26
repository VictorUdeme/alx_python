def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row): #Used the enumerate() function to keep track of index(i) while iterating 2ru loops
            print("{:d}".format(num), end=' ' if i < len(row) - 1 else '')
        print()
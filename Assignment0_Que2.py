def matrix_operation(array1, array2, operation):
    # Helper function to calculate dot product of two vectors (1D arrays)
    def dot_product(vec1, vec2):
        if len(vec1) != len(vec2):
            return "Error: Vectors must have the same length for dot product."
        return sum(vec1[i] * vec2[i] for i in range(len(vec1)))

    # Helper function to perform matrix multiplication
    def matrix_multiply(mat1, mat2):
        # Check if matrix multiplication is possible
        if len(mat1[0]) != len(mat2):
            return "Error: Number of columns in the first matrix must be equal to number of rows in the second."
        result = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                result[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
        return result

    # Helper function to calculate the determinant of a matrix (only for 2x2 or 3x3)
    def determinant(matrix):
        # Check if the matrix is square
        if len(matrix) != len(matrix[0]):
            return "Error: Determinants can only be calculated for square matrices."

        # Base case for 2x2 matrix
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        # Base case for 3x3 matrix
        elif len(matrix) == 3:
            return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
                    - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
                    + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
        else:
            return "Error: Determinant function only supports 2x2 or 3x3 matrices."

    if operation == "dot":
        # Flatten arrays if they are 1D and calculate dot product
        flat_array1 = [elem for row in array1 for elem in row]
        flat_array2 = [elem for row in array2 for elem in row]
        return dot_product(flat_array1, flat_array2)

    elif operation == "matrix":
        return matrix_multiply(array1, array2)

    elif operation == "determinant":
        det1 = determinant(array1)
        det2 = determinant(array2)
        return (det1, det2)

    else:
        return "Error: Unsupported operation. Please choose 'dot', 'matrix', or 'determinant'."

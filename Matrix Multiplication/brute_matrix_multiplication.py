def matrix_multiply(A, B):
    # Get dimensions of A and B
    rows_A = len(A)
    cols_A = len(A[0])  # Number of columns in A
    rows_B = len(B)
    cols_B = len(B[0])  # Number of columns in B

    # Check if multiplication is possible
    if cols_A != rows_B:
        print("Error: Number of columns in A must be equal to the number of rows in B.")
        return None

    # Initialize the result matrix with zeros (size rows_A x cols_B)
    C = []
    for i in range(rows_A):
        C.append([0] * cols_B)

    # Perform the brute-force multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Example usage:
A = [[1, 2, 3, 4],
              [5, 6, 7, 8]]

B = [[16, 15, 14],
              [12, 11, 10],
              [8, 7, 6],
              [4, 3, 2]]

C = matrix_multiply(A, B)

# Display the result
if C:
    for row in C:
        print(row)

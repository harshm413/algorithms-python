import numpy as np

def add_matrices(A, B):
    return np.add(A, B)

def subtract_matrices(A, B):
    return np.subtract(A, B)

def split_matrix(M):
    n, m = M.shape
    mid_n, mid_m = n // 2, m // 2
    A11 = M[:mid_n, :mid_m]
    A12 = M[:mid_n, mid_m:]
    A21 = M[mid_n:, :mid_m]
    A22 = M[mid_n:, mid_m:]
    return A11, A12, A21, A22

def merge_matrices(C11, C12, C21, C22):
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))

def brute_force(A, B):
    return np.dot(A, B)

def strassen(A, B):
    if len(A) <= 2:
        return brute_force(A, B)

    a, b, c, d = split_matrix(A)
    e, f, g, h = split_matrix(B)

    p1 = strassen(add_matrices(a, d), add_matrices(e, h))
    p2 = strassen(d, subtract_matrices(g, e))
    p3 = strassen(add_matrices(a, b), h)
    p4 = strassen(b, subtract_matrices(g, h))
    p5 = strassen(a, subtract_matrices(f, h))
    p6 = strassen(add_matrices(c, d), e)
    p7 = strassen(subtract_matrices(a, c), add_matrices(e, f))

    C11 = add_matrices(subtract_matrices(add_matrices(p1, p2), p3), p4)
    C12 = add_matrices(p5, p3)
    C21 = add_matrices(p6, p2)
    C22 = add_matrices(subtract_matrices(add_matrices(p1, p5), p6), p7)

    return merge_matrices(C11, C12, C21, C22)

# Testing the Strassen matrix multiplication
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])

B = np.array([[16, 15, 14],
              [12, 11, 10],
              [8, 7, 6],
              [4, 3, 2]])

C = strassen(A, B)

print("Result of Strassen's matrix multiplication:")
print(C)

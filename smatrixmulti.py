import numpy as np

def strassen_2x2(A, B):
    # Extract matrix elements
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    e, f, g, h = B[0, 0], B[0, 1], B[1, 0], B[1, 1]

    # Calculate 7 Strassen products
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    # Compute sub-matrices
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    return np.array([[c11, c12], 
                     [c21, c22]])

# Test
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 2], [3, 4]])

print("Strassen 2x2 Result:")
print(strassen_2x2(A, B))
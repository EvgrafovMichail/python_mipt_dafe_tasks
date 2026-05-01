import numpy as np


class ShapeMissmatchError: ...


def some_product(vec1: np.ndarray, vec2: np.ndarray, vec3: np.ndarray):
    if any(x > 2 for x in (vec1.ndim, vec2.ndim, vec3.ndim)):
        raise ShapeMissmatchError

    if not (vec1.shape == vec2.shape == vec3.shape):
        raise ShapeMissmatchError

    return np.sum(vec1 * np.cross(vec2, vec3), axis=-1)


# Single vectors
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
c = np.array([0, 0, 1])
print(some_product(a, b, c))  # Output: 1.0

# Matrices of vectors
A = np.array([[1, 0, 0], [1, 1, 1]])
B = np.array([[0, 1, 0], [0, 1, 0]])
C = np.array([[0, 0, 1], [0, 0, 1]])
print(some_product(A, B, C))  # Output: [1.0, 1.0]

import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_to_sphere(
    xs: np.ndarray,
    ys: np.ndarray,
    zs: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (len(xs) == len(ys) == len(zs)):
        raise ShapeMismatchError

    r = np.sqrt(xs**2 + ys**2 + zs**2)
    phi = np.arctan2(ys, xs)
    alpha = np.arctan2(np.sqrt(xs**2 + ys**2), zs)

    return (r, phi, alpha)


def convert_from_sphere(
    r: np.ndarray,
    phi: np.ndarray,
    alpha: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (len(r) == len(phi) == len(alpha)):
        raise ShapeMismatchError

    x = r * np.sin(alpha) * np.cos(phi)
    y = r * np.sin(alpha) * np.sin(phi)
    z = r * np.cos(alpha)

    return (x, y, z)

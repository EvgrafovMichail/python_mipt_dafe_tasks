import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (distances.shape == azimuth.shape == inclination.shape):
        raise ShapeMismatchError

    z = distances * np.cos(inclination)
    x = distances * np.sin(inclination) * np.cos(azimuth)
    y = distances * np.sin(inclination) * np.sin(azimuth)

    return x, y, z


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x, y, z = abscissa, ordinates, applicates

    if not (x.shape == y.shape == z.shape):
        raise ShapeMismatchError

    r = np.sqrt(x**2 + y**2 + z**2)
    phi = np.arctan2(y, x)
    r_xy = np.sqrt(x**2 + y**2)
    theta = np.arctan2(r_xy, z)

    return r, phi, theta

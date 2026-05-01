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

    x = distances * np.sin(inclination) * np.cos(azimuth)
    y = distances * np.sin(inclination) * np.sin(azimuth)
    z = distances * np.cos(inclination)
    return x, y, z


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (abscissa.shape == ordinates.shape == applicates.shape):
        raise ShapeMismatchError

    r = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    az = np.arctan2(ordinates, abscissa)

    inc = np.zeros(r.shape)
    inc[r != 0] = np.arccos(applicates[r != 0] / r[r != 0])

    return r, az, inc

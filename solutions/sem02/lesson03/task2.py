import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (distances.shape == azimuth.shape == inclination.shape):
        raise ShapeMismatchError("distances, azimuth, inclination must have same shape")

    x = distances * np.cos(azimuth) * np.sin(inclination)
    y = distances * np.sin(azimuth) * np.sin(inclination)
    z = distances * np.cos(inclination)

    return x, y, z


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (abscissa.shape == ordinates.shape == applicates.shape):
        raise ShapeMismatchError("abscissa, ordinates, applicates must have same shape")

    distances = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    inclination = np.arctan2(ordinates, abscissa)
    azimuth = np.arctan2(np.sqrt(abscissa**2 + ordinates**2), applicates)

    return distances, inclination, azimuth

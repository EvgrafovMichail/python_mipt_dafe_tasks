import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (np.shape(distances) == np.shape(azimuth) == np.shape(inclination)):
        raise ShapeMismatchError
    x = distances * np.cos(azimuth) * np.sin(inclination)
    y = distances * np.sin(azimuth) * np.sin(inclination)
    z = distances * np.cos(inclination)
    return x, y, z


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (np.shape(abscissa) == np.shape(ordinates) == np.shape(applicates)):
        raise ShapeMismatchError
    distance = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    azimuth = np.arctan2(ordinates, abscissa)
    inciclination = np.zeros_like(distance)
    compare_mask = distance != 0.0

    inciclination[compare_mask] = np.arccos(applicates[compare_mask] / distance[compare_mask])
    return distance, azimuth, inciclination

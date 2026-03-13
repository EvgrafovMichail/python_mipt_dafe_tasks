import numpy as np
from numpy.ma.core import arccos, arctan2


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if (
        (distances.shape != azimuth.shape)
        or (distances.shape != inclination.shape)
        or (azimuth.shape != inclination.shape)
    ):
        raise ShapeMismatchError
    abscissa = distances * np.sin(inclination) * np.cos(azimuth)
    ordinates = distances * np.sin(inclination) * np.sin(azimuth)
    applicates = distances * np.cos(inclination)
    return abscissa, ordinates, applicates


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if (
        (abscissa.shape != ordinates.shape)
        or (abscissa.shape != applicates.shape)
        or (ordinates.shape != applicates.shape)
    ):
        raise ShapeMismatchError
    distances = (abscissa**2 + ordinates**2 + applicates**2) ** 0.5
    inclication = arccos(applicates / distances)
    azimuth = arctan2(ordinates, abscissa)
    return distances, azimuth, inclication

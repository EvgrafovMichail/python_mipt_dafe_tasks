import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if distances.shape != azimuth.shape or azimuth.shape != inclination.shape:
        raise ShapeMismatchError

    print(distances.size, azimuth.size)

    abscissa = distances * np.sin(inclination) * np.cos(azimuth)
    ordinates = distances * np.sin(inclination) * np.sin(azimuth)
    applicates = distances * np.cos(inclination)

    return abscissa, ordinates, applicates


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if abscissa.shape != ordinates.shape or ordinates.shape != applicates.shape:
        raise ShapeMismatchError

    distances = (abscissa**2 + ordinates**2 + applicates**2) ** 0.5
    inclination = np.arctan2((abscissa**2 + ordinates**2) ** 0.5, applicates)
    azimuth = np.arctan2(ordinates, abscissa)

    return distances, azimuth, inclination

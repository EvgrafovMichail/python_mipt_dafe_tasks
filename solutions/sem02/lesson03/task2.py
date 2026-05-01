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

    abscissa = distances * np.sin(inclination) * np.cos(azimuth)
    ordinates = distances * np.sin(inclination) * np.sin(azimuth)
    applicates = distances * np.cos(inclination)

    return (abscissa, ordinates, applicates)


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (abscissa.shape == ordinates.shape == applicates.shape):
        raise ShapeMismatchError

    distances = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    azimuth = np.arctan2(ordinates, abscissa)

    with np.errstate(divide="ignore", invalid="ignore"):
        inclination = np.where(distances == 0, 0.0, np.arccos(applicates / distances))

    return (distances, azimuth, inclination)

import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if distances.shape != azimuth.shape or distances.shape != inclination.shape:
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
    if abscissa.shape != ordinates.shape or abscissa.shape != applicates.shape:
        raise ShapeMismatchError

    distances = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    azimuth = np.atan2(ordinates, abscissa)
    safe_distances = np.where(distances == 0, 1, distances)
    inclination = np.where(distances == 0, 0.0, np.acos(applicates / safe_distances))

    return distances, azimuth, inclination

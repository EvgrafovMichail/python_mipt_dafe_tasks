import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if distances.shape != azimuth.shape or distances.shape != inclination.shape:
        raise ShapeMismatchError("размеры не совпадают")

    x = np.multiply(distances, np.multiply(np.cos(azimuth), np.sin(inclination)))
    y = np.multiply(distances, np.multiply(np.sin(azimuth), np.sin(inclination)))
    z = np.multiply(distances, np.cos(inclination))

    return x, y, z


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if abscissa.shape != ordinates.shape or abscissa.shape != applicates.shape:
        raise ShapeMismatchError("размеры не совпадают")

    distances = np.sqrt(
        np.add(np.add(np.square(abscissa), np.square(ordinates)), np.square(applicates))
    )
    azimuth = np.where(distances != 0, np.arctan2(ordinates, abscissa), 0.0)
    inclination = np.where(distances != 0, np.arccos(applicates / distances), 0.0)

    return distances, azimuth, inclination

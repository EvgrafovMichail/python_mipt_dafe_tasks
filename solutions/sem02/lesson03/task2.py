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
    x = distances * np.cos(azimuth) * np.sin(inclination)
    y = distances * np.sin(azimuth) * np.sin(inclination)
    z = distances * np.cos(inclination)
    return x, y, z


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if abscissa.shape != ordinates.shape or abscissa.shape != applicates.shape:
        raise ShapeMismatchError
    r = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    azimuth = np.arctan2(ordinates, abscissa)
    inclination = np.zeros_like(r)
    mask = r != 0
    inclination[mask] = np.arccos(applicates[mask] / r[mask])
    return r, azimuth, inclination

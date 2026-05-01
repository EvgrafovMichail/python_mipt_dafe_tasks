import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (len(distances) == len(azimuth) == len(inclination)):
        raise ShapeMismatchError
    return (
        distances * np.sin(inclination) * np.cos(azimuth),
        distances * np.sin(inclination) * np.sin(azimuth),
        distances * np.cos(inclination),
    )


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (len(abscissa) == len(ordinates) == len(applicates)):
        raise ShapeMismatchError
    return (
        np.sqrt(np.power(abscissa, 2) + np.power(ordinates, 2) + np.power(applicates, 2)),
        np.arctan2(ordinates, abscissa),
        np.arctan2(np.sqrt(abscissa**2 + ordinates**2), applicates),
    )

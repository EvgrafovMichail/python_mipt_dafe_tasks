import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not distances.shape == azimuth.shape == inclination.shape:
        raise ShapeMismatchError
    return tuple(
        (
            distances * np.sin(inclination) * np.cos(azimuth),
            distances * np.sin(inclination) * np.sin(azimuth),
            distances * np.cos(inclination),
        )
    )


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not abscissa.shape == ordinates.shape == applicates.shape:
        raise ShapeMismatchError
    distances = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    azimuth = np.arctan2(ordinates, abscissa)
    inclination = np.arccos(applicates / distances)

    mask = distances == 0
    inclination[mask] = 0.0
    azimuth[mask] = 0.0
    return (distances, azimuth, inclination)

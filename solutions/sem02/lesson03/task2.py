import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if (
        azimuth.shape != distances.shape
        or inclination.shape != distances.shape
        or azimuth.shape != inclination.shape
    ):
        raise ShapeMismatchError()
    else:
        x = distances * np.sin(inclination) * np.cos(azimuth)
        z = distances * np.cos(inclination)
        y = distances * np.sin(inclination) * np.sin(azimuth)
        return tuple([x, y, z])


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if (
        ordinates.shape != abscissa.shape
        or ordinates.shape != applicates.shape
        or abscissa.shape != applicates.shape
    ):
        raise ShapeMismatchError
    else:
        r = (abscissa**2 + ordinates**2 + applicates**2) ** 0.5
        mask = r != 0
        inclination = np.zeros(r.shape)
        azimuth = np.zeros(r.shape)
        inclination[mask] = np.arccos(applicates[mask] / r[mask])
        azimuth[mask] = np.arctan2(ordinates[mask], abscissa[mask])
        return tuple([r, azimuth, inclination])

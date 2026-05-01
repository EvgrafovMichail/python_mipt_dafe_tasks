import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if distances.shape == azimuth.shape == inclination.shape:
        abscissa = distances * np.sin(inclination) * np.cos(azimuth)
        ordinates = distances * np.sin(inclination) * np.sin(azimuth)
        applicates = distances * np.cos(inclination)
        return (abscissa, ordinates, applicates)
    raise ShapeMismatchError


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if abscissa.shape == ordinates.shape == applicates.shape:
        distances = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
        azimuth = np.zeros(distances.shape)
        azimuth[distances > 0] = np.arctan2(ordinates[distances > 0], abscissa[distances > 0])
        inclination = np.zeros(distances.shape)
        inclination[distances > 0] = np.arccos(applicates[distances > 0] / distances[distances > 0])

        return (distances, azimuth, inclination)
    raise ShapeMismatchError

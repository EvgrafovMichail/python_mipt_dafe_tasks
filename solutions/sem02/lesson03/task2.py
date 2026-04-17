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
    abscissa = distances * np.sin(inclination) * np.cos(azimuth)
    ordinates = distances * np.sin(inclination) * np.sin(azimuth)
    applicates = distances * np.cos(inclination)
    answer = (abscissa, ordinates, applicates)
    return answer



def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if abscissa.shape != ordinates.shape or ordinates.shape != applicates.shape:
        raise ShapeMismatchError
    azimuth = np.atan2(ordinates, abscissa)
    distances = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    non_zeros_idx = distances != 0
    inclination = np.zeros_like(distances)
    inclination[non_zeros_idx] = np.arccos(applicates[non_zeros_idx] / distances[non_zeros_idx])
    answer = (distances, azimuth, inclination)
    return answer


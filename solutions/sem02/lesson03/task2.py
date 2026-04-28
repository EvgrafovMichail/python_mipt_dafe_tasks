import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if distances.size != azimuth.size or distances.size != inclination.size:
        raise ShapeMismatchError
    if distances.ndim != azimuth.ndim or distances.ndim != inclination.ndim:
        raise ShapeMismatchError
    if distances.ndim > 2:
        raise ShapeMismatchError
    if distances.ndim == 2 and (
        distances.shape[1] != azimuth.shape[1] or distances.shape[1] != inclination.shape[1]
    ):
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
    if abscissa.size != ordinates.size or abscissa.size != applicates.size:
        raise ShapeMismatchError
    if abscissa.ndim != ordinates.ndim or abscissa.ndim != applicates.ndim:
        raise ShapeMismatchError
    if abscissa.ndim > 2:
        raise ShapeMismatchError
    if abscissa.ndim == 2 and (
        abscissa.shape[1] != ordinates.shape[1] or abscissa.shape[1] != applicates.shape[1]
    ):
        raise ShapeMismatchError
    return (
        (abscissa**2 + ordinates**2 + applicates**2) ** 0.5,
        np.atan2(ordinates, abscissa),
        np.atan2((abscissa**2 + ordinates**2) ** 0.5, applicates),
    )

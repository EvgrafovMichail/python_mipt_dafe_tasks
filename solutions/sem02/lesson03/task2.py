import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if distances.shape != azimuth.shape:
        raise ShapeMismatchError
    if distances.shape != inclination.shape:
        raise ShapeMismatchError

    n = len(distances)

    x = np.zeros(n)
    y = np.zeros(n)
    z = np.zeros(n)

    for i in range(n):
        r = distances[i]
        phi = azimuth[i]
        theta = inclination[i]

        sin_theta = np.sin(theta)
        cos_theta = np.cos(theta)
        sin_phi = np.sin(phi)
        cos_phi = np.cos(phi)

        x_i = r * sin_theta * cos_phi
        y_i = r * sin_theta * sin_phi
        z_i = r * cos_theta

        x[i] = x_i
        y[i] = y_i
        z[i] = z_i

    return x, y, z


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError
    if abscissa.shape != applicates.shape:
        raise ShapeMismatchError

    n = len(abscissa)

    r_array = np.zeros(n)
    phi_array = np.zeros(n)
    theta_array = np.zeros(n)

    for i in range(n):
        x = abscissa[i]
        y = ordinates[i]
        z = applicates[i]

        x2 = x * x
        y2 = y * y
        z2 = z * z
        r2 = x2 + y2 + z2
        r = np.sqrt(r2)

        if r > 0:
            cos_theta = z / r
            if cos_theta > 1.0:
                cos_theta = 1.0
            elif cos_theta < -1.0:
                cos_theta = -1.0
            theta = np.arccos(cos_theta)
        else:
            theta = 0.0

        phi = np.arctan2(y, x)

        r_array[i] = r
        phi_array[i] = phi
        theta_array[i] = theta

    return r_array, phi_array, theta_array

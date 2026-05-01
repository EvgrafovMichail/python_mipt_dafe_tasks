import numpy as np
from matplotlib import image


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    H, W = image.shape[:2]

    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        zer = np.zeros((H + 2 * pad_size, W + 2 * pad_size), dtype=image.dtype)
        zer[pad_size : pad_size + H, pad_size : pad_size + W] = image
    else:
        zer = np.zeros((H + 2 * pad_size, W + 2 * pad_size, image.shape[2]), dtype=image.dtype)
        zer[pad_size : pad_size + H, pad_size : pad_size + W, :] = image

    return zer


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError

    if kernel_size == 1:
        return image.copy()

    padded_image = pad_image(image, kernel_size // 2)
    res = np.zeros(image.shape, dtype=float)

    for i in range(kernel_size):
        for j in range(kernel_size):
            res += padded_image[i : i + image.shape[0], j : j + image.shape[1]]

    res /= kernel_size**2
    return res.astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

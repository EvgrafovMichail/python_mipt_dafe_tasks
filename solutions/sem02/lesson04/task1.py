import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        n, m = image.shape
        result = np.zeros((n + 2 * pad_size, m + 2 * pad_size), np.uint8)

    if image.ndim == 3:
        n, m, z = image.shape
        result = np.zeros((n + 2 * pad_size, m + 2 * pad_size, z), np.uint8)

    result[pad_size:-pad_size, pad_size:-pad_size] += image

    return result


def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if (kernel_size % 2 == 0) or (kernel_size < 1):
        raise ValueError("Kernel size must be odd and >= 1")

    if kernel_size == 1:
        return image.copy()

    pad_size = kernel_size // 2
    padded = pad_image(image, pad_size).astype(np.float32)

    sum_array = np.zeros(image.shape, dtype=np.float32)

    for i in range(kernel_size):
        for j in range(kernel_size):
            sum_array += padded[i : i + image.shape[0], j : j + image.shape[1], ...]

    return (sum_array / (kernel_size**2)).astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

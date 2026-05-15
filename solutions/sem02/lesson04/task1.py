import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        height, width = image.shape
        pad_height, pad_width = height + pad_size * 2, pad_size * 2 + width

        pad = np.zeros(shape=(pad_height, pad_width), dtype=image.dtype)
        pad[pad_size : pad_size + height, pad_size : pad_size + width] = image
        return pad

    if image.ndim == 3:
        height, width, channels = image.shape
        pad_height, pad_width = height + pad_size * 2, pad_size * 2 + width

        pad = np.zeros(shape=(pad_height, pad_width, channels), dtype=image.dtype)
        pad[pad_size : pad_size + height, pad_size : pad_size + width, :] = image
        return pad


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    padd_image = pad_image(image, kernel_size // 2)

    res = np.zeros(image.shape, dtype=image.dtype)
    height, width = image.shape[:2]

    for i in range(height):
        for j in range(width):
            if image.ndim == 2:
                kernel = padd_image[i : i + kernel_size, j : j + kernel_size]
                res[i, j] = np.mean(kernel)
            else:
                kernel = padd_image[i : i + kernel_size, j : j + kernel_size, :]
                res[i, j, :] = np.mean(kernel, axis=(0, 1))

    return res.astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

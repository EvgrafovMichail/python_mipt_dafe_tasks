import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1 or image.ndim > 3:
        raise ValueError
    if image.ndim == 2:
        height, weight = image.shape
        res_image = np.zeros((height + 2 * pad_size, weight + 2 * pad_size), dtype=image.dtype)
        res_image[pad_size : pad_size + height, pad_size : pad_size + weight] = image
    if image.ndim == 3:
        height, weight, razm = image.shape
        res_image = np.zeros(
            (height + 2 * pad_size, weight + 2 * pad_size, razm), dtype=image.dtype
        )
        res_image[pad_size : pad_size + height, pad_size : pad_size + weight, :] = image
    return res_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError
    elif kernel_size == 1:
        return image
    res_image = np.zeros(image.shape, dtype=np.float64)
    padded_image = pad_image(image, kernel_size // 2)
    if image.ndim == 2:
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                res_image[i, j] = np.mean(padded_image[i : i + kernel_size, j : j + kernel_size])
    if image.ndim == 3:
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                res_image[i, j] = np.mean(
                    padded_image[i : i + kernel_size, j : j + kernel_size, :], axis=(0, 1)
                )
    return np.round(res_image).astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

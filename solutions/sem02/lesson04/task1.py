import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        i, j = image.shape
        newimage = np.zeros((i + 2 * pad_size, j + 2 * pad_size), dtype=np.uint8)
        newimage[pad_size : pad_size + i, pad_size : pad_size + j] = image

    else:
        i, j, k = image.shape
        newimage = np.zeros((i + 2 * pad_size, j + 2 * pad_size, k), dtype=np.uint8)
        newimage[pad_size : pad_size + i, pad_size : pad_size + j, :] = image

    return newimage


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    if kernel_size == 1:
        return image

    newimage = pad_image(image, kernel_size // 2)

    if image.ndim == 2:
        i, j = image.shape
        result = np.zeros((i, j), dtype=np.float32)

        for a in range(i):
            for b in range(j):
                result[a, b] = np.mean(newimage[a : a + kernel_size, b : b + kernel_size])

    else:
        i, j, k = image.shape
        result = np.zeros((i, j, k), dtype=np.float32)

        for a in range(i):
            for b in range(j):
                result[a, b] = np.mean(
                    newimage[a : a + kernel_size, b : b + kernel_size, :], axis=(0, 1)
                )

    return result.astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

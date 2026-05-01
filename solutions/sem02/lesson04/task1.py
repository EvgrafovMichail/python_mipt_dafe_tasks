import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError("pad_size must be a positive integer")
    if image.ndim not in (2, 3):
        raise ValueError("image must be a 2D or 3D array")

    new_shape = list(image.shape)
    new_shape[0] += 2 * pad_size
    new_shape[1] += 2 * pad_size

    new_image = np.zeros(new_shape, dtype=image.dtype)
    new_image[
        pad_size : pad_size + image.shape[0],
        pad_size : pad_size + image.shape[1],
    ] = image
    return new_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError("kernel_size must be a more then 1 and odd integer")

    pad_size = kernel_size // 2
    try:
        new_image = pad_image(image, pad_size)
    except ValueError:
        new_image = image.copy()

    if image.ndim == 2:
        padded_sum = new_image.astype(np.uint64)
        matrix = np.zeros((padded_sum.shape[0] + 1, padded_sum.shape[1] + 1), dtype=np.uint64)
        matrix[1:, 1:] = padded_sum.cumsum(axis=0).cumsum(axis=1)

        summa = (
            matrix[kernel_size:, kernel_size:]
            - matrix[:-kernel_size, kernel_size:]
            - matrix[kernel_size:, :-kernel_size]
            + matrix[:-kernel_size, :-kernel_size]
        )
    else:
        padded_sum = new_image.astype(np.uint64)
        matrix = np.zeros(
            (padded_sum.shape[0] + 1, padded_sum.shape[1] + 1, padded_sum.shape[2]),
            dtype=np.uint64,
        )
        matrix[1:, 1:, :] = padded_sum.cumsum(axis=0).cumsum(axis=1)

        summa = (
            matrix[kernel_size:, kernel_size:, :]
            - matrix[:-kernel_size, kernel_size:, :]
            - matrix[kernel_size:, :-kernel_size, :]
            + matrix[:-kernel_size, :-kernel_size, :]
        )

    result = summa / (kernel_size * kernel_size)
    return result.astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

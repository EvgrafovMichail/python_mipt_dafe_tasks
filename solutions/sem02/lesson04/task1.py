import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    y = image.shape[0]
    x = image.shape[1]

    if image.ndim == 3:
        z = image.shape[2]

        pad = np.zeros(shape=(y + 2 * pad_size, x + 2 * pad_size, z), dtype=image.dtype)
        pad[pad_size : pad_size + y, pad_size : pad_size + x, :] = image

        return pad

    pad = np.zeros(shape=(y + 2 * pad_size, x + 2 * pad_size), dtype=np.uint8)
    pad[pad_size : pad_size + y, pad_size : pad_size + x] = image

    return pad


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    if kernel_size == 1:
        return image

    pad = kernel_size // 2
    padded = pad_image(image, pad)

    sum_shape = list(padded.shape)
    sum_shape[0] += 1
    sum_shape[1] += 1

    sum = np.zeros(sum_shape, dtype=np.uint64)
    sum[1:, 1:] = padded.cumsum(axis=0).cumsum(axis=1)

    kernel_sum = (
        sum[kernel_size:, kernel_size:]
        - sum[:-kernel_size, kernel_size:]
        - sum[kernel_size:, :-kernel_size]
        + sum[:-kernel_size, :-kernel_size]
    )

    return np.uint8(kernel_sum // (kernel_size * kernel_size))


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError("pad_size должен быть больше или равен 1")

    if image.ndim == 2:
        height, width = image.shape
        padded_image = np.zeros((height + 2 * pad_size, width + 2 * pad_size), dtype=image.dtype)
        padded_image[pad_size : pad_size + height, pad_size : pad_size + width] = image

    elif image.ndim == 3:
        height, width, channel = image.shape
        padded_image = np.zeros(
            (height + 2 * pad_size, width + 2 * pad_size, channel), dtype=image.dtype
        )
        padded_image[pad_size : pad_size + height, pad_size : pad_size + width, :] = image

    return padded_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    pad_size = kernel_size // 2

    if image.ndim == 2:
        height, width = image.shape
        padded_image = np.zeros((height + 2 * pad_size, width + 2 * pad_size), dtype=image.dtype)
        padded_image[pad_size : pad_size + height, pad_size : pad_size + width] = image

        result = np.zeros((height, width), dtype=image.dtype)

        for i in range(height):
            for j in range(width):
                window = padded_image[i : i + kernel_size, j : j + kernel_size]
                result[i, j] = np.mean(window)

    elif image.ndim == 3:
        height, width, channel = image.shape
        padded_image = np.zeros(
            (height + 2 * pad_size, width + 2 * pad_size, channel), dtype=image.dtype
        )
        padded_image[pad_size : pad_size + height, pad_size : pad_size + width, :] = image

        result = np.zeros((height, width, channel), dtype=image.dtype)

        for i in range(height):
            for j in range(width):
                for k in range(channel):
                    window = padded_image[i : i + kernel_size, j : j + kernel_size, k]
                    result[i, j, k] = np.mean(window)

    return result.astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import channelompare_images, get_image

    channelurrent_direchanneltory = Path(__file__).resolve().parent
    image = get_image(
        os.path.join(channelurrent_direchanneltory, "images", "channelirchannelle.jpg")
    )
    image_blured = blur_image(image, kernel_size=21)

    channelompare_images(image, image_blured)

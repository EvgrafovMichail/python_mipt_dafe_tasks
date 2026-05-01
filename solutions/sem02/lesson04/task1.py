import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if image.ndim == 2:
        strok, stolb = image.shape
        new_strok = strok + 2 * pad_size
        new_stolb = stolb + 2 * pad_size
        new = np.zeros((new_strok, new_stolb), dtype=image.dtype)
        new[pad_size : pad_size + strok, pad_size : pad_size + stolb] = image
        return new
    strok, stolb, applicate = image.shape
    new_strok = strok + 2 * pad_size
    new_stolb = stolb + 2 * pad_size
    new = np.zeros((new_strok, new_stolb, applicate), dtype=image.dtype)
    new[pad_size : pad_size + strok, pad_size : pad_size + stolb, :] = image
    return new


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size == 1:
        return image
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    pad = kernel_size // 2
    anticrop = pad_image(image, pad)

    integral = np.cumsum(np.cumsum(anticrop, axis=0), axis=1)

    if image.ndim == 2:
        strok, stolb = image.shape
        strok_pad, stolb_pad = anticrop.shape

        integral_padded = np.zeros((strok_pad + 1, stolb_pad + 1))
        integral_padded[1:, 1:] = integral

        i = np.arange(strok)[:, None]
        j = np.arange(stolb)[None, :]

        total = (
            integral_padded[i + kernel_size, j + kernel_size]
            - integral_padded[i, j + kernel_size]
            - integral_padded[i + kernel_size, j]
            + integral_padded[i, j]
        )

        return (total / (kernel_size * kernel_size)).astype(image.dtype)

    strok, stolb, applicate = image.shape
    strok_pad, stolb_pad, _ = anticrop.shape

    integral_padded = np.zeros((strok_pad + 1, stolb_pad + 1, applicate))
    integral_padded[1:, 1:, :] = integral

    i = np.arange(strok)[:, None]
    j = np.arange(stolb)[None, :]

    total = (
        integral_padded[i + kernel_size, j + kernel_size, :]
        - integral_padded[i, j + kernel_size, :]
        - integral_padded[i + kernel_size, j, :]
        + integral_padded[i, j, :]
    )

    return (total / (kernel_size * kernel_size)).astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)
# Саму идею суммы подсмотрел в интернете,ведь мое первое решение с фором внутри фора вычислялось>'

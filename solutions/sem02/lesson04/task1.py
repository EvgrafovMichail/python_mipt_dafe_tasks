import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if np.ndim(image) == 2:
        hieght, length = image.shape
        new_height, new_length = hieght + pad_size * 2, length + pad_size * 2
        padded_image = np.zeros((new_height, new_length), dtype=image.dtype)
        padded_image[pad_size : pad_size + hieght, pad_size : pad_size + length] = image
    else:
        hieght, length, depth = image.shape
        new_height, new_length = hieght + pad_size * 2, length + pad_size * 2
        padded_image = np.zeros((new_height, new_length, depth), dtype=image.dtype)
        padded_image[pad_size : pad_size + hieght, pad_size : pad_size + length, ...] = image
    return padded_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError
    if kernel_size == 1:
        return image
    pad = kernel_size // 2
    padded_image = pad_image(image, pad)
    shifted = [
        padded_image[i : i + image.shape[0], j : j + image.shape[1], ...]
        for i in range(kernel_size)
        for j in range(kernel_size)
    ]
    # сверху сам массив а в глубину уходят элементы вокруг и потом мы просто ищем среднее вглубь
    blurred = np.mean(shifted, axis=0)

    return blurred.astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

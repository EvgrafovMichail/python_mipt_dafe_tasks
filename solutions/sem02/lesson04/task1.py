import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if image.ndim == 2:
        h, w = image.shape
        pad_image = np.zeros((h + 2 * pad_size, w + 2 * pad_size), dtype=image.dtype)
        pad_image[pad_size : pad_size + h, pad_size : pad_size + w] = image
    elif image.ndim == 3:
        h, w, c = image.shape
        pad_image = np.zeros((h + 2 * pad_size, w + 2 * pad_size, c), dtype=image.dtype)
        pad_image[pad_size : pad_size + h, pad_size : pad_size + w, :] = image
    else:
        raise ValueError
    return pad_image


def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError
    if kernel_size == 1:
        return image
    pad = kernel_size // 2
    padd_image = pad_image(image, pad)
    moved = [
        padd_image[i : i + image.shape[0], j : j + image.shape[1]]
        for i in range(kernel_size)
        for j in range(kernel_size)
    ]
    return np.round(np.mean(moved, axis=0)).astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

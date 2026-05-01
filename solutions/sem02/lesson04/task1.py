import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    elif image.ndim == 2:
        h, w = image.shape
        new_h = h + pad_size * 2
        new_w = w + pad_size * 2

        padded = np.zeros((new_h, new_w), dtype=image.dtype)
        padded[pad_size : pad_size + h, pad_size : pad_size + w] = image

    elif image.ndim == 3:
        h, w, c = image.shape
        new_h = h + pad_size * 2
        new_w = w + pad_size * 2

        padded = np.zeros((new_h, new_w, c), dtype=image.dtype)
        padded[pad_size : pad_size + h, pad_size : pad_size + w, :] = image

    return padded


def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError
    if kernel_size == 1:
        return image

    padding = kernel_size // 2
    padded = pad_image(image, padding)
    shifted = [
        padded[i : i + image.shape[0], j : j + image.shape[1], ...]
        for i in range(kernel_size)
        for j in range(kernel_size)
    ]
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

import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if image.ndim == 2:
        h, w = image.shape
        shape_with_frame = (h + 2 * pad_size, w + 2 * pad_size)
    if image.ndim == 3:
        h, w, s = image.shape
        shape_with_frame = (h + 2 * pad_size, w + 2 * pad_size, s)

    result = np.zeros(shape_with_frame, dtype=image.dtype)

    result[pad_size : pad_size + h, pad_size : pad_size + w] = image

    return result


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    if kernel_size == 1:
        return image.copy()

    pad_size = kernel_size // 2
    padded = pad_image(image, pad_size)
    if image.ndim == 2:
        h, w = image.shape
    if image.ndim == 3:
        h, w, _ = image.shape

    result = np.zeros(image.shape, dtype=float)

    for i in range(h):
        for j in range(w):
            window = padded[i : i + kernel_size, j : j + kernel_size]
            if image.ndim == 2:
                result[i, j] = np.mean(window)
            else:
                result[i, j] = np.mean(window, axis=(0, 1))
    return result.round().astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

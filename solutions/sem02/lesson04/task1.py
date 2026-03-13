import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if image.ndim == 2:
        height, width = image.shape
        res = np.zeros((height + 2 * pad_size, width + 2 * pad_size), dtype=image.dtype)
        res[pad_size : pad_size + height, pad_size : pad_size + width] = image
    elif image.ndim == 3:
        height, width, depth = image.shape
        res = np.zeros((height + 2 * pad_size, width + 2 * pad_size, depth), dtype=image.dtype)
        res[pad_size : pad_size + height, pad_size : pad_size + width, :] = image
    return res


def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError
    if kernel_size == 1:
        return image.copy()
    pad = kernel_size // 2
    padded = pad_image(image, pad)
    pref = np.zeros(tuple(s + 1 for s in padded.shape[:2]) + image.shape[2:])
    pref[1:, 1:] = padded.cumsum(0).cumsum(1)
    h, w = image.shape[:2]
    k = kernel_size
    window_sum = (
        pref[k : h + k, k : w + k] + pref[:h, :w] - pref[:h, k : w + k] - pref[k : h + k, :w]
    )
    return (window_sum / (k * k)).astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

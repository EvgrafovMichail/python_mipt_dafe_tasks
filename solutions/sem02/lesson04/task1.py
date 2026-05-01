import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if len(image.shape) == 2:
        n, m = list(image.shape)
        new_pad_n = n + 2 * pad_size
        new_pad_m = m + 2 * pad_size
        padded = np.zeros((new_pad_n, new_pad_m), dtype=image.dtype)
        padded[pad_size : pad_size + n, pad_size : pad_size + m] = image
    elif len(image.shape) == 3:
        n, m, c = list(image.shape)
        new_pad_n = n + 2 * pad_size
        new_pad_m = m + 2 * pad_size
        # new_pad_c = c + 2*pad_size
        padded = np.zeros((new_pad_n, new_pad_m, c), dtype=image.dtype)
        padded[pad_size : pad_size + n, pad_size : pad_size + m, :] = image
    else:
        return ValueError
    return padded


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    if kernel_size == 1:
        return image.copy()

    padded = pad_image(image, kernel_size // 2)
    if image.ndim == 2:
        n, m = image.shape
        res = np.zeros((n, m), dtype=np.float32)
        for i in range(n):
            for j in range(m):
                window = padded[i : i + kernel_size, j : j + kernel_size]
                res[i, j] = np.mean(window)
    elif image.ndim == 3:
        n, m, c = image.shape
        res = np.zeros((n, m, c), dtype=np.float32)
        for i in range(n):
            for j in range(m):
                window = padded[i : i + kernel_size, j : j + kernel_size, :]
                res[i, j, :] = np.mean(window, axis=(0, 1))
    else:
        raise ValueError

    return np.round(res).astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

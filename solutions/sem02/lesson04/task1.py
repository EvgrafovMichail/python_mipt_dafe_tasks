import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    h, w = image.shape[:2]
    new_h, new_w = h + pad_size * 2, w + pad_size * 2
    res_form = (new_h, new_w) if image.ndim == 2 else (new_h, new_w, image.shape[2])
    result = np.zeros(res_form, dtype=image.dtype)
    result[pad_size : pad_size + h, pad_size : pad_size + w, ...] = image
    return result


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    if kernel_size == 1:
        return image

    padded_image = pad_image(image, kernel_size // 2)
    h, w = image.shape[:2]
    windows = [
        padded_image[i : i + h, j : j + w, ...]
        for j in range(kernel_size)
        for i in range(kernel_size)
    ]
    return np.mean(windows, axis=0).astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

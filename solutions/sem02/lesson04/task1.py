import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    new_shape = (image.shape[0] + 2 * pad_size, image.shape[1] + 2 * pad_size) + image.shape[2:]
    result = np.zeros(new_shape, dtype=np.uint8)
    result[pad_size:-pad_size, pad_size:-pad_size] = image
    return result


def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    pad_size = kernel_size // 2

    if pad_size == 0:
        return image.copy()

    padded = pad_image(image, pad_size).astype(np.float64)
    cumsum = np.cumsum(np.cumsum(padded, axis=0), axis=1)

    c = np.zeros((padded.shape[0] + 1, padded.shape[1] + 1) + image.shape[2:], dtype=np.float64)
    c[1:, 1:] = cumsum
    cumsum = c

    H, W = image.shape[:2]
    k = kernel_size

    result = (
        cumsum[k : k + H, k : k + W]
        - cumsum[0:H, k : k + W]
        - cumsum[k : k + H, 0:W]
        + cumsum[0:H, 0:W]
    )

    return (result / k**2).astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

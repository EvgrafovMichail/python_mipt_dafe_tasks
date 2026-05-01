import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    height, width = image.shape[:2]
    height += 2 * pad_size
    width += 2 * pad_size

    img_new = np.zeros((height, width) + image.shape[2:], dtype=image.dtype)

    if len(image.shape) == 2:
        img_new[pad_size:-pad_size, pad_size:-pad_size] = image
    else:
        image.shape[2]
        img_new[pad_size:-pad_size, pad_size:-pad_size, :] = image

    return img_new


def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError
    if kernel_size == 1:
        return image

    pad_img = pad_image(image, kernel_size // 2)
    height, width = image.shape[:2]
    result = np.zeros((height, width) + image.shape[2:], dtype=image.dtype)

    for i in range(height):
        for j in range(width):
            region = pad_img[i : i + kernel_size, j : j + kernel_size]
            result[i, j] = region.mean(axis=(0, 1))

    return result


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=51)

    compare_images(image, image_blured)

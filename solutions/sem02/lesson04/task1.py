import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError("Pad size must be greater then 1")

    if image.ndim == 3:
        h, w, c = image.shape
        result_image = np.zeros((h + 2 * pad_size, w + 2 * pad_size, c), dtype=np.uint8)
        result_image[pad_size:-pad_size, pad_size:-pad_size, :] = image

    else:
        h, w = image.shape
        result_image = np.zeros((h + 2 * pad_size, w + 2 * pad_size), dtype=np.uint8)
        result_image[pad_size:-pad_size, pad_size:-pad_size] = image

    return result_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1:
        raise ValueError("Kernel size must pe greater then 1")

    if kernel_size == 1:
        return image

    if kernel_size % 2 == 0:
        raise ValueError("Kernel value must be odd")

    pad_size = kernel_size // 2
    image = pad_image(image, pad_size) / kernel_size**2

    np.cumsum(image, axis=1, out=image)
    values_horizontal_offset = np.zeros(shape=image.shape)
    values_horizontal_offset[::, kernel_size::] = image[::, :-kernel_size]
    image -= values_horizontal_offset

    np.cumsum(image, axis=0, out=image)
    values_vertical_offset = np.zeros(shape=image.shape)
    values_vertical_offset[kernel_size::, ::] = image[:-kernel_size, ::]
    image -= values_vertical_offset

    return np.array(image[pad_size * 2 : :, pad_size * 2 : :], dtype=np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

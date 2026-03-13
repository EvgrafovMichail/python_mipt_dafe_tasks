import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    expanded_shape = np.array(image.shape)

    expanded_shape[:2] += 2 * pad_size

    expanded_image = np.zeros(expanded_shape, dtype=image.dtype)

    expanded_image[pad_size:-pad_size, pad_size:-pad_size, ...] = image

    return expanded_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    if kernel_size == 1:
        return image

    padded_image = pad_image(image, kernel_size // 2)
    width, height = image.shape[:2]

    accum_matrix = np.zeros(image.shape, dtype=np.float64)

    for x_offset in range(kernel_size):
        for y_offset in range(kernel_size):
            accum_matrix += padded_image[
                x_offset : x_offset + width, y_offset : y_offset + height, ...
            ]

    return np.array(accum_matrix / kernel_size**2, dtype=np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    pad_image(image, 10)

    compare_images(image, image_blured)

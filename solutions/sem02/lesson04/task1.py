import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    new_shape = list(image.shape)

    new_shape[0] += 2 * pad_size
    new_shape[1] += 2 * pad_size

    ans = np.zeros(new_shape, dtype=image.dtype)

    ans[pad_size : image.shape[0] + pad_size, pad_size : image.shape[1] + pad_size] = image

    return ans


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    N = image.shape[0]
    M = image.shape[1]

    pad_size = kernel_size // 2
    if pad_size == 0:
        return image

    new_image = pad_image(image, pad_size)
    sum_in_window = np.zeros(image.shape, dtype=np.float64)

    for i in range(kernel_size):
        for j in range(kernel_size):
            sum_in_window += new_image[i : i + N, j : j + M]

    return (sum_in_window / kernel_size**2).astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

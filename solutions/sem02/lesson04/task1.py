import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if len(image.shape) != 2:
        padded = np.zeros(
            (image.shape[0] + pad_size * 2, image.shape[1] + pad_size * 2, image.shape[2]),
            dtype=image.dtype,
        )
        padded[pad_size:-pad_size, pad_size:-pad_size, :] = image
    else:
        padded = np.zeros(
            (image.shape[0] + pad_size * 2, image.shape[1] + pad_size * 2), dtype=image.dtype
        )
        padded[pad_size:-pad_size, pad_size:-pad_size] = image

    return padded


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:

    N = image.shape[0]
    M = image.shape[1]

    if kernel_size % 2 == 0:
        raise ValueError
    if kernel_size < 1:
        raise ValueError
    if kernel_size == 1:
        return image

    blurred_image = np.zeros_like(image)
    image = pad_image(image, kernel_size // 2)

    if len(image.shape) == 3:
        for i in range(N):
            for j in range(M):
                blurred_image[i, j] = np.mean(
                    image[i : i + kernel_size, j : j + kernel_size], axis=(0, 1)
                )
    else:
        for i in range(N):
            for j in range(M):
                blurred_image[i, j] = np.mean(image[i : i + kernel_size, j : j + kernel_size])

    return blurred_image


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

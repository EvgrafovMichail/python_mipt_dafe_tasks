import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        altitude, width = image.shape

        padd_image = np.zeros((altitude + 2 * pad_size, width + 2 * pad_size), dtype=image.dtype)

        padd_image[pad_size : pad_size + altitude, pad_size : pad_size + width] = image

    elif image.ndim == 3:
        altitude, width, depth = image.shape

        padd_image = np.zeros(
            (altitude + 2 * pad_size, width + 2 * pad_size, depth), dtype=image.dtype
        )

        padd_image[pad_size : pad_size + altitude, pad_size : pad_size + width, :] = image

    return padd_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:

    if ((kernel_size % 2 == 0) or (kernel_size < 1)):
        raise ValueError

    if kernel_size == 1:
        return image
    
    i = np.arange(image.shape[0])[:, np.newaxis]
    j = np.arange(image.shape[1])[np.newaxis, :]

    padd_image = pad_image(image, kernel_size // 2)
    csum_image_a0 = np.cumsum(padd_image, axis=0)
    csum_image = np.cumsum(csum_image_a0, axis=1)

    if image.ndim == 2:
        csum_image_edit = np.zeros((csum_image.shape[0] + 1, csum_image.shape[1] + 1))
        csum_image_edit[1:, 1:] = csum_image

    else:
        csum_image_edit = np.zeros(
            (csum_image.shape[0] + 1, csum_image.shape[1] + 1, csum_image.shape[2])
        )
        csum_image_edit[1:, 1:, :] = csum_image

    kernel_sums = (
        csum_image_edit[i + kernel_size, j + kernel_size]
        - csum_image_edit[i, j + kernel_size]
        - csum_image_edit[i + kernel_size, j]
        + csum_image_edit[i, j]
    )

    result = kernel_sums / (kernel_size * kernel_size)

    return np.array(result, dtype=np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

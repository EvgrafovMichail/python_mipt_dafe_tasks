import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        edited_image = np.zeros(
            shape=(image.shape[0] + 2 * pad_size, image.shape[1] + 2 * pad_size), dtype=np.uint8
        )
        edited_image[pad_size : image.shape[0] + pad_size, pad_size : image.shape[1] + pad_size] = (
            image
        )
    else:
        edited_image = np.zeros(
            shape=(image.shape[0] + 2 * pad_size, image.shape[1] + 2 * pad_size, image.shape[2]),
            dtype=np.uint8,
        )
        edited_image[
            pad_size : image.shape[0] + pad_size, pad_size : image.shape[1] + pad_size, :
        ] = image

    return edited_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    if kernel_size == 1:
        return image

    image_with_padding = pad_image(image, kernel_size // 2)
    image_cumsum = np.cumsum(np.cumsum(image_with_padding, axis=0), axis=1)

    i = np.arange(image.shape[0])[:, np.newaxis]
    j = np.arange(image.shape[1])[np.newaxis, :]

    if image.ndim == 2:
        edited_image_cumsum = np.zeros((image_cumsum.shape[0] + 1, image_cumsum.shape[1] + 1))
        edited_image_cumsum[1:, 1:] = image_cumsum

    else:
        edited_image_cumsum = np.zeros(
            (image_cumsum.shape[0] + 1, image_cumsum.shape[1] + 1, image_cumsum.shape[2])
        )
        edited_image_cumsum[1:, 1:, :] = image_cumsum

    sums_for_window = (
        edited_image_cumsum[i + kernel_size, j + kernel_size]
        - edited_image_cumsum[i, j + kernel_size]
        - edited_image_cumsum[i + kernel_size, j]
        + edited_image_cumsum[i, j]
    )

    result_image = sums_for_window / (kernel_size * kernel_size)

    return np.array(result_image, dtype=np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

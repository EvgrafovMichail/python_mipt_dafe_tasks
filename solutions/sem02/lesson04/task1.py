import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        height, weight = image.shape
        result = np.zeros((height + 2 * pad_size, weight + 2 * pad_size), dtype=image.dtype)
        result[pad_size : height + pad_size, pad_size : weight + pad_size] = image

    elif image.ndim == 3:
        height, weight, c = image.shape
        result = np.zeros((height + 2 * pad_size, weight + 2 * pad_size, c), dtype=image.dtype)
        result[pad_size : height + pad_size, pad_size : weight + pad_size, :] = image

    return result


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError
    if kernel_size == 1:
        return image
    pad = kernel_size // 2
    h, w = image.shape[0], image.shape[1]
    ks = kernel_size
    ks_area = ks * ks
    image_with_padding = pad_image(image, pad)
    image_cumsum = np.cumsum(np.cumsum(image_with_padding, axis=0), axis=1)
    i = np.arange(h)[:, np.newaxis]
    j = np.arange(w)[np.newaxis, :]
    if image.ndim == 2:
        edited_image_cumsum = np.zeros((image_cumsum.shape[0] + 1, image_cumsum.shape[1] + 1))
        edited_image_cumsum[1:, 1:] = image_cumsum
        sums_for_window = (
            edited_image_cumsum[i + ks, j + ks]
            - edited_image_cumsum[i, j + ks]
            - edited_image_cumsum[i + ks, j]
            + edited_image_cumsum[i, j]
        )

    else:
        c = image.shape[2]
        edited_image_cumsum = np.zeros((image_cumsum.shape[0] + 1, image_cumsum.shape[1] + 1, c))
        edited_image_cumsum[1:, 1:, :] = image_cumsum

        sums_for_window = (
            edited_image_cumsum[i + ks, j + ks, :]
            - edited_image_cumsum[i, j + ks, :]
            - edited_image_cumsum[i + ks, j, :]
            + edited_image_cumsum[i, j, :]
        )

    result_image = sums_for_window / ks_area
    return result_image.astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

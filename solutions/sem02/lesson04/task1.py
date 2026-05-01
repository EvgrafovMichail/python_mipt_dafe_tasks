import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError("pad_size must be at least 1")

    height, width = image.shape[:2]
    new_height = height + 2 * pad_size
    new_width = width + 2 * pad_size

    if image.ndim == 2:
        new_image = np.zeros((new_height, new_width), dtype=image.dtype)
        new_image[pad_size : pad_size + height, pad_size : pad_size + width] = image

    elif image.ndim == 3:
        new_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)
        new_image[pad_size : pad_size + height, pad_size : pad_size + width, :] = image

    else:
        raise ValueError("image dimensions must be 2 or 3")

    return new_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1:
        raise ValueError("kernel size must be at least 1")
    elif kernel_size % 2 == 0:
        raise ValueError("kernel size must be odd")

    padded_image = pad_image(image, kernel_size // 2)
    window_area = kernel_size**2
    k = kernel_size

    if image.ndim == 2:
        height, width = image.shape
        cumsum_image = np.zeros(
            (padded_image.shape[0] + 1, padded_image.shape[1] + 1), dtype=np.uint64
        )
        cumsum_image = padded_image.cumsum(axis=0).cumsum(axis=1)

        i, j = np.indices((height, width))

        extra_sum = cumsum_image[i, j + k - 1] + cumsum_image[i + k - 1, j] - cumsum_image[i, j]

        result = (cumsum_image[i + k - 1, j + k - 1] - extra_sum) / window_area

        result = np.round(result).astype(np.uint8)

    elif image.ndim == 3:
        height, width, colors = image.shape
        result = np.zeros((height, width, colors), dtype=np.float64)

        for c in range(colors):
            color = padded_image[:, :, c]
            cumsum_image = np.zeros((color.shape[0] + 1, color.shape[1] + 1), dtype=np.uint64)
            cumsum_image = color.cumsum(axis=0).cumsum(axis=1)

            i, j = np.indices((height, width))

            extra_window_sum = (
                cumsum_image[i, j + k - 1] + cumsum_image[i + k - 1, j] - cumsum_image[i, j]
            )

            window_sum = cumsum_image[i + k - 1, j + k - 1] - extra_window_sum

            result[:, :, c] = window_sum / window_area

            result = np.round(result).astype(np.uint8)

    else:
        raise ValueError("image dimensions must be 2 or 3")

    return result


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

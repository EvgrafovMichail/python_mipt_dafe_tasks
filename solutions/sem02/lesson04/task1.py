import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if image.ndim == 2:
        rows_count, columns_count = image.shape
        new_image = np.zeros(
            (rows_count + 2 * pad_size, columns_count + 2 * pad_size), dtype=image.dtype
        )
        new_image[pad_size : pad_size + rows_count, pad_size : pad_size + columns_count] = image
    else:
        rows_count, columns_count, layer_count = image.shape
        new_image = np.zeros(
            (rows_count + 2 * pad_size, columns_count + 2 * pad_size, layer_count),
            dtype=image.dtype,
        )
        new_image[pad_size : pad_size + rows_count, pad_size : pad_size + columns_count, :] = image
    return new_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError
    if kernel_size == 1:
        return image

    pad_size = int((kernel_size - 1) / 2)
    kernel_area = kernel_size**2
    if image.ndim == 2:
        rows_count, column_count = image.shape
        new_image = pad_image(image, pad_size)
        result = np.zeros((rows_count, column_count), dtype=image.dtype)

        for i in range(rows_count):
            for j in range(column_count):
                window = new_image[i : i + kernel_size, j : j + kernel_size]
                result[i, j] = np.sum(window, dtype=np.int32) // kernel_area
        return result

    else:
        rows_count, column_count, layer_count = image.shape
        new_image = pad_image(image, pad_size)
        result = np.zeros((rows_count, column_count, layer_count), dtype=image.dtype)

        for i in range(rows_count):
            for j in range(column_count):
                window = new_image[i : i + kernel_size, j : j + kernel_size, :]
                result[i, j, :] = np.sum(window, axis=(0, 1), dtype=np.int32) // kernel_area
        return result


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

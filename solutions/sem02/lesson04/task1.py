import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:

    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        padded = np.zeros(np.array(image.shape) + 2 * pad_size, dtype=np.uint8)

    if image.ndim == 3:
        padded = np.zeros(
            (image.shape[0] + 2 * pad_size, image.shape[1] + 2 * pad_size, image.shape[2]),
            dtype=np.uint8,
        )

    padded[pad_size : padded.shape[0] - pad_size, pad_size : padded.shape[1] - pad_size] = image

    return padded


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:

    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    padded = pad_image(image, kernel_size // 2 + 1)
    column_cumsum = np.cumsum(padded, axis=0, dtype=np.uint64)
    block_column_sum = (
        column_cumsum[kernel_size : column_cumsum.shape[0] - 1]
        - column_cumsum[: column_cumsum.shape[0] - kernel_size - 1]
    )
    row_cumsum = np.cumsum(block_column_sum, axis=1, dtype=np.uint64)
    row_cumsum[:, kernel_size : row_cumsum.shape[1] - 1] -= row_cumsum[
        :, : row_cumsum.shape[1] - kernel_size - 1
    ]
    blur = row_cumsum[:, kernel_size : row_cumsum.shape[1] - 1] // kernel_size**2

    return np.array(blur, dtype=np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

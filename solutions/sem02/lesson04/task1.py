import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    frame_shape = np.array(image.shape)
    frame_shape[:2] += 2 * pad_size

    frame = np.zeros(frame_shape, dtype=image.dtype)
    frame[pad_size:-pad_size, pad_size:-pad_size] = image
    return frame


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    blur = pad_image(image, kernel_size // 2 + 1)
    prefix_summ = blur.cumsum(axis=0).cumsum(axis=1)

    cols_index = np.arange(1, blur.shape[0] - kernel_size + 1)[..., np.newaxis]
    lines_index = np.arange(1, blur.shape[1] - kernel_size + 1)[np.newaxis, ...]

    k = kernel_size - 1
    slide_sum = (
        prefix_summ[cols_index - 1, lines_index - 1]
        + prefix_summ[cols_index + k, lines_index + k]
        - prefix_summ[cols_index + k, lines_index - 1]
        - prefix_summ[cols_index - 1, lines_index + k]
    )

    result = slide_sum // kernel_size**2

    return np.array(result[:-1, :-1], dtype=image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

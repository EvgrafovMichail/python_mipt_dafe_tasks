import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    new_sh = list(image.shape)
    new_sh[0] += 2 * pad_size
    new_sh[1] += 2 * pad_size

    with_pad = np.zeros(new_sh, dtype=image.dtype)

    with_pad[
        pad_size:-pad_size,
        pad_size:-pad_size,
    ] = image
    return with_pad


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    if kernel_size == 1:
        return image

    pad_size = kernel_size // 2
    with_pad = pad_image(image, pad_size)
    h, w = image.shape[:2]

    csy = np.cumsum(with_pad, axis=0)
    y_sum = np.zeros((h, with_pad.shape[1]) + image.shape[2:])

    y_sum[0,] = csy[kernel_size - 1,]
    y_sum[1:,] = csy[kernel_size:,] - csy[:-kernel_size,]

    csx = np.cumsum(y_sum, axis=1)
    xy_sum = np.zeros((h, w) + image.shape[2:])

    xy_sum[
        :,
        0,
    ] = csx[
        :,
        kernel_size - 1,
    ]
    xy_sum[
        :,
        1:,
    ] = (
        csx[
            :,
            kernel_size:,
        ]
        - csx[
            :,
            :-kernel_size,
        ]
    )

    blur_im = xy_sum / (kernel_size**2)
    return blur_im.astype(image.dtype)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

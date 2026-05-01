import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        height, width = image.shape

        padded_image = np.zeros((height + 2 * pad_size, width + 2 * pad_size), dtype=np.uint8)
        padded_image[pad_size:-pad_size, pad_size:-pad_size] = image
    else:
        height, width, depth = image.shape

        padded_image = np.zeros(
            (height + 2 * pad_size, width + 2 * pad_size, depth), dtype=np.uint8
        )
        padded_image[pad_size : pad_size + height, pad_size : pad_size + width, :] = image

    return padded_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    if kernel_size == 1:
        return image

    pad_size = kernel_size // 2
    image = pad_image(image, pad_size) / kernel_size**2

    np.cumsum(image, axis=0, out=image)
    vert = np.zeros(image.shape)
    vert[kernel_size:, :] = image[:-kernel_size, :]
    image -= vert

    np.cumsum(image, axis=1, out=image)
    horiz = np.zeros(image.shape)
    horiz[:, kernel_size:] = image[:, :-kernel_size]
    image -= horiz

    return np.array(image[pad_size * 2 : :, pad_size * 2 : :], dtype=np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

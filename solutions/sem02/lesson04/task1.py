import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError("размер паддинга должен быть не меньше 1")

    if image.ndim == 2:
        image = np.concatenate(
            (
                np.zeros((image.shape[0], pad_size), dtype=image.dtype),
                image,
                np.zeros((image.shape[0], pad_size), dtype=image.dtype),
            ),
            axis=1,
        )
        image = np.concatenate(
            (
                np.zeros((pad_size, image.shape[1]), dtype=image.dtype),
                image,
                np.zeros((pad_size, image.shape[1]), dtype=image.dtype),
            ),
            axis=0,
        )

    if image.ndim == 3:
        image = np.concatenate(
            (
                np.zeros((pad_size, image.shape[1], image.shape[2]), dtype=image.dtype),
                image,
                np.zeros((pad_size, image.shape[1], image.shape[2]), dtype=image.dtype),
            ),
            axis=0,
        )
        image = np.concatenate(
            (
                np.zeros((image.shape[0], pad_size, image.shape[2]), dtype=image.dtype),
                image,
                np.zeros((image.shape[0], pad_size, image.shape[2]), dtype=image.dtype),
            ),
            axis=1,
        )
    return image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1:
        raise ValueError("размер ядра должен быть не меньше 1")

    if kernel_size == 1:
        return image

    if kernel_size % 2 == 0:
        raise ValueError("размер ядра должен быть нечетным")

    pad_size = kernel_size // 2
    image_blured = image.copy()
    image = pad_image(image, pad_size)

    if image.ndim == 2:
        for i in range(pad_size, image.shape[0] - pad_size):
            for j in range(pad_size, image.shape[1] - pad_size):
                image_blured[i - pad_size, j - pad_size] = np.sum(
                    image[i - pad_size : i + pad_size + 1, j - pad_size : j + pad_size + 1]
                ) / (kernel_size**2)

    if image.ndim == 3:
        for i in range(pad_size, image.shape[0] - pad_size):
            for j in range(pad_size, image.shape[1] - pad_size):
                for k in range(0, image.shape[2]):
                    image_blured[i - pad_size, j - pad_size, k] = np.sum(
                        image[i - pad_size : i + pad_size + 1, j - pad_size : j + pad_size + 1, k]
                    ) / (kernel_size**2)

    image = image_blured.copy()
    return image


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

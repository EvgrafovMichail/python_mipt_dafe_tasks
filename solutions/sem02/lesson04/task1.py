import numpy as np

MIN_PAD_SIZE = 1
MIN_KERNEL_SIZE = 1


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < MIN_PAD_SIZE:
        raise ValueError
    shp = image.shape
    if len(shp) == 2:
        new_shp = (shp[0] + 2 * pad_size, shp[1] + 2 * pad_size)
        padded_image = np.zeros(shape=new_shp, dtype=image.dtype)
        for i in range(shp[0]):
            for j in range(shp[1]):
                padded_image[i + pad_size, j + pad_size] = image[i, j]
    else:
        new_shp = (shp[0] + 2 * pad_size, shp[1] + 2 * pad_size, shp[2])
        padded_image = np.zeros(shape=new_shp, dtype=image.dtype)
        for i in range(shp[0]):
            for j in range(shp[1]):
                for k in range(shp[2]):
                    padded_image[i + pad_size, j + pad_size, k] = image[i, j, k]
    return padded_image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if (kernel_size < MIN_KERNEL_SIZE) or (kernel_size % 2 == 0):
        raise ValueError
    if kernel_size == 1:
        return image
    shp = image.shape
    pad = kernel_size // 2
    image = pad_image(image, pad)
    blured_image = np.zeros(shape=shp, dtype=image.dtype)
    if len(shp) == 2:
        for i in range(shp[0]):
            for j in range(shp[1]):
                kemel = image[i : i + kernel_size, j : j + kernel_size]
                blured_image[i, j] = np.mean(kemel)
    else:
        for i in range(shp[0]):
            for j in range(shp[1]):
                kemel = image[i : i + kernel_size, j : j + kernel_size, :]
                blured_image[i, j, :] = np.mean(kemel, axis=(0, 1))
    return blured_image


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

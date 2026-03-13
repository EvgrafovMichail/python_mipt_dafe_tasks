import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        height = image.shape[0]
        lenght = image.shape[1]
        array = np.zeros((height + 2 * pad_size, lenght + 2 * pad_size), dtype=np.uint8)
        array[pad_size : height + pad_size, pad_size : lenght + pad_size] = image

    elif image.ndim == 3:
        height = image.shape[0]
        lenght = image.shape[1]
        _3d = image.shape[2]
        array = np.zeros((height + 2 * pad_size, lenght + 2 * pad_size, _3d), dtype=np.uint8)
        array[pad_size : height + pad_size, pad_size : lenght + pad_size, :] = image

    return array


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError
    if kernel_size == 1:
        return image.copy()

    if image.ndim == 2:
        height, lenght = image.shape[0], image.shape[1]
        res = np.zeros((height, lenght), dtype=image.dtype)

        new = pad_image(image, kernel_size // 2)

        for i in range(height):
            for j in range(lenght):
                sl = new[i : i + kernel_size, j : j + kernel_size]
                res[i, j] = int(np.mean(sl))

        return res

    elif image.ndim == 3:
        height, lenght, _3d = image.shape[0], image.shape[1], image.shape[2]
        res = np.zeros((height, lenght, _3d), dtype=np.uint8)

        new = pad_image(image, kernel_size // 2)

        for i in range(height):
            for j in range(lenght):
                for k in range(_3d):
                    sl = new[i : i + kernel_size, j : j + kernel_size, k]
                    res[i, j, k] = int(np.mean(sl))

        return res


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

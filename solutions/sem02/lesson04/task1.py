import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    if image.ndim == 2:
        height = image.shape[0]
        lenght = image.shape[1]

        with_padding = np.zeros((height + 2 * pad_size, lenght + 2 * pad_size), dtype=np.uint8)
        with_padding[pad_size : height + pad_size, pad_size : lenght + pad_size] = image

    elif image.ndim == 3:
        height = image.shape[0]
        lenght = image.shape[1]
        width = image.shape[2]

        with_padding = np.zeros(
            (height + 2 * pad_size, lenght + 2 * pad_size, width), dtype=np.uint8
        )
        with_padding[pad_size : height + pad_size, pad_size : lenght + pad_size, :] = image

    return with_padding


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size % 2 == 0 or kernel_size < 1:
        raise ValueError

    if kernel_size == 1:
        return image

    if image.ndim == 2:
        height = image.shape[0]
        lenght = image.shape[1]
        answer = np.zeros((height, lenght), dtype=image.dtype)

        new_image = pad_image(image, kernel_size // 2)

        for i in range(height):
            for j in range(lenght):
                window = new_image[i : i + kernel_size, j : j + kernel_size]
                answer[i, j] = int(np.mean(window))

        return answer

    elif image.ndim == 3:
        height, lenght, width = image.shape[0], image.shape[1], image.shape[2]
        answer = np.zeros((height, lenght, width), dtype=np.uint8)

        new_image = pad_image(image, kernel_size // 2)

        for i in range(height):
            for j in range(lenght):
                for k in range(width):
                    window = new_image[i : i + kernel_size, j : j + kernel_size, k]
                    answer[i, j, k] = int(np.mean(window))

        return answer


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

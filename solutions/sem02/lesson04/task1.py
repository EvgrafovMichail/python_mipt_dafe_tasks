import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError()
    if len(image.shape) == 2:
        n_image = np.zeros((image.shape[0] + 2 * pad_size, image.shape[1] + 2 * pad_size), dtype=np.uint8)
        n_image[pad_size:image.shape[0] + pad_size, pad_size:image.shape[1] + pad_size] = image
    elif len(image.shape) == 3:
        n_image = np.zeros((image.shape[0] + 2 * pad_size, image.shape[1] + 2 * pad_size, image.shape[2] ), dtype=np.uint8)
        n_image[pad_size:image.shape[0] + pad_size, pad_size:image.shape[1] + pad_size, :] = image
    return n_image

def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError()
    try:
        new_image = pad_image(image, kernel_size//2)
    except ValueError:
        new_image = image
    res = np.zeros(image.shape)
    if len(image.shape) == 2:
        for i in range(kernel_size):
            for j in range(kernel_size):
                res += new_image[i:image.shape[0] + i, j:image.shape[1] + j] / (kernel_size**2)

    elif len(image.shape) == 3:
        for i in range(kernel_size):
            for j in range(kernel_size):
                res += new_image[i:image.shape[0] + i, j:image.shape[1] + j, :] / (kernel_size ** 2)

    res = np.array(res, dtype=np.uint8)
    return res
if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

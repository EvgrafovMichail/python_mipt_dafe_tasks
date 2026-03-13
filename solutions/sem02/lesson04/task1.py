import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    # ваш код
    return image


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    # ваш код
    return image


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

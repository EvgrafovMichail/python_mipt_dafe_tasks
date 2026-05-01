import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    
    if len(image.shape) == 2:
        length, width = image.shape[0], image.shape[1]
        new_image = np.zeros((length + pad_size*2, width + pad_size*2), dtype=image.dtype)
        new_image[pad_size:pad_size + length, pad_size:pad_size + width] = image

    else:
        length, width, color = image.shape[0], image.shape[1], image.shape[2]
        new_image = np.zeros((length + pad_size*2, width + pad_size*2, color), dtype=image.dtype)
        new_image[pad_size:pad_size + length, pad_size:pad_size + width, :] = image

    return new_image






def blur_image(image: np.ndarray, kernel_size: int,) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError
    
    if len(image.shape) == 2:
        pad_size = kernel_size // 2
        new_image = pad_image(image, pad_size)
        length, width = image.shape[0], image.shape[1]
        result = np.zeros((length, width), dtype=np.uint8)

        for i in range(length):
            for j in range(width):
                window = new_image[i:i + kernel_size, j:j + kernel_size]
                result[i, j] = np.mean(window)
                
    else:
        pad_size = kernel_size // 2
        new_image = pad_image(image, pad_size)
        length, width, color = image.shape[0], image.shape[1], image.shape[2]
        result = np.zeros((length, width, color), dtype=np.uint8)

        for i in range(length):
            for j in range(width):
                window = new_image[i:i + kernel_size, j:j + kernel_size, :]
                result[i, j, :] = np.mean(window)

    return result 


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

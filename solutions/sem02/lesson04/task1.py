import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    shape = image.shape
    shape = list(shape)

    if len(shape) == 2:
        for i in range(len(shape)):
            shape[i] += 2 * pad_size
    else:
        shape[0] += 2 * pad_size
        shape[1] += 2 * pad_size

    border_array = np.ones(shape, dtype=image.dtype)

    if len(shape) == 2:
        border_array[:pad_size, :] = 0
        border_array[-pad_size:, :] = 0
        border_array[:, :pad_size] = 0
        border_array[:, -pad_size:] = 0
    else:
        border_array[:pad_size, :, :] = 0
        border_array[-pad_size:, :, :] = 0
        border_array[:, :pad_size, :] = 0
        border_array[:, -pad_size:, :] = 0

    idx = border_array != 0
    border_array[idx] = image.reshape(-1)

    return border_array


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    border = kernel_size // 2
    if border == 0:
        return image.astype(np.uint8)

    if image.ndim == 3:
        first, second, third = image.shape
        out = np.zeros((first, second, third), dtype=np.uint8)
        for i in range(third):
            out[:, :, i] = blur_image(image[:, :, i], kernel_size)
        return out

    first, second = image.shape
    image_new = pad_image(image, border)
    new_first, new_second = image_new.shape

    flat = image_new.flatten()

    centers = []
    for i in range(border, border + first):
        for j in range(border, border + second):
            centers.append(i * new_second + j)
    centers = np.array(centers)

    remotes = []
    for i in range(-border, border + 1):
        for j in range(-border, border + 1):
            remotes.append(i * new_second + j)
    remotes = np.array(remotes)

    n_idx = centers[:, None] + remotes[None, :]
    n_vals = flat[n_idx]
    means = n_vals.mean(axis=1)

    blur_flat = flat.astype(float)
    blur_flat[centers] = means

    blur_new = blur_flat.reshape(new_first, new_second)
    final_image = blur_new[border : border + first, border : border + second]

    return np.round(final_image).astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

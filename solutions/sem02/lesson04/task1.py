import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError
    if len(image.shape) == 2:
        padded_image = np.zeros(
            shape=(image.shape[0] + 2 * pad_size, image.shape[1] + 2 * pad_size), dtype=image.dtype
        )
        padded_image[pad_size : pad_size + image.shape[0], pad_size : pad_size + image.shape[1]] = (
            image
        )
    else:
        padded_image = np.zeros(
            shape=(image.shape[0] + 2 * pad_size, image.shape[1] + 2 * pad_size, image.shape[2]),
            dtype=image.dtype,
        )
        padded_image[
            pad_size : pad_size + image.shape[0], pad_size : pad_size + image.shape[1], :
        ] = image
    return padded_image


def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    if kernel_size == 1:
        return image.copy()

    h = kernel_size // 2

    if image.ndim == 2:
        padded = pad_image(image, h)

        sums = np.cumsum(np.cumsum(padded, axis=1), axis=0).astype(np.int64)

        N, M = image.shape

        i1 = np.arange(N).reshape(N, 1)
        j1 = np.arange(M).reshape(1, M)
        i2 = i1 + kernel_size - 1
        j2 = j1 + kernel_size - 1

        I1 = i1 * np.ones((1, M), dtype=int)
        J1 = j1 * np.ones((N, 1), dtype=int)
        I2 = i2 * np.ones((1, M), dtype=int)
        J2 = j2 * np.ones((N, 1), dtype=int)

        sum1 = sums[I2, J2]

        sum2 = np.zeros(shape=sum1.shape, dtype=np.int64)
        mask_x = I1 > 0
        sum2[mask_x] = sums[I1[mask_x] - 1, J2[mask_x]]

        sum3 = np.zeros(shape=sum1.shape, dtype=np.int64)
        mask_y = J1 > 0
        sum3[mask_y] = sums[I2[mask_y], J1[mask_y] - 1]

        sum4 = np.zeros(shape=sum1.shape, dtype=np.int64)
        mask_xy = mask_x & mask_y
        sum4[mask_xy] = sums[I1[mask_xy] - 1, J1[mask_xy] - 1]

        sums = sum1 - sum2 - sum3 + sum4
        area = kernel_size * kernel_size
        result = ((sums + area // 2) // area).astype(np.uint8)

    else:
        padded = pad_image(image, h)
        N, M, L = image.shape

        result = np.zeros((N, M, L), dtype=np.uint8)
        area = kernel_size * kernel_size
        half_area = area // 2

        for c in range(L):
            sums = np.cumsum(np.cumsum(padded[:, :, c], axis=1), axis=0).astype(np.int64)

            i1 = np.arange(N).reshape(N, 1)
            j1 = np.arange(M).reshape(1, M)
            i2 = i1 + kernel_size - 1
            j2 = j1 + kernel_size - 1

            I1 = i1 * np.ones((1, M), dtype=int)
            J1 = j1 * np.ones((N, 1), dtype=int)
            I2 = i2 * np.ones((1, M), dtype=int)
            J2 = j2 * np.ones((N, 1), dtype=int)

            sum1 = sums[I2, J2]

            sum2 = np.zeros(shape=sum1.shape, dtype=np.int64)
            mask_x = I1 > 0
            sum2[mask_x] = sums[I1[mask_x] - 1, J2[mask_x]]

            sum3 = np.zeros(shape=sum1.shape, dtype=np.int64)
            mask_y = J1 > 0
            sum3[mask_y] = sums[I2[mask_y], J1[mask_y] - 1]

            sum4 = np.zeros(shape=sum1.shape, dtype=np.int64)
            mask_xy = mask_x & mask_y
            sum4[mask_xy] = sums[I1[mask_xy] - 1, J1[mask_xy] - 1]

            sums = sum1 - sum2 - sum3 + sum4
            result[:, :, c] = ((sums + half_area) // area).astype(np.uint8)

    return result


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

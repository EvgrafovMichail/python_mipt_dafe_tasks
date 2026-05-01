import numpy as np

MINIMAL_THRESHOLD = 1


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < MINIMAL_THRESHOLD:
        raise ValueError("threshold must be positive")
    all_possibals = np.full(shape=256, fill_value=-42, dtype=int)
    image = image.reshape(-1)
    for pixel in range(0, 256):
        if pixel in image:
            all_possibals[pixel] = 0
        mask = (image > pixel) & ((image - pixel) < threshold) | (image <= pixel) & (
            (pixel - image) < threshold
        )
        all_possibals[pixel] += np.sum(mask)
    return (
        np.uint8(np.argmax(all_possibals)),
        all_possibals[np.argmax(all_possibals)] / image.size,
    )

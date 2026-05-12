import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    image.flatten()

    colours, counts = np.unique(image, return_counts=True)

    maxcolor = colours[0]
    maxcount = 0

    for color in colours:
        mask = np.abs(colours.astype(int) - int(color)) < threshold
        count = np.sum(counts[mask])

        if count > maxcount:
            maxcount = count
            maxcolor = color

    return np.uint8(maxcolor), maxcount / image.size * 100

import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    # ваш код
    if threshold < 1:
        raise ValueError("threshold must be positive")
    image_uniq, image_count = np.unique(image, return_counts=True)
    boollist = np.zeros(256)
    boollist[image_uniq] = image_count
    maxsum = 0
    for pix in image_uniq:
        intpix = int(pix)
        le = max(0, intpix - threshold + 1)
        r = min(255, intpix + threshold - 1)
        mysum = np.sum(boollist[le : r + 1])
        if mysum > maxsum:
            rasp = pix
            maxsum = mysum
    return rasp, maxsum / image.size * 100

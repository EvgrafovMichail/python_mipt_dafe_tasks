import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    image = np.array(image, dtype=np.int64)
    unique_elems, counts = np.unique(image, return_counts=True)
    substracts = abs(unique_elems[..., np.newaxis] - unique_elems)
    similar = substracts < threshold
    similar_cnt = (similar * counts).sum(axis=1)

    indx_max = np.argmax(similar_cnt)
    color = unique_elems[indx_max]
    percentage = similar_cnt[indx_max] / image.size

    return np.uint8(color), float(percentage)


a = np.array([[100, 100, 100, 102, 104, 106, 108]])
print()

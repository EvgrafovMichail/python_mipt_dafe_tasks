import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    flatten_image = image.astype(np.uint8).flatten()
    unique_colors, unique_counts = np.unique(flatten_image, return_counts=True)

    color_counts = np.zeros(256, dtype=np.int64)
    color_counts[unique_colors] = unique_counts

    prefix_sums = np.zeros(257, dtype=np.int64)
    prefix_sums[1:] = np.cumsum(color_counts)

    colors = np.arange(256)
    left = np.max(
        np.array([colors - threshold + 1, np.zeros_like(colors)]),
        axis=0,
    )
    right = np.min(
        np.array([colors + threshold - 1, np.full_like(colors, 255)]),
        axis=0,
    )
    pix_cnt = prefix_sums[right + 1] - prefix_sums[left]

    pix_cnt[color_counts == 0] = -1

    main_color = int(np.argmax(pix_cnt))
    percent = pix_cnt[main_color] / flatten_image.size * 100

    return np.uint8(main_color), float(percent)

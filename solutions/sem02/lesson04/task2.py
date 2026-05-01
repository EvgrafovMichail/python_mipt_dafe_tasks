import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    
    if threshold < 1:
        raise ValueError("threshold must be positive")

    counts = np.zeros(256, dtype=np.int64)
    for pixel in image.ravel():
        counts[pixel] += 1
    
    max_pixels = 0
    best_color = 0

    for current_color in range(256):
        if counts[current_color] > 0:
            left = max(0, current_color - (threshold - 1))
            right = min(255, current_color + (threshold - 1))
            cur_sum = np.sum(counts[left:right + 1])

            if cur_sum > max_pixels:
                max_pixels = cur_sum
                best_color = current_color

            elif cur_sum == max_pixels:
                if counts[current_color] > counts[best_color]:
                    best_color = current_color
    
    total_pixels = image.size
    percent = (max_pixels / total_pixels) * 100
    
    return np.uint8(best_color), float(percent)

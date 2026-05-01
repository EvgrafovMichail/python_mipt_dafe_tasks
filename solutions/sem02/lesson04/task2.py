import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    
    if threshold < 1:
        raise ValueError
    
    pixels = image.flatten()
    pixels.sort()

    current_group_start = 0
    current_group_size = 1
    best_group_start = 0
    best_group_size = 1
    
    for i in range(1, len(pixels)):
        if pixels[i] - pixels[current_group_start] < threshold:
            current_group_size += 1
        else:
            if current_group_size > best_group_size:
                best_group_size = current_group_size
                best_group_start = current_group_start
            current_group_start = i
            current_group_size = 1
    
    if current_group_size > best_group_size:
        best_group_size = current_group_size
        best_group_start = current_group_start
    
    total_pixels = len(pixels)
    percentage = (best_group_size / total_pixels) * 100

    return (pixels[best_group_start], percentage)
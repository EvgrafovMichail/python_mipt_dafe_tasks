import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if (np.size(ordinates)) < 3:
        raise ValueError

    all_numbers = np.arange(1, len(ordinates) - 1)

    moved_left = ordinates[:-2]
    moved_right = ordinates[2:]
    check_area = ordinates[1:-1]
    max_mask = (check_area > moved_left) & (check_area > moved_right)
    min_mask = (check_area < moved_left) & (check_area < moved_right)
    return (all_numbers[min_mask], all_numbers[max_mask])

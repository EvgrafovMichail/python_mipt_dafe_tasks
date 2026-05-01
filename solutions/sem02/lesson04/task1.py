import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:

    if pad_size < 1:
        raise ValueError
    
    if image.ndim == 2:

        h, w = image.shape
        
        padded = np.zeros((h + 2*pad_size, w + 2*pad_size), dtype=image.dtype)
        padded[pad_size:pad_size+h, pad_size:pad_size+w] = image
        
    elif image.ndim == 3:

        h, w, c = image.shape
        
        padded = np.zeros((h + 2*pad_size, w + 2*pad_size, c), dtype=image.dtype)
        padded[pad_size:pad_size+h, pad_size:pad_size+w, :] = image
        
    else:
        raise ValueError
    
    return padded


def blur_image(
    image: np.ndarray,
    kernel_size: int,
) -> np.ndarray:
    
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError
    
    pad = kernel_size // 2
    k = kernel_size
    
    padded = pad_image(image.astype(np.float64), pad)
    integral = np.cumsum(np.cumsum(padded, axis=0), axis=1)
    
    if image.ndim == 2:
        h, w = image.shape
        
        sums = (integral[k:, k:] - integral[:-k, k:] - 
                integral[k:, :-k] + integral[:-k, :-k])
        
        result = sums[:h, :w] / (k * k)
        
    else:
        h, w, c = image.shape
        result = np.zeros((h, w, c), dtype=np.float64)
        
        for ch in range(c):
            sums = (integral[k:, k:, ch] - integral[:-k, k:, ch] - 
                    integral[k:, :-k, ch] + integral[:-k, :-k, ch])
            result[:, :, ch] = sums[:h, :w] / (k * k)
    
    return np.clip(result, 0, 255).astype(np.uint8)


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def get_image(path_to_image: str) -> np.ndarray:
    image = cv.imread(path_to_image)
    return cv.cvtColor(image, code=cv.COLOR_BGR2RGB)


def compare_images(image1: np.ndarray, image2: np.ndarray) -> None:
    _, (axis1, axis2) = plt.subplots(1, 2, figsize=(16, 8))
    axis1: plt.Axes = axis1
    axis2: plt.Axes = axis2

    axis1.imshow(image1)
    axis2.imshow(image2)

    axis1.axis("off")
    axis2.axis("off")

    plt.show()

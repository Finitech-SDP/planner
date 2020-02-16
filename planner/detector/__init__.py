from typing import Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np
import cv2

from planner.config import IMAGE_PATH


def drawRect(image, space):
    cv2.rectangle(image, (space[0][0], space[0][1]), (space[1][0], space[1][1]),
                  (0, 255, 0), 2)


def captureImage():
    """
    THIS IS A MOCK FUNCTION.

    It will be replaced by a function that captures an image
    from the video stream...

    --Bora
    """
    img = cv2.imread(IMAGE_PATH)
    if img is None:
        raise Exception("could not capture image!")
    return img


def getEmptySpaces(image, coordMap: Dict[Tuple[int, int], np.ndarray], showSpaces=False) \
        -> Dict[Tuple[int, int], bool]:
    """
    :param image:
    :param coordMap: A dictionary that maps tiles (a tuple of int's) to coordinates from the video stream
    :param showSpaces:
    :return: True if empty else False
    """
    results = {}  # type: Dict[Tuple[int, int], bool]

    for tile, space in coordMap.items():
        spaceCropped = (image[space[0][1]:space[1][1], space[0][0]:space[1][0]])
        gray = cv2.cvtColor(spaceCropped, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 150, 200)
        isEmpty = np.sum(edged) <= 100

        results[tile] = isEmpty
        if showSpaces and isEmpty:
            drawRect(image, space)

    if showSpaces:
        plt.imshow(image)
        plt.show()

    return results

# spaceArray = getEmptySpaces('test.jpeg', showSpaces=True)
# print(spaceArray)

from typing import Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np
import cv2

from planner.config import STREAM_URL


def drawRect(image, space, colour=(0, 255, 0)):
    cv2.rectangle(image, (space[0][0], space[0][1]), (space[1][0], space[1][1]),
                  colour, 2)


def captureImage():
    cap = cv2.VideoCapture(STREAM_URL)

    # Skip the first 120 frames
    c = 0
    while cap.grab() and cap.isOpened() and c < 120:
        ok, img = cap.retrieve()
        if not ok:
            break
        c += 1

    # Retrieve the frame
    ok, img = cap.retrieve()
    if not ok:
        raise Exception("Could not retrieve the image!")

    return img


def annotateEmptySpaces(image, coordMap: Dict[Tuple[int, int], np.ndarray]):
    is_empty_map = getEmptySpaces(image, coordMap)

    for tile, space in coordMap.items():
        if is_empty_map[tile]:
            drawRect(image, space)
        else:
            drawRect(image, space, (255, 0, 0))

    return image


def getEmptySpaces(image, coordMap: Dict[Tuple[int, int], np.ndarray]) -> Dict[Tuple[int, int], bool]:
    """
    :param image:
    :param coordMap: A dictionary that maps tiles (a tuple of int's) to coordinates from the video stream
    :param showSpaces:
    :return: True if empty else False
    """
    results = {}  # type: Dict[Tuple[int, int], bool]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    for tile, space in coordMap.items():
        spaceCropped = (gray[space[0][1]:space[1][1], space[0][0]:space[1][0]])
        if spaceCropped is None:
            raise Exception("coordinates wrong?")
        edged = cv2.Canny(spaceCropped, 150, 200)
        isEmpty = np.sum(edged) <= 100
        results[tile] = isEmpty

    return results

# spaceArray = getEmptySpaces('test.jpeg', showSpaces=True)
# print(spaceArray)

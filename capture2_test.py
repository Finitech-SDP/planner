import cv2
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    cap = cv2.VideoCapture("http://129.215.3.22:8081/stream.ogg")

    c = 0
    while cap.grab() and cap.isOpened() and c < 120:
        ok, _ = cap.retrieve()
        if not ok:
            break

        c += 1

    ok, img = cap.retrieve()
    if not ok:
        raise Exception("anan")

    print(">>>", np.shape(img), img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.clf()
    plt.imshow(gray, cmap='gray', vmin=0, vmax=255)
    plt.show()

    print("DONE.")

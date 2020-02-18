import cv2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    cap = cv2.VideoCapture("http://129.215.3.22:8081/stream.ogg")

    plt.ion()
    while cap.grab() and cap.isOpened():
        ok, img = cap.retrieve()
        if not ok:
            break

        plt.clf()
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        plt.pause(0.001)

    print("DONE.")

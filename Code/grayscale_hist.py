# import numpy as np
from matplotlib import pyplot as plt
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

image_gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([image_gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

chans = cv2.split(image)
colors = ('b', 'g', 'r')
plt.figure()
plt.title('Flattened')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

plt.show()
cv2.waitKey(0)

eq = cv2.equalizeHist(image_gray)
cv2.imshow("Equalized", eq)
cv2.waitKey(0)


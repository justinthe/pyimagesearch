# python thresholding_1.py -i ../Data/thresholding/coins01.png
import argparse
import cv2
from skimage.filters import threshold_local

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Image", image)

# thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
thres = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
cv2.imshow("Mean Thresh", thres)

T = threshold_local(blurred, 29, offset=5, method='gaussian')
thresh = (blurred < T).astype('uint8') * 255
cv2.imshow("scikit thresh", thresh)
cv2.waitKey(0)
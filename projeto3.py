import cv2
import numpy as np

# read original image
img = cv2.imread('../images/dados1.jpg', cv2.IMREAD_COLOR)

# create binary image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(blur, 245, 255, cv2.THRESH_BINARY_INV)

# find contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# create all-black mask image
mask = np.zeros(img.shape, dtype="uint8")

# print table of contours and sizes
# print("Found %d objects." % len(contours))
for (i, c) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)

# apply mask to the original image
img = cv2.bitwise_and(img, mask)

# display original image with contours
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)
# cv2.imshow("output", img)

####################################################################################################
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary2 = cv2.threshold(blur, 245, 255, cv2.THRESH_BINARY)

# # find contours
contours, hierarchy = cv2.findContours(binary2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(hierarchy)

for c in contours:
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.polylines(img, [box],  True,  (0, 255, 0),  2)

# apply mask to the original image
img = cv2.bitwise_and(img, mask)

# # apply mask to the original image
# img = cv2.bitwise_and(img, mask)
#
# # display original image with contours
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)
# cv2.imshow("output", img)
#
cv2.imshow("output", img)
cv2.imshow("binary2", binary2)

cv2.waitKey(0)
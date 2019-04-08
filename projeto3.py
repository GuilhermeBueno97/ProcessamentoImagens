# Standard imports
import cv2

# Read image
img = cv2.imread("images/dados.jpg", cv2.IMREAD_COLOR)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# binary image
_, thresh = cv2.threshold(gray_image, 250, 255, cv2.THRESH_BINARY_INV)

# get contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

height, width = gray_image.shape
min_x, min_y = width, height
max_x = max_y = 0

# computes the bounding box for the contour, and draws it on the frame,
print(len(contours))

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 25:
        (x, y, w, h) = cv2.boundingRect(contour)
        # print("x = ", x, " y= ", y, " w = ", w, " h = ", h)
        min_x, max_x = min(x, min_x), max(x + w, max_x)
        min_y, max_y = min(y, min_y), max(y + h, max_y)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

        aux_image = img[y:y+h, x:x+w]

        # Detect blobs.
        keypoints = detector.detect(aux_image)

        print("Blobs = ", len(keypoints))

        cv2.putText(img, str(len(keypoints)), (int(x+(w/2)), int(y+(h/2))), cv2.FONT_HERSHEY_SIMPLEX, 1, (123, 23, 255), 2)

cv2.imshow("Blobs ", img)

cv2.waitKey(0)
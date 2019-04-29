# Standard imports
import cv2


def main():
    video()


def count_dices(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # binary image
    _, thresh = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)
    thresh_blur = cv2.medianBlur(thresh, 21)

    # get contours
    contours, hierarchy = cv2.findContours(thresh_blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

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
            min_x, max_x = min(x, min_x), max(x + w, max_x)
            min_y, max_y = min(y, min_y), max(y + h, max_y)

            roi = img[y:y+h, x:x+w]

            # Detect blobs.
            key_points = detector.detect(roi)

            print("Blobs = ", len(key_points))

            cv2.putText(img, str(len(key_points)), (int(x+(w/2)), int(y+(h/2))), cv2.FONT_HERSHEY_SIMPLEX, 1, (123, 23, 255), 2)


def video():
    cap = cv2.VideoCapture('images/diceVideo.mp4')

    while cap.isOpened():
        ret, frame = cap.read()

        count_dices(frame)
        cv2.imshow('Count Dices Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
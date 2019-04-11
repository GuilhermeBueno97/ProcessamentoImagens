import cv2
import numpy as np


def main():
    original = np.array([
                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
                ], dtype=np.uint8)

    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

    erode = personalizedErode(original, element)
    
    printImg(element, 'Element', 50)
    printImg(original, 'Original Image', 50)
    printImg(erode, 'Eroded Image', 50)

    print('\n\nNúmero de quadrados: ', np.count_nonzero(erode == 1))

    cv2.waitKey()
    cv2.destroyAllWindows()

def personalizedErode(original, element):
    finalImage = np.copy(original)
    original = np.pad(original,pad_width=1,mode='constant',constant_values=0)

    for (row,col),value in np.ndenumerate(finalImage) :
        if elementFound(row+1, col+1, original, element) :
            finalImage[row][col] = 1            
            original[row:row+3,col:col+3] = 0
        else:
            finalImage[row][col] = 0
            
    return finalImage

def elementFound(row, col, originalImage, element):
    refArray = originalImage[row-1:row+2,col-1:col+2]
    if np.array_equal(refArray, element):
        return True
    return False

def printImg(img, windowName, tam) :
    newimg = np.zeros((img.shape[0]*tam, img.shape[1]*tam), np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            tam = newimg.shape[0]/img.shape[0]
            radius = int(tam/2)
            x = int((i*tam)+(tam/2))
            y = int((j*tam)+(tam/2))
            if img[i, j] == 1:
                color = 255
            else:
                color = 0
            cv2.circle(newimg, (y, x), radius, (color, color, color), -1)
    ret,thresh1 = cv2.threshold(newimg, 0, 255, cv2.THRESH_BINARY_INV)
    img = np.array(thresh1)
    cv2.imshow(str(windowName), thresh1)


if __name__ == "__main__":
    main()

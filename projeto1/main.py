import cv2
import glob
from time import sleep

images = [cv2.imread(file) for file in glob.glob("imagens/*.jpg")]

fim = False
idx1 = 0
idx2 = 1

def fadeIn (img1, img2, len=20):
    for IN in range(0,len):
        fadein = IN/float(len)
        dst = cv2.addWeighted( img1, 1-fadein, img2, fadein, 0)
        cv2.imshow('window', dst)
        cv2.waitKey(1)
        sleep(0.05)

while (not fim) :
    for i in range(0, len(images)) :
        idx1 = i
        idx2 = i + 1 

        if(i == len(images) - 1):
            idx2 = 0 

        print("{} - {}".format(idx1,idx2))

        fadeIn(images[idx1],images[idx2],20)
        sleep(1)
    if fim :
        break

cv2.destroyAllWindows()
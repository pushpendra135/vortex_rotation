import cv2 as cv
import numpy as np
import math

img=cv.imread('visit5.jpeg')
#cv.imshow('image',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)


blur = cv.GaussianBlur(gray,(9,9),10)
#cv.imshow('Smooth', blur)

ret,thresh = cv.threshold(blur,127,255,cv.THRESH_TRUNC)
#cv.imshow('thresh',thresh)
# canny=cv.Canny(gray,128,128)
# cv.imshow('canny',canny

#
#all_circles = list()
rows = thresh.shape[0]
circles = cv.HoughCircles(thresh, cv.HOUGH_GRADIENT, 1, rows /4, param1=50, param2=50, minRadius=150, maxRadius=200)
#print(len(circles))
    
if circles is not None:
    circles = np.uint16(np.around(circles))
    #print(len(circles[0, :]))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(img, center, 1, (0, 100, 100), 3)
            # circle outline
        x, y, r = i[0],i[1],i[2]
        #all_circles.append([[x,y],r])
        radius = i[2]
        side = radius
        print(x,y,r)
        crop_image = img[y-side:y+side, x-side:x+side]
        img_name = str(x)+'_'+str(y)+'_'+str(r)+'.png'
        cv.imwrite(img_name,crop_image)
        cv.circle(img, center, radius, (255, 0, 255), 3)

#print(all_circles)

cv.imshow("detected circles", img)
cv.waitKey(0)
cv.destroyAllWindows()
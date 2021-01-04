import cv2

image=cv2.imread("rajini 1.jpg")                # Type the filename with extension
grayImg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image",image)
cv2.imshow("Grayscale image",grayImg)













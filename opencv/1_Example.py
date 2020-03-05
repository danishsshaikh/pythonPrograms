import imutils
import cv2

image = cv2.imread("jp.png")
#print(image.shape)
cv2.imshow("Jurassic Park",image)
#cv2.waitKey(0)

roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

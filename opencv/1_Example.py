import imutils
import cv2


image = cv2.imread("jp.png")
print(image.shape)
cv2.imshow("Jurassic Park",image)
cv2.waitKey(0)

import cv2
import imutils

image = cv2.imread("jp.png")

#cv2.imshow("Jurassic Park",image)
#cv2.waitKey(0)

output = image.copy()
cv2.rectangle(output, (320,60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle",output)
cv2.waitKey(0)

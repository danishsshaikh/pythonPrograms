import cv2
import imutils

image = cv2.imread("jp.png")

#cv2.imshow("Jurassic Park",image)
#cv2.waitKey(0)

output = image.copy()
#Rectangle
cv2.rectangle(output, (320,60), (420, 160), (0, 255, 255), 5)
#cv2.imshow("Rectangle",output)
cv2.waitKey(0)

#Circle
cv2.circle(output,(300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)



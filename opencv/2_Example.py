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
#cv2.imshow("Circle", output)
cv2.waitKey(0)

#Line
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
#cv2.imshow("Line", output)
cv2.waitKey(0)

cv2.putText(output, "DAN", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)


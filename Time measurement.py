import cv2

img1 = cv2.imread('Images/lena.jpg')
e1 = cv2.getTickCount()
for i in xrange(3,51,2):
	img1 = cv2.medianBlur(img1,i)
	#cv2.imshow("res", img1)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t
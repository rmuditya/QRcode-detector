import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture
# (2)
cap = cv2.VideoCapture(4)
# cap = cv2.VideoCapture()

cap.set(3,600)
cap.set(4,480)

while True:
	_,img = cap.read()
	code = decode(img)
	for barcode in decode(img):
		myData = barcode.data.decode('utf-8')
		# print(type(int(myData)))
		if int(myData) == 5:
			print("product ha = ", 5 )
		else:
			print("prodict nhi ha bhai")
		pts = np.array([barcode.polygon],np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img,[pts],True,(0,255,0),5)
		pts2 = barcode.rect
		cv2.putText(img,myData,(pts2[0],pts2[1]-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
		# print(myData)
	cv2.imshow("output", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

0
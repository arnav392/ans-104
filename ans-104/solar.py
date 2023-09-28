import cv2

img=cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(80,60),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255))
cv2.putText(img,"Mercury",(130,250),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Venus",(200,260),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Earth",(300,260),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Mars",(390,255),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Jupitar",(510,60),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Saturn",(770,300),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Uranus",(980,290),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Neptune",(1120,280),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.imshow("output",img)
cv2.waitKey(0)


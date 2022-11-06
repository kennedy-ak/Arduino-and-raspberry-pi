import cv2
vid = cv2.VideoCapture(0)
ret,frame =vid.read()
if ret:
    cv2.imwrite('image.jpg',frame)
    
    
vid.release()
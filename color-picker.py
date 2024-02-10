import cv2
import numpy as np

def cross(x):
    pass

img = np.ones([512,512,3],np.uint8)*0
cv2.namedWindow("color-picker")

cv2.createTrackbar("switch", "color-picker", 0, 1, cross)

cv2.createTrackbar("Red", "color-picker", 0, 255, cross)
cv2.createTrackbar("Green", "color-picker", 0, 255, cross)
cv2.createTrackbar("Blue", "color-picker", 0, 255, cross)

while True:
    cv2.imshow("color-picker", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    s = cv2.getTrackbarPos("switch", 'color-picker')
    r = cv2.getTrackbarPos("Red", 'color-picker')
    g = cv2.getTrackbarPos("Green", 'color-picker')
    b = cv2.getTrackbarPos("Blue", 'color-picker')
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
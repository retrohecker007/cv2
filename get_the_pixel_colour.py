''''
This program shows the cordinate of pixel when LMB is clicked,
and the colour code (in BGR format) is shown when RMB is clicked.
Input the file location to obtain the pixel colour.
'''

import cv2

def getinfo(event, x, y, flag, param):
       
    print('x: ', x)
    print('y: ', y)
    print('flag: ', flag)
    print('param: ', param)
    
    if event == cv2.EVENT_LBUTTONDOWN :
        
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cord = '.' + str(x) + ',' + str(y)
        cv2.putText(img, cord, (x, y), font, 1, (75, 255, 42), 1)
        cv2.imshow("lena", img)
        
    if event == cv2.EVENT_RBUTTONDOWN :
        
        b = img[x,y,0]
        g = img[x,y,1]
        r = img[x,y,2]
        
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = '.' + str(b) + ',' + str(g) + ',' + str(r)
        print("colour is: ",text)
        cv2.putText(img, text, (x,y), font, 1, (75, 255, 42), 1)
        cv2.imshow("lena", img)

inp = input(r"Enter file location: ")
img = cv2.imread(inp)
cv2.namedWindow("lena")
cv2.setMouseCallback("lena", getinfo)

while True:
    
    cv2.imshow("lena", img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
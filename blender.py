import cv2
import numpy as np

def onChange(x):
    pass

samp = np.ones([600,400,3], np.uint8)*255

cat = input(r"first image loc: ")
pik = input(r"second image loc: ")
cat = cv2.imread(cat)
pik = cv2.imread(pik)

cat = cv2.resize(cat, (600,400))
pik = cv2.resize(pik, (600,400))

cv2.namedWindow("controller")
cv2.namedWindow("blender")

cv2.createTrackbar("switch", "controller", 0, 1, onChange)
cv2.createTrackbar("blender", "controller", 0, 100, onChange)

while True:
    
    s = cv2.getTrackbarPos("switch", "controller")
    blend_val = cv2.getTrackbarPos("blender", "controller")
    
    res = cv2.addWeighted(cat, blend_val/100, pik, 1 - blend_val/100, 0)
    
    if s == 0:
        blend_val = 100
    
    else:
        
        cv2.imshow("controller", samp)
        cv2.imshow("blender", res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()


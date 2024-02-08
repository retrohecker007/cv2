#Screen Recorder

import cv2
import pyautogui as auto
import numpy as np

#get the resolution of screen
rs = auto.size()

file = input("Enetr the location to save: ")

fps = 20.0

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(file,fourcc,fps,rs)

#Create Recording module

cv2.namedWindow("Screen-Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Screen-Recording", (600,400))

while True:
    img = auto.screenshot()
    img = cv2.COLOR_BGR2RGB
    f = np.array(img)
    out.write(f)
    cv2.imshow("result", f)
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release()
cv2.destroyAllWindows()

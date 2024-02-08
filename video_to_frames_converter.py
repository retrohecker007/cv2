import cv2

vid = cv2.VideoCapture(r"C:\Users\navee\projects\learn cv2\resources\test2.mp4")
ret, frame = vid.read()

count = 0

while True:
    cv2.imwrite(r"C:\Users\navee\projects\learn cv2\outputs\frames\imgN%d.jpg"%count, frame)
    vid.set(cv2.CAP_PROP_POS_MSEC, (count*100))
    ret, frame = vid.read()
    cv2.imshow("result", frame)
    
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
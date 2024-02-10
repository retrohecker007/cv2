import cv2

#cv2.add() and cv2.addweighted()

cat = cv2.imread(r"C:\Users\navee\projects\learn cv2\resources\cat.jpg")
pik = cv2.imread(r"C:\Users\navee\projects\learn cv2\resources\pikachu.jpg")

cat = cv2.resize(cat, (600,400))
pik = cv2.resize(pik, (600,400))

add = cv2.add(cat,pik)

weight = cv2.addWeighted(cat, 0.7, pik, 0.3, 10)

cv2.imshow("add",add)
cv2.imshow("weight", weight)
cv2.waitKey(0)
cv2.destroyAllWindows()
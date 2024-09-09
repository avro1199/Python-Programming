import cv2 as cv

img = cv.imread(r"small_flower_dataset\tulips\142218310_d06005030a_n.jpg")
cv.imshow('Demo',img)
cv.waitKey(0)

# cap = cv.VideoCapture(r"F:\VID20211204223703.mp4")
cap = cv.VideoCapture(0)

while(True):
    state, img = cap.read()
    if not state:
        break
    img = cv.resize(img, (480,360), interpolation=cv.INTER_AREA)
    cv.imshow('DU',img)
    cv.waitKey(10)

cap.release()
cv.destroyAllWindows()
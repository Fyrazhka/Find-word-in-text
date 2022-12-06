import cv2
import pytesseract

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 24)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, img = cap.read()
    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27: # Клавиша Esc
        break
    str=pytesseract.image_to_string(img, lang='rus')
    if str:
        print(str)
        s=input('найден текст! Продолжить(1)')
        if s=='1':
            foud = input("Что найти? ")
            data = pytesseract.image_to_data(img, lang='rus')
            for i, el in enumerate(data.splitlines()):
                if i == 0:
                    continue
                el = el.split()
                try:
                    if (el[11] == foud):
                       print(el[11])
                       try:
                            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
                            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
                       except IndexError:
                           continue
                except IndexError:
                    continue

            cv2.imshow('Result', img)
            cv2.waitKey(0)


cap.release()
cv2.destroyAllWindows()



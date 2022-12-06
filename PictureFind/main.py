import cv2
import pytesseract

img = cv2.imread('SomePhoto.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



print(pytesseract.image_to_string(img,lang='rus'))
foud=input("Что найти? ")

data = pytesseract.image_to_data(img,lang='rus')
for i,el in enumerate(data.splitlines()):
    if i==0:
        continue

    el=el.split()
    try:
        if(el[11]==foud):
            print(el[11])
            try:
                x,y,w,h=int(el[6]),int(el[7]),int(el[8]),int(el[9])
                cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            except IndexError:
                continue
    except IndexError:
        continue

cv2.imshow('Result', img)
cv2.waitKey(0)


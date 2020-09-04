import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('people.jpg' , 1)
#1.5 and 3 are related to knn thing min and max values of neighbors
faces = face_cascade.detectMultiScale(img, 1.2, 3)
print (faces) #we get output in format of numbers which means its
#detecting faces in image

for(x,y,w,h) in faces:
    print(x,y,w,h)
    img = cv2.rectangle(img, (x,y) , (x+w, y+h) , (0, 255, 0) , 5)

resize = cv2.resize(img , (500, 500))

cv2.imshow('img' , img)
cv2.waitKey()
cv2.destroyAllWindows()

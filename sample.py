import cv2
#flag = 0 for balck and white and 1 for as it was
img = cv2.imread('people.jpg' , 1)
cv2.imshow('img' , img)
cv2.waitKey(10000)
cv2.imwrite('something.jpg' , img)
cv2.destroyAllWindows()




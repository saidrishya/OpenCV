import numpy as np
import cv2
#basically creating a black image of the dimensions
img = np.zeros((512, 512, 3) , np.uint8)
#creating a rectangle on it
#height , width rgb colors, 5=thickness 
cv2.rectangle(img, (200,100) , (300,10) , (255, 0 , 255) , 5)
cv2.imshow('img' , img)
cv2.waitKey()
cv2.destroyAllWindows()





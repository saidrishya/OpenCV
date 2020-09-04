import cv2

#videocapture(0) takes default webcam
#1 for external cam that is connected using usb or something
cap = cv2.VideoCapture('video.mp4')
while(True):
    #capture frame by frame
    ret ,frame = cap.read()
    
    #display the resulting frame
    cv2.imshow('frame', frame)

    #we were unable to stop the video, so we've given a condition that when we press q in the keyborad  it stops
    #the value in the waitkey is the number of frames per ms. 25 is the correct no
    #if anything > 25, the speed increases and viceversa
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


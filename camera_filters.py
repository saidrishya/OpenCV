import sys
import numpy as np
import cv2

preview = 0
blur = 1
features = 2
canny = 3

feature_params = dict(maxCorners = 500, qualityLevel = 0.2, minDistance = 15, blockSize = 9 )

s=0
if len(sys.argv) > 1:
    s = sys.argv[1]


image_filter = preview
alive = True

win_name = 'Camera Filters'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(s)

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)
    if image_filter == preview:
        result = frame
    elif image_filter == canny:
        result = cv2.Canny(frame, 80, 150)
    elif image_filter == blur:
        result = cv2.blur(frame, (13,13))
    elif image_filter == features:
         result = frame
         frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
         if corners is not None:
             for x, y in np.float32(corners).reshape(-1, 2):
                 cv2.circle(result, (int(x),int(y)), 10, (0, 255 , 0), 1)

    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord('q') or key == 27:
        alive = False
    elif key == ord('C') or key == ord('c'):
        image_filter = canny
    elif key == ord('B') or key == ord('b'):
        image_filter = blur
    elif key == ord('F') or key == ord('f'):
        image_filter = features
    elif key == ord('P') or key == ord('p'):
        image_filter = preview

source.release()
cv2.destroyWindow(win_name)



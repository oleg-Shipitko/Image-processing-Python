# This script detects cube's surface on a video frame 
# and reconstructs 3D image of cube from known in
# advance geometric paramiters.
 
import numpy as np
import cv2

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    res = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    # Display original frame
    #cv2.imshow("Original video (0.5 resizing)", res)
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    blurred = cv2.bilateralFilter(res,9,75,75)
    edges = auto_canny(blurred)
    cv2.imshow("Edge detection (0.5 resizing)", edges)

    (cnts, _) = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:4]
    # loop over the contours
    for c in cnts:
    # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4: 
            screenCnt = approx
            break

    cv2.drawContours(res, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Original video (0.5 resizing)", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.waitKey(0)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

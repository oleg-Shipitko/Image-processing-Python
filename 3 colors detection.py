import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of colors in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
   
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])

    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    res_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    res = cv2.bitwise_or(res_green, cv2.bitwise_or(res_blue, res_red))

    # cv2.imshow('mask blue',mask_blue)
    # cv2.imshow('mask red',mask_red)
    # cv2.imshow('mask green',mask_green)
    # cv2.imshow('res blue',res_blue)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
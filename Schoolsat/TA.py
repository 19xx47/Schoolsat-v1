import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('slide1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
elif cv2.waitKey(0) & 0xFF == ord('s'):
    cv2.imwrite('slide1.png', img)
    cv2.destroyAllWindows()
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 100], 'c', linewidth=5)
plt.show()

# Drawing on Images

img = cv2.imread('slide1.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()


# image from webcam
cap = cv2.V9ideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

ret = True
while ret:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('s'):
        cv2.imwrite('webcam.png', frame)
        break
cap.release()
cv2.destroyAllWindows()


# Webcam Resolution
def set_res(cap, x, y):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, x)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, y)
    return str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
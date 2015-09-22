print("loading")

import cv2
import numpy as np

img_orig = cv2.imread("otsu.png", 0)

hist, bins = np.histogram(img_orig.flatten(), 256, [0, 256])

sum1 = np.sum(range(0, 256) * hist)
total = img_orig.shape[0] * img_orig.shape[1]
sumB = 0
wB = 0
maximum = 0
threshold1 = 0
threshold2 = 0
for i in range(0, 256):
    wB = wB + hist[i]
    if(wB == 0): continue
    wF = total - wB
    if(wF == 0): break
    sumB = sumB + i * hist[i]
    mB = sumB / wB
    mF = (sum1 - sumB) / wF
    between = wB * wF * (mB - mF) * (mB - mF)
    if(between >= maximum):
        threshold1 = i
        if(between > maximum):
            threshold2 = i
        maximum = between

thresh = (threshold1 + threshold2) / 2

tr = np.zeros(256, dtype=np.uint8)
for i in range(0, 256):
    if(i < thresh): tr[i] = 0
    else: tr[i] = 255

img_res = tr[img_orig]

cv2.imshow("original", img_orig)
cv2.moveWindow("original", 0, 0)
cv2.imshow("result", img_res)
cv2.moveWindow("result", 512, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
print("loading")

import math
import cv2
import numpy as np

img_orig = cv2.imread("hough_small.png")

iw = img_orig.shape[0]
ih = img_orig.shape[1]
idiag = int(math.sqrt(iw*iw + ih*ih)) + 1

angle_q = 256 # [0, pi]
dist_q = 256 # [-idiag, idiag]

hough_space = np.zeros((dist_q, angle_q), dtype=np.double)

def draw_sinusoid(x, y):
    for a in range(0, angle_q):
        angle = (a * math.pi) / angle_q
        r = (x*math.cos(angle) + y*math.sin(angle)) * dist_q / (idiag * 2) + (dist_q / 2)
        if r > dist_q: print(r)
        if r < 0: print(r)
        hough_space.itemset((r, a), hough_space.item((r, a)) + 1)

print("processing")

for y in range(0, ih):
    print("%d / %d" % (y, ih))
    for x in range(0, iw):
        draw_sinusoid(x, y)

hough_space = hough_space / hough_space.max()

cv2.imshow("hough space", hough_space)
cv2.moveWindow("hough space", 0, 0)

#cv2.imshow("original", img_orig)
#cv2.moveWindow("original", 0, 0)
#cv2.imshow("result", img_res)
#cv2.moveWindow("result", 512, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
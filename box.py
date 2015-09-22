print("loading")

import cv2
import numpy as np

img_orig = cv2.imread("Lenna.png")

iw = img_orig.shape[0]
ih = img_orig.shape[1]

bw = int(raw_input("box width (default 3) :") or 3)
bh = int(raw_input("bow height (default 3) :") or 3)

img_integ = np.cumsum(np.cumsum(img_orig, 0), 1)

img_res = np.copy(img_orig)

for y in range(0, ih):
    y1 = y - (bh/2)
    y2 = y1 + bh
    y1 = max(0, min(y1, ih-1))
    y2 = max(0, min(y2, ih-1))
    for x in range(0, iw):
        x1 = x - (bw/2)
        x2 = x1 + bh
        x1 = max(0, min(x1, iw-1))
        x2 = max(0, min(x2, iw-1))
        val = img_integ[y2][x2] - img_integ[y1][x2] - img_integ[y2][x1] + img_integ[y1][x1]
        img_res[y][x] = val / ((x2-x1) * (y2-y1))

cv2.imshow("original", img_orig)
cv2.moveWindow("original", 0, 0)
cv2.imshow("result", img_res)
cv2.moveWindow("result", 512, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
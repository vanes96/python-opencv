print("loading")

import cv2
import numpy as np

img_orig = cv2.imread("Lenna.png")
img_orig = np.double(img_orig) / 255.0

gamma = float(raw_input("gamma:") or 1.0)

img_res = cv2.pow(img_orig, 1.0 / gamma)

cv2.imshow("original", img_orig)
cv2.moveWindow("original", 0, 0)
cv2.imshow("result", img_res)
cv2.moveWindow("result", 512, 0)

#cv2.imshow("original, result", np.hstack( (img_orig, img_res) ))
#cv2.moveWindow("original, result", 0, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()

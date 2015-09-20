print("loading")

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv2.imread("unequalized.png", 0)

B = float(raw_input("B (default 0.0) :") or 0.0)
W = float(raw_input("W (default 1.0) :") or 1.0)

hist, bins = np.histogram(img_orig.flatten(), 256, [0, 256])

cdf = np.cumsum(hist)
cdf_n = cdf * hist.max() / cdf.max()

cdf_m = np.ma.masked_less_equal(cdf, B * cdf.max())
cdf_m = np.ma.masked_greater_equal(cdf_m, W * cdf.max())

imin = cdf_m.argmin()
imax = cdf_m.argmax()

tr = np.zeros(256, dtype=np.uint8)
for i in range(0, 256):
    if i < imin: tr[i] = 0
    elif i > imax: tr[i] = 255
    else: tr[i] = (i - imin) * 255 / (imax - imin)

img_res = tr[img_orig]

hist_res, bins = np.histogram(img_res.flatten(), 256, [0, 256])
cdf_res = np.cumsum(hist_res)
cdf_res_n = cdf_res * hist_res.max() / cdf_res.max()

plt.subplot(211)
plt.hist(img_orig.flatten(), 256, [0, 256], color = 'r')
plt.plot(cdf_n, color = 'g')
plt.axhline(B * hist.max(), color = 'b')
plt.axhline(W * hist.max(), color = 'y')
plt.xlim([0, 256])
plt.ylim([0, hist.max()])

plt.subplot(212)
plt.hist(img_res.flatten(), 256, [0, 256], color = 'b')
plt.plot(cdf_res_n, color = 'g')
plt.xlim([0, 256])
plt.ylim([0, hist_res.max()])

plt.show()

cv2.imshow("original", img_orig)
cv2.moveWindow("original", 0, 0)
cv2.imshow("result", img_res)
cv2.moveWindow("result", 512, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()

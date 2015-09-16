print("loading")

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv2.imread("unequalized.png", 0)

'''
for x in range(0, 511):
    c1 = max(255 - abs(x - 256), 0) / 255.0
    c2 = c1 * c1 * 255.0
    c = (c2 // 32) * 32
    if c == 0: c = 1
    for y in range(0, 511):
        img_orig.itemset((x, y), c)
'''

B = float(raw_input("B (default 0.0) :") or 0.0)
W = float(raw_input("W (default 1.0) :") or 1.0)

hist, bins = np.histogram(img_orig.flatten(), 256, [0, 256])

cdf = np.cumsum(hist)

cdf_orig = cdf
#cdf_norm = cdf * hist.max() / cdf.max()

#cdf_m = np.ma.masked_less_equal(cdf, B * cdf.max())
cdf_m = np.ma.masked_less_equal(cdf, 0)
print(cdf_m)
print(cdf_m.min(), cdf_m.max())
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
#cdf[ cdf>255*W ] = 255

#cdf2_norm = cdf * hist.max() / cdf.max()

img_res = cdf[img_orig]

#for y in range(0, 511):
#    for x in range(0, 511):
#        c = img_orig.item(y, x)
#        img_res.itemset((y, x), cdf[c-1])

hist, bins = np.histogram(img_res.flatten(), 256, [0, 256])
cdf_res = np.cumsum(hist)

plt.subplot(221)
plt.plot(cdf_orig, color = 'r')
plt.plot(cdf_res, color = 'g')
plt.xlim([0, 256])
plt.ylim([0, 512*512])

plt.subplot(222)
plt.plot(cdf, color = 'g')
plt.xlim([0, 256])
plt.ylim([0, 256])

plt.subplot(223)
plt.hist(img_orig.flatten(), 256, [0, 256], color = 'r')
plt.xlim([-8, 264])

plt.subplot(224)
plt.hist(img_res.flatten(), 256, [0, 256], color = 'g')
plt.xlim([-8, 264])

#plt.show()

#exit()

cv2.imshow("original", img_orig)
cv2.moveWindow("original", 0, 0)
cv2.imshow("result", img_res)
cv2.moveWindow("result", 512, 0)

plt.show()

#cv2.imshow("original, result", np.hstack( (img_orig, img_res) ))
#cv2.moveWindow("original, result", 0, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()

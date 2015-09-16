print("loading")

import cv2
import numpy as np
#import matplotlib.pyplot as plt

img_orig = cv2.imread("unequalized.png", 0)

hist, bins = np.histogram(img_orig.flatten(), 256, [0, 256])

cdf = np.cumsum(hist)
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

img_res = cdf[img_orig]

#plt.hist(img_orig.flatten(), 256, [0, 256], color = 'r')
#plt.hist(img_res.flatten(), 256, [0, 256], color = 'g')
#plt.xlim([0, 256])
#plt.show()

hist, bins = np.histogram(img_res.flatten(), 256, [0, 256])

cv2.imshow("original", img_orig)
cv2.moveWindow("original", 0, 0)
cv2.imshow("result", img_res)
cv2.moveWindow("result", 512, 0)

#cv2.imshow("original, result", np.hstack( (img_orig, img_res) ))
#cv2.moveWindow("original, result", 0, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()

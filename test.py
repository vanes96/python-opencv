import cv2
#import numpy as np
#from matplotlib import pyplot as plt

def imshow(img):
    cv2.imshow('1', img)
    cv2.moveWindow('1', 256, 0)
    cv2.waitKey(0)
    cv2.destroyWindow('1')

img_lenna = cv2.imread("Lenna.png")

imshow(img_lenna)

img_r = cv2.imread("r.png")
img_g = cv2.imread("g.png")
img_b = cv2.imread("b.png")

imshow(cv2.add(img_lenna, img_r))

cr = 1.0
cg = 0.5
cb = 0.1

img = cv2.addWeighted(img_r, cr, img_g, cg, 0.0)
img = cv2.addWeighted(img, 1.0, img_b, cb, 0.0)

imshow(img)

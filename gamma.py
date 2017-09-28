from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2
import os.path
from sys import argv

def gamma_correction(image, a, b):
    table = np.array(
        [int((a * ((i / 255.0) ** b)) * 255) for i in range(0, 256)]
    ).astype("uint8")
    return cv2.LUT(image, table)

def save_image(image_name, new_name, a, b):
    img_orig = img.imread(image_name)
    plt.subplot(1, 2, 1)
    plt.title('Original image')
    plt.imshow(img_orig)

    img_corr = gamma_correction(img_orig, a, b)
    plt.subplot(1, 2, 2)
    plt.title ('Corrected image: a = ' + str(a) + ', b = ' + str(b))
    plt.imshow(img_corr)
    cv2.imwrite(new_name, img_corr)
    plt.show()

#======================= MAIN =========================
if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = float(argv[3])
    argv[4] = float(argv[4])
    assert 0 <= argv[3] < 1
    assert 0 <= argv[4] < 1
    save_image(argv[1], argv[2], argv[3], argv[4])
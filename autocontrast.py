from __future__ import print_function
import matplotlib.pyplot as plt
from PIL import Image
import os.path
from sys import argv

def brighness(a):
    return int(0.3 * a[0] + 0.59 * a[1] + 0.11 * a[2])

def autocontrast(image, white_perc, black_perc):
    image_ = image
    size = image_.size[0] * image_.size[1]
    number_white = int(size * white_perc)
    number_black = int(size * black_perc)
    clrs = image_.getcolors(size)
    brts = [0] * 256

    for col in clrs:
        brts[brighness(col[1])] += col[0]

    count, index_black = 0, 0
    for i in range(256):
        if count < number_black:
            count += brts[i]
        else:
            index_black = i
            break

    count, index_white = 0, 0
    for i in range(255, -1, -1):
        if count < number_white:
            count += brts[i]
        else:
            index_white = i
            break
    #----------------------------------------------
    pixels = list(image_.getdata())
    for i in range(size):
        brt = brighness(pixels[i])
        if brt < index_black:
            pixels[i] = (0, 0, 0)
        elif brt > index_white:
            pixels[i] = (255, 255, 255)
        else:
            dif = (brt - index_black) * 255 / (index_white - index_black) - brt
            pixels[i] = (int(pixels[i][0] + dif * 0.3), int(pixels[i][1] + dif * 0.59), int(pixels[i][2] + dif * 0.11))
    image_.putdata(pixels)
    # ----------------------------------------------
    return image_

def save_image(img_orig, new_name, white_perc, black_perc):
    plt.subplot(1, 2, 1)
    plt.title('Original image')
    plt.imshow(img_orig)

    img_corr = autocontrast(img_orig, white_perc, black_perc)
    plt.subplot(1, 2, 2)
    plt.title('Changed image: black = ' + str(black_perc) + ', white = ' + str(white_perc))
    plt.imshow(img_corr)
    #plt.savefig(new_name) Если станет скучно
    img_corr.save(new_name)
    plt.show()

#======================= MAIN =========================
if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = float(argv[3])
    argv[4] = float(argv[4])
    assert 0 <= argv[3] < 1
    assert 0 <= argv[4] < 1
    save_image(Image.open(argv[1]), argv[2], argv[3], argv[4])






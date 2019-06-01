# -*- coding: utf-8 -*-
import os, cv2, numpy as np

#video = "../test-fg-imgs/"
video = './../../aic19-track3/test_fg_imgs'

rt_p = './video_mask'
if not os.path.exists(rt_p):
    os.mkdir(rt_p)


def make_mask(num, thre=1):
    path = os.path.join(video, str(num))
    imgs = os.listdir(path)
    imgs.sort()

    kernel = np.ones((5,5), np.uint8)
    w, h, _ = cv2.imread(os.path.join(path, imgs[0])).shape
    ave_img = np.zeros((w, h, 3))
    for i in range(300, 2100):
        img = cv2.imread(os.path.join(path, imgs[i]))
        ave_img += img.astype(np.float64)
    ave_img /= 1800
    ret,thresh = cv2.threshold(ave_img.astype(np.uint8), thre, 255, cv2.THRESH_BINARY)
    img_new = cv2.dilate(cv2.erode(thresh, kernel, iterations=1), kernel, iterations=1)
    cv2.imwrite(os.path.join(rt_p, str(num), 'mask.jpg'), img_new)

for i in range(1, 101):
    if not os.path.exists(os.path.join(rt_p, str(i))):
        os.mkdir(os.path.join(rt_p, str(i)))
    make_mask(i)




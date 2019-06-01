# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np

#tasks = ['./aic19-track3-test-data', './aic19-track3-train-data']

tasks = ['./aic19-track3-test-videos']

for t in tasks:
    name = 'test' if 'test' in t else 'train'
    save_bg_path = name + '_bg_imgs'
    save_fg_path = name + '_fg_imgs'
    if not os.path.exists(save_bg_path):
        os.mkdir(save_bg_path)
        os.mkdir(save_fg_path)

    path = os.path.join(t, 'videos')
    videos = os.listdir(path)

    for v in videos:
        v_name = os.path.join(path, v)
        print("Now for {}".format(v_name))
        save_bg_path_ = os.path.join(save_bg_path, v.split('.')[0])
        save_fg_path_ = os.path.join(save_fg_path, v.split('.')[0])
        if not os.path.exists(save_bg_path_):
            os.mkdir(save_bg_path_)
            os.mkdir(save_fg_path_)
        cap = cv2.VideoCapture(v_name)

        bg = cv2.createBackgroundSubtractorMOG2()
        bg.setHistory(120)

        #fourcc = cv2.VideoWriter_fourcc(*'FLV1')
        ret, frame = cap.read()
        #h, w, _ = frame.shape
        #fg_writer = cv2.VideoWriter(
        #    os.path.join(save_fg_path,'{}.flv'.format(v.split('.')[0])),
        #    fourcc, 30, (w,h))
        count = 0

        while ret:
            fg_img = bg.apply(frame)
            #fg_img_rgb = np.expand_dims(fg_img, axis=2)
            #fg_img_rgb = np.concatenate((fg_img, fg_img, fg_img), axis=-1)
            #fg_writer.write(fg_img_rgb)
            cv2.imwrite(os.path.join(save_fg_path_, '{}.png'.format(count)), fg_img)
            bg_img = bg.getBackgroundImage()
            #if count%30==0:
            cv2.imwrite(os.path.join(save_bg_path_,'{}.png'.format(count)), bg_img)
            ret, frame = cap.read()
            count += 1
        cap.release()
        #fg_writer.release()

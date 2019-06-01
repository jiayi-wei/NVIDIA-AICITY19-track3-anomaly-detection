# -*- coding: utf-8 -*-
import os, cv2, numpy as np

video = "./../aic19-track3-test-videos"

rt_p = './stuck_record'
if not os.path.exists(rt_p):
    os.mkdir(rt_p)


vs = os.listdir(video)
for v in vs:
    path = os.path.join(video, v)
    cap = cv2.VideoCapture(path)
    ret, frame = cap.read()
    begin = 0
    old_ = frame.copy()
    ret, frame = cap.read()
    count = 1
    f = open(os.path.join(rt_p, v.split('.')[0]+'.txt'), 'a')
    while ret:
        diff = frame-old_
        diff_sum = np.sum(diff)
        if diff_sum<10:
            begin = count
            #f = open(os.path.join(rt_p, str(i)+'.txt'), 'a')
            #f.write(str(v)+" "+str(count))

            while ret:
                ret, frame = cap.read()
                count += 1
                diff = frame-old_
                diff_sum = np.sum(diff)
                if diff_sum>10:
                    break
            if count-begin>60:
                f.write(str(begin)+" "+str(count)+"\n")
        old_ = frame.copy()
        ret, frame = cap.read()
        count += 1
    f.close()





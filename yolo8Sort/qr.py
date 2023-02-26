import os
import datetime
import time

import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np


with open('./whitelist.txt', 'r') as f:
    authorized_users = [l[:-1] for l in f.readlines() if len(l) > 2]
    f.close()

log_path = './log.txt'

cap = cv2.VideoCapture(0)

most_recent_access = {}

time_between_logs_th = 5

while True:

    ret, frame = cap.read()

    qr_info = decode(frame)

    if len(qr_info) > 0:

        qr = qr_info[0]

        data = qr.data
        rect = qr.rect
        polygon = qr.polygon
        print(qr.data)


        cv2.putText(frame, 'ACCESS GRANTED', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        with open(log_path, 'a') as f:
            f.write('{},{}\n'.format(data.decode(), datetime.datetime.now()))
            f.close()



        frame = cv2.polylines(frame, [np.array(polygon)], True, (255, 0, 0), 5)

    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
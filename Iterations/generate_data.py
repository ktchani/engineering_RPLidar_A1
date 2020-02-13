import csv
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from threading import Thread
import time
from rplidar import RPLidar
import random
lidar = RPLidar('COM6', baudrate=115200)

x_value = 0
theta = 0
r = 0
counter = 0
fieldnames = ["x_value", "theta", "r"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()



with open('data.csv', 'a') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)


    print('test1')

    print('test2')


    print(x_value, theta, r)
    for scan in lidar.iter_scans(max_buf_meas=500):
        print('test3')

        for data in scan:
            counter=counter+1
            x_value=str(data[0])
            theta = str(data[1])
            r = str(data[2])
            info = {
                "x_value": x_value,
                "theta": theta,
                "r": r
            }
            csv_writer.writerow(info)

            if counter>200:
                csv_file.truncate()

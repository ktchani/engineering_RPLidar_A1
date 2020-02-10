import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from threading import Thread
import time
from rplidar import RPLidar
import random

# lidar.set_pwm()

def get_data():
    lidar = RPLidar('COM6', baudrate=115200)
    for scan in lidar.iter_scans(max_buf_meas=500):
        print(scan)
        file1 = open("text_data.txt", "a")
        file1.write(str(scan))
        # for data in scan:
        #     theta = str(data[1] % 360)
        #     r = str(data[2])
        #
        # file1.write(theta + "|" + r + " ")

        file1.close()

        break
    lidar.stop()
    return scan


            




get_data()
print('hello')
get_data()
print('hello')


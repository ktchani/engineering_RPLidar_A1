import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from threading import Thread
import time
from rplidar import RPLidar

plt.axis([0, 10, 0, 1])
lidar = RPLidar('COM7', baudrate=115200)


def get_data():
    for scan in lidar.iter_scans(max_buf_meas=100):
        print(scan)
        print(scan[0])
        print('test')
        print(scan[0][1])
        print(scan[0][2])


get_data()





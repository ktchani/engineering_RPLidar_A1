import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from threading import Thread
import time
from rplidar import RPLidar
import random
lidar = RPLidar('COM7', baudrate=115200)
# lidar.set_pwm()

def get_data():

    for scan in lidar.iter_scans(max_buf_meas=500):
        print(scan)
        for data in scan:
            file1 = open("text_data.txt", "a")
            r=str(data[2])
            theta=str(data[1]%360)
            file1.write(r+"|"+theta+" ")

            file1.close()

            




get_data()





import numpy as np
from math import cos, sin, pi, floor
import matplotlib.pyplot as plt
from rplidar import RPLidar
# lidar = RPLidar('COM6', baudrate=115200)
# lidar.stop()
# lidar.disconnect()
def get_data():
    x=[]
    y=[]
    scan_data = [0] * 360
    lidar = RPLidar(port='COM6', baudrate=115200)
    for scan in lidar.iter_scans(max_buf_meas=500):
        for(_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])]=distance

    lidar.stop()
    return scan_data, distance



for i in range(1000000):
    # if(i%3==0):
    #     x = []
    #     y = []
    print(i)
    scan_data, distance = get_data()
    print(distance)
    print(scan_data)

    plt.clf()
    plt.scatter(x, y)
    plt.pause(.00001)
plt.show()




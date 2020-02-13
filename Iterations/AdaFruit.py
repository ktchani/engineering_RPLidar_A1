import numpy as np
from math import cos, sin, pi, floor
import matplotlib.pyplot as plt
from rplidar import RPLidar
# lidar = RPLidar('COM6', baudrate=115200)
# lidar.stop()
# lidar.disconnect()



scan_data = []
lidar = RPLidar(port='COM7', baudrate=115200)
for scan in lidar.iter_scans(max_buf_meas=500):
    angleA=[]
    distanceA=[]
    counter=0
    for(_, angle, distance) in scan:
        counter=counter+1
        # scan_data[min([359, floor(angle)])]=distance
        angleA.append(distance*sin(angle))
        distanceA.append(distance*cos(angle))
        if(counter==len(scan)):
            print('end of loop start plotting')
            plt.scatter(angleA, distanceA)

            plt.clf()
            plt.pause(.001)

plt.show()













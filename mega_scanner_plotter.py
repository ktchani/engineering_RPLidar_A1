import numpy as np
from numpy import exp, abs, angle
import matplotlib.pyplot as plt
from matplotlib import animation
from threading import Thread
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from threading import Thread
import time
from rplidar import RPLidar
import random
x=[]
y=[]



def get_data():
    lidar = RPLidar('COM6', baudrate=115200)
    for scan in lidar.iter_scans(max_buf_meas=500):
        break
    lidar.stop()
    return scan


for i in range(1000000):
    print(i)
    current_data=get_data()
    for point in current_data:
        if point[0]==15:
            x.append(point[2]*np.cos(point[1]))
            y.append(point[2]*np.sin(point[1]))
            


    plt.scatter(x, y)
    
    plt.pause(.1)

    if(i%2==0):
        plt.cla()
        

        




plt.show()




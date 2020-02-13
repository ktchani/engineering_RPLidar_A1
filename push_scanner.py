from math import pi, sin, cos
import matplotlib.pyplot as plt
from rplidar import RPLidar

def get_data():
    x=[]
    y=[] 
    lidar = RPLidar('COM7', baudrate=115200)
    lidar.set_pwm(pwm=800)
    counter=0
    for scan in lidar.iter_scans(max_buf_meas=500):
        x=[]
        y=[]
        for point in scan:
            x.append(point[2] * sin(point[1] * pi / 180))
            y.append(point[2] * cos(point[1] * pi / 180))
        plt.clf()
        plt.scatter(x, y, marker='o', s=1)
        plt.xlim(-1000,1000)
        plt.ylim(-1000,1000)
        plt.pause(.0001)
 

    lidar.stop()
    return scan
plt.show()

get_data()

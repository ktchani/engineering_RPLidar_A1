from math import pi, sin, cos
import matplotlib.pyplot as plt
from rplidar import RPLidar

# lidar = RPLidar('COM6', baudrate=115200)
# lidar.stop()
# lidar.disconnect()
def get_data():
    lidar = RPLidar('COM7', baudrate=115200)
    lidar.set_pwm(pwm=800)
    for scan in lidar.iter_scans(max_buf_meas=500):
        print(scan)
        print(len(scan))
        for thing in scan:
            print(thing)
        break
    lidar.stop()
    return scan

for i in range(1000000):
    if(i%1==0):
        x = []
        y = []
    print(i)
    current_data=get_data()
    for point in current_data:

        x.append(point[2]*sin(point[1]*pi/180))
        y.append(point[2]*cos(point[1]*pi/180))
    plt.clf()
    plt.scatter(x, y)
    plt.pause(.1)
plt.show()




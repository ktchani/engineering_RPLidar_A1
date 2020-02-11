import numpy as np
import matplotlib.pyplot as plt
from rplidar import RPLidar
# lidar = RPLidar('COM6', baudrate=115200)
# lidar.stop()
# lidar.disconnect()

def get_data():
    lidar = RPLidar('COM6', baudrate=115200)
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
    if(i%7==0):
        x = []
        y = []
    print(i)
    current_data=get_data()
    for point in current_data:

        x.append(point[2])
        y.append(point[1])
    plt.clf()
    plt.scatter(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    theta = y
    r = x

    ax.plot(theta, r, "o")





    plt.pause(.00001)
plt.show()




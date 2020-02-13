import numpy as np
import matplotlib.pyplot as plt
from rplidar import RPLidar

def get_data():
    lidar = RPLidar('COM6', baudrate=115200)
    j=0
    scan_array=[]
    for scan in lidar.iter_scans(max_buf_meas=500):
        j=j+1
        scan_array.append(scan)
        if(j==10):
            break
    lidar.stop()
    return scan_array


for i in range(1000000):
    x = []
    y = []
    print(i)
    current_data = get_data()
    for array in current_data:
        for point in array:
            if point[0] == 15:
                x.append(point[2] * np.sin(point[1]))
                y.append(point[2] * np.cos(point[1]))
    plt.clf()
    plt.scatter(x, y)

    plt.pause(.1)

plt.show()




from rplidar import RPLidar
import matplotlib
from matplotlib import pyplot
import time
import matplotlib.pyplot as plt

lidar = RPLidar('COM7', baudrate=115200)
lidar.stop_motor()
lidar.set_pwm(pwm=1)
print('timing finishing')
lidar.start_motor()
health = lidar.get_health()
print(health)
i = 0
theta = []
r = []


def plotprog():
    plt.plot(r, theta)
    plt.ylabel('some numbers')
    plt.show()


while (i < 100):
    for scan in lidar.iter_scans(max_buf_meas=100):
        print(i)
        for data in scan:
            i = i + 1
            if i % 10 == 0:
                theta.append(data[1] % 360)
                r.append(data[2])

            if (i >= 2000):
                plotprog()

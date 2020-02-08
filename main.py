import numpy as np
from numpy import exp, abs, angle
import matplotlib.pyplot as plt
from matplotlib import animation
from threading import Thread
import time
import math
from rplidar import RPLidar

plt.axis([-1000, 1000, -1000, 1000])



for i in range(1000):

    file1 = open("text_data.txt","r")
    file_data=file1.read().split()[-1]
    r=float(file_data.split("|")[0])
    theta=float(file_data.split("|")[1])
    print(file_data)
    y=r*math.cos(theta)
    x=r*math.sin(theta)
    print("-------")
    print(x)
    print(y)

    plt.scatter(x, y)
    plt.pause(.001)
    file1.close()
        

        




plt.show()




import numpy as np
from numpy import exp, abs, angle
import matplotlib.pyplot as plt
from matplotlib import animation
from threading import Thread
import time
import math


plt.axis([-500, 500, -500, 500])



for i in range(1000000):

    file1 = open("text_data.txt","r")
    
    file_data=file1.read().split()[-1]
    r=float(file_data.split("|")[0])
    print('********'+file_data)
    theta=float(file_data.split("|")[1])
    print('--------')
    print(r, theta)
  
    x=r*(np.cos(theta))
    y=r*(np.sin(theta))
    print("-------")
    print(x)
    print(y)

    plt.scatter(x, y)
    plt.pause(.005)
    file1.close()
        

        




plt.show()




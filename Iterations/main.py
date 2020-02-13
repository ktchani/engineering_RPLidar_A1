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
  
    parent_set=file1.read().replace(']','').replace('[','').replace(')','').replace('(','').split(',')
    print(parent_set)
    file_data=file1.read().split()[-1]
    theta=float(file_data.split("|")[0])
    print('********'+file_data)
    r=float(file_data.split("|")[1])
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
    if(i>1000):
        plt.cla()
        

        




plt.show()




import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy

plt.style.use('classic')

x_vals = []
y_vals = []

index = count()

j=0
print("test1")
def animate(i):

    print(i)
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['theta']
    y2 = data['r']
    real1=y2*(numpy.cos(y1))
    real2=y2*(numpy.sin(y1))
    plt.clf()

    plt.plot(real1, real2, label='Channel 1')


    plt.legend(loc='best')
    plt.tight_layout()
    


print("test3")
ani = FuncAnimation(plt.gcf(), animate, interval=100)
print("test4")

plt.show()

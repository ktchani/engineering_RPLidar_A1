import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

# Data:
mu = 1
e = 1
a = 1
c = 1

beta = np.linspace(0.0 ,0.5,25)
C = (mu*((e*a)**2)) / (16*(np.pi**2)*c) 

theta = np.linspace(-2 * np.pi, 2 * np.pi, 200)

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

line, = ax.plot([],[])


def update(b):
    r = (np.sin(theta)**2)/(1 - b*np.cos(theta))**5
    dP = C*r
    line.set_xdata(theta)
    line.set_ydata(dP)
    return line,

ani = FuncAnimation(fig, update, frames=beta, blit=True)
plt.show()

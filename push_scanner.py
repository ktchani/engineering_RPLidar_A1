from math import pi, sin, cos
import matplotlib.pyplot as plt
from rplidar import RPLidar
lidar = RPLidar('COM7', baudrate=115200)
plt.ion()
plt.show()
range_mm=2500
def get_data():
    x=[]
    y=[] 
    

    counter=0
    for scan in lidar.iter_scans(max_buf_meas=500):
        file1 = open("MyFile.txt","a")
        file1.write(str(scan))
        file1.close()
        plot_data(x,y)
        x=[]
        y=[]
            
        for point in scan:

            x.append(point[2] * -1*sin(point[1] * pi / 180))
            y.append(point[2] * -1*cos(point[1] * pi / 180))
            print(str(point[2] * -1*sin(point[1] * pi / 180))+" "+str(point[2] * -1*cos(point[1] * pi / 180)))
        

 
    
   
    return scan

def plot_data(x, y):

    plt.clf()
    plt.xlim(-range_mm, range_mm)
    plt.ylim(-range_mm, 0)
    plt.scatter(x, y, marker='o', s=.5)
    plt.pause(0.01)


get_data()

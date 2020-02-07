from rplidar import RPLidar
import time
lidar = RPLidar('COM7', baudrate=115200)
lidar.stop_motor()
lidar.set_pwm(pwm=1)
print('timing finishing')
lidar.start_motor()
health = lidar.get_health()
print(health)
i=0
for scan in lidar.iter_scans():
    print(scan)
    print(len(scan))
    i=i+1
    print(i)
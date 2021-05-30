import Particle as prt
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
#from mpl_toolkits.mplot3d.axes3d import Axes3D
#mislim da mi je zadatak dobar jer mi je dio pomogla kolegica i radila sam na satu, ali mi ne radi mpl_toolkits nadam se da ce vama raditi jer je ne znam kako to rjesiti...

p0 = prt.ElMangnPolje()
p1 = prt.ElMangnPolje()


p0.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p0.moveE(15)
p1.init(1, 1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p1.moveE(15)

ax = plt.axes(projection = "3d"š
ax.plot3D(p0.x_, p0.y_, p0.z_)
ax.plot3D(p1.x_, p1.y_, p1.z_)
ax.view_init(30, 30)
plt.legend()
plt.show()

p2 = prt.ElMangnPolje()
p2.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))
p2.moveR(15)

ax = plt.axes(projection = "3d")
ax.plot3D(p0.x_, p0.y_, p0.z_)
ax.plot3D(p2.x_x, p2.y_y, p2.z_z)
ax.view_init(30, 30)
plt.legend()
plt.show()
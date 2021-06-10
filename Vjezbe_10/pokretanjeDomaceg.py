import Particle as prt
import domacirad as dr
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D

p0 = prt.ElMangnPolje()
p1 = prt.ElMangnPolje()

p0.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p0.moveE(20)

p1.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p1.moveE2(20)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot3D(p0.x_, p0.y_, p0.z_, 'blue')
ax.plot3D(p1.x_x1, p1.y_y1, p1.z_z1, 'red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("elepoz.png")

p0.reset()
p1.reset()


p2 = prt.ElMangnPolje()
p3 = prt.ElMangnPolje()

p2.init(1, -1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))
p2.moveE2(20)

p3.init(1, 1, np.array([0,0,0]), np.array([0.1,0.1,0.1]), np.array([0,0,1]), np.array([0,0,0]))  
p3.moveE2(20)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot3D(p2.x_x1, p2.y_y1, p2.z_z1)
ax.plot3D(p3.x_x1, p3.y_y1, p3.z_z1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("ele_poz.png")
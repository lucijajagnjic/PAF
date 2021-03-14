import matplotlib.pyplot as plt 
from math import sin, cos
v0 = 20 #brzina je u m/s
theta = 60 
g = 9.8
dt = 0.1
t = 0
x = 0
y = 0
vx = v0 * cos(theta)
xl = []
yl = []
tl = []

for i in range(100):
    x = vx * t 
    y = v0 * sin(theta) * t - 0.1 * g * t * t
    t += dt

    xl.append(x)
    yl.append(y)
    tl.append(t)

plt.subplot(311)
plt.plot(xl,yl)
#radi y-x graf
plt.subplot(312)
plt.plot(tl,xl)
#radi x-t graf
plt.subplot(313)
plt.plot(tl,yl)
#radi y-t graf
plt.show()
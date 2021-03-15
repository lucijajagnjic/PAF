import matplotlib.pyplot as plt 
from math import sin, cos, pi
v0 = 20 
theta = 60
theta = (theta/360) * 2 * pi 
g = 9.81
dt = 0.1
t = 10
N = int(t/dt)
t = 0
x = 0
y = 0
vx = v0 * cos(theta)
vy = v0 * sin(theta)
xl = []
yl = []
tl = []

for i in range(N):
    x = x + vx * dt
    vy = vy - g * dt
    y = y + vy * dt
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
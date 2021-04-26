import matplotlib.pyplot as plt
from math import sin, cos, pi

def kosi_hitac(v0, theta, t):
    theta = (theta/360)*2*pi
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)
    dt = 0.1
    g = 9.81
    x = 0
    y = 0
    N = int(t/dt)
    t = 0
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

    plt.subplot(312)
    plt.plot(tl,xl)
    
    plt.subplot(313)
    plt.plot(tl,yl)

    plt.show()

def jednoliko_gibanje(F,m,t):
    v = 0
    x = 0
    dt = 0.1
    a = F/m
    N = int(t/dt)
    t = 0
    vrijeme = []
    brzina = []
    pomak = []
    akceleracija = []

    for i in range(N):
        v = v + a * dt
        x = x + v * dt
        t += dt
        
        vrijeme.append(t)
        brzina.append(v)
        pomak.append(x)
        akceleracija.append(a)

    plt.subplot(311)
    plt.plot(vrijeme,pomak)

    plt.subplot(312)
    plt.plot(vrijeme,brzina)

    plt.subplot(313)
    plt.plot(vrijeme,akceleracija)

    plt.show()
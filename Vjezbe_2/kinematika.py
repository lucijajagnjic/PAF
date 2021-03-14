import matplotlib.pyplot as plt
from math import sin, cos
#kosi hitac - pocetna brzina, kut i vrijeme
def kosi_hitac(v0, theta, t):
    vx = v0 * cos(theta)
    dt = 0.1
    t = 0
    g = 9.8
    x = 0
    y = o
    N = 2 * t
    xl = []
    yl = []
    tl = []

    for i in range(N):
        x = vx * t
        y = v0 * sin(theta) * t - 0.1 * g * t * t
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

    plt.show

#jednoliko gibanje - sila, masa, vrijeme
def jednoliko_gibanje(F,m,t):
    v = 0
    x = 0
    dt = 0.1
    t = 0
    a = F/m
    vrijeme = []
    brzina = []
    pomak = []
    akceleracija = []

    for i in range(100):
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
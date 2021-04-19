import math
import zadatak1 as zdk1

def maxVisina(v0, g):
    g = 9.81
    h = 0
    v0 = 0
    hmaxl = []

    for i in range(0.01):
        h = 2*v0 / 2*g
        
        hmaxl.append(h)


def vrijeme(v0, g):
    g = 9.81
    t = 0
    v0 = 0
    tmaxl = []

    for i in range(0.05):
        t = v0 / g

        tmaxl.append(t)


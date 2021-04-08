import math 
import numpy as np 
import matplotlib.pyplot as plt

def derivacija(func,x,h):
    d3 = (func(h+x)-func(x-h))/(2*h)
    return d3

def derivacija2 (func,x,h):
    d2 = ((func(x))-(func(x-h))) / h


def deriviranje(func,x1,x2,h,m):
    dlista = []
    xlista = np.arange(x1,x2,h)

    if m == 3:
        for x in xlista:
            d = derivacija(func,x,h)
            dlista.append(d)

        elif m == 2:
            for x in xlista:
                d = derivacija2(func,x,h)
                dlista.append(d) 

    return xlista, dlista

def integriranje(func, a, b, N):
    dx = (float(b)-float(a)) / float(N)
    print(dx)
    gX = a + dx
    dX = a
    gornjaMeda = 0
    donjaMeda = 0

    for i in range(N):
        if abs(func(gX)) >= abs(func(dX)):
            gornjaMeda += func(gX)*dx
            donjaMeda += func(dX)*dx
        else:
            gornjaMeda += func(dX)*dx
            donjaMeda += func(gX)*dx
        gX += dx
        dX += dx
    return gornjaMeda, donjaMeda

def trapezium(func,a,b,N):
    dx = (float(b)-float(a)) / float(N)
    gX = a + dx
    dX = a
    I = 0.0
    for i in range(N):
        I += ((func(gX)+func(dX))/2)*dx
        gX += dx
        dX += dx
    
    return I

def analytic(func,x1,x2):
    a = func(x2) - func(x1)

    return a

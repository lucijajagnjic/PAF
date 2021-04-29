import calculus
import matplotlib.pyplot as plt
import modul
import math
import numpy as np

def f4(x):
    return 5*x**3 - 2*x**2+2*x-3

xk = -2
xk2 = 2
hk = 0.1
xl1 = np.arange(xk,xk2,hk)
dl1 = []
for x in xl1:
    d = 15*x**2 - 4*x +2
    dl1.append(d)

a,b = calculus.deriviranje(f4,-2,2,0.1)
plt.plot(xl1,dl1)
plt.scatter(a,b, s = 5, c ='r')
plt.show()

def ftrig(x):
    return math.sin(2*x) - math.cos(x)
xt = -10
xt2 = 10
ht = 0.01
dl2 = []
xl2 = np.arange(xt,xt2,ht)

for x in xl2:
    d = math.cos(2*x)*2+math.sin(x)
    dl2.append(d)

c,d = calculus.deriviranje(ftrig,-10,10,0.1)
plt.plot(xl2,dl2)
plt.scatter(c,d, s = 1)
plt.show()
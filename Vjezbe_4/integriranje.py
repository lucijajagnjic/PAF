import calculus
import matplotlib.pyplot as plt
import modul
import math
import numpy as np

a = 0
b = 10

def f1(x):
    return x**2-4*x+2
def integ_f(x):
    return x**3/3-2*x**2+2*x

dlista = []
gornja = []
donja = []
trapezno = []
analiticko = []

dn = 50
for i in range(1,20):
    d = dn * i
    dlista.append(d)
   

for d in dlista:
    gm, dm = calculus.integriranje(f1,a,b,d)
    trap = calculus.integriranje(f1,a,b,d)
    analit = integ_f(b)-integ_f(a)
    gornja.append(gm)
    donja.append(dm)
    trapezno.append(trap)
    analiticko.append(analit)
    
plt.plot(dlista,gornja)
plt.plot(dlista,donja)
plt.plot(dlista,trapezno)
plt.plot(dlista,analiticko)

plt.show()
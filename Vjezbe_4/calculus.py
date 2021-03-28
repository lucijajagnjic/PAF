import math 
import numpy as np 

def derivacija(func,x,h):
    d = (func(h+x)-func(x-h))/(2*h)
    return d

def deriviranje(func,x1,x2,h):
    dlista = []
    xlista = np.arange(x1,x2,h)

    for x in xlista:
        d = derivacija(func,x,h)
        dlista.append(d)

    return xlista, dlista



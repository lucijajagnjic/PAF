import numpy as np 

def derivacija(func,x,h):
    d = (func(h+x)-func(x)) / h
    return d

def derivacija2 (func,x,h):
    d = (func(h+x)-func(x-h)) / (2*h)


def deriviranje(func,x1,x2,h,m=3):
    dlista = []
    xlista = np.arange(x1,x2,h)

    for x in xlista:
        if m == 3:
            d = derivacija2(func,h,x)
        elif m == 2:
            d = derivacija(func,h,x)
        else:
            print("Nema opcije.")
        dlista.append(d)

    return xlista, dlista

def integriranje(func,a,b,N):
    dx = (float(b)-float(a)) / float(N)
    xg = a
    xd = a + dx
    gm = 0
    dm = 0

    for i in range(N):
        gm += func(xg)*dx
        dm += func(xd)*dx
        xd += dx
        xg += dx

    return gm,dm

def integracija(func,a,b,N):
    dx = (b-a) / N
    xk = a
    suma = 0

    for i in range(N):
        suma += (func(xk) + func(xk + dx))
        xk += dx
    integ = (dx/2) * suma

    return integ
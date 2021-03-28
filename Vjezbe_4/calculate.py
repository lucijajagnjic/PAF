import calculus
import math
import matplotlib.pyplot as plt

h = 0.0002

def f1(x):
    return x*x-2*x

def f2(x):
    return math.sin(x)

def f3(x):
    return 5*x**3 - 2*x**2 + 2*x-3

print(calculus.derivacija(f1,2,h))
print(calculus.derivacija(f2,2,h))

lista3,lista4 = calculus.deriviranje(f3,-2,2,h)
plt.plot(lista3,lista4)
lista1,lista2 = calculus.deriviranje(f3,-2,2,0.1)
plt.scatter(lista1,lista2)
plt.show()
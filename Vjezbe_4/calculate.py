import calculus
import math
import matplotlib.pyplot as plt

h = 0.1

def f1(x):
    return x*x-2*x

def f2(x):
    return math.sin(x)

def f3(x):
    return 5*x**3 - 2*x**2 + 2*x-3

def f4(x):
    return 2*x**2 + 3

def der_f3(x):
    return 15*x**2 - 4*x + 2

def f5(x):
    return 2*(x**3/3) + 3*x

print(calculus.derivacija(f1,2,h))
print(calculus.derivacija(f2,2,h))

lista1,lista2 = calculus.deriviranje(f3,-2,2,h)
plt.plot(lista1,lista2,".")
plt.xlabel('f(x)')
plt.ylabel('x')

a = -2
b = 2
lista3 = lista1.copy()
lista4 = []
while a < b:
    y = der_f3(a)
    lista4.append(y)
    a += h

plt.plot(lista3,lista4)
plt.show()

integral = calculus.integriranje(f4,0,1,3)
print(integral)
result = calculus.trapezium(calculus.f4,0,1,3)
print("Integral: {}.format(result)")

analyt = calculus.analytic(calculus.f5,0,1)
plt.axhline(y=analyt)

xX = []
gY = []
dY = []
dots = []
x = 0

for i in range(20):
    x += 50
    xX.append(x)
    integral = calculus.integriranje(calculus.f4, 0, 1, x)
    result = calculus.trapezium(calculus.f4, 0, 1, x)
    gY.append(integral)
    dY.append(integral)
    dots.append(result)
plt.plot(xX, gY, ".")
plt.plot(xX, dY, ".")
plt.plot(xX, dots, ".")
plt.ylabel('Integral')
plt.xlabel('N steps')
plt.title("Numerička integracija  $f(x) = 5x^3 - 2x^2 + 2x - 3$")
plt.show()
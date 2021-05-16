import Projectile2 as prt
import matplotlib.pyplot as plt

p1 = prt.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)

p1.__init__(60, 15, 0.01, 0, 0, 1, 1.56, 1, 1)
p2 = prt.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p2.__init__(60, 15, 0.01, 0, 0, 1, 1.56, 3, 1)
p3 = prt.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p3.__init__(60, 15, 0.01, 0, 0, 1, 1.56, 6, 1)
lista1, lista2 = p1.eulerovaMetoda()
lista3, lista4 = p2.eulerovaMetoda()
lista5, lista6 = p3.eulerovaMetoda()

plt.plot(lista1, lista2)
plt.plot(lista3, lista4)
plt.plot(lista5, lista6)
plt.pause(5)
plt.show

p1.reset()
p2.reset()
p3.reset()

p1 = prt.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.56, 1, 1)
p2 = prt.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p2.__init__(60, 15, 0.01, 0, 0, 2, 1.56, 1, 1)
p3 = prt.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0)
p3.__init__(60, 15, 0.01, 0, 0, 3, 1.56, 1, 1) 
lista1, lista2 = p1.eulerovaMetoda()
lista3, lista4 = p2.eulerovaMetoda()
lista5, lista6 = p3.eulerovaMetoda()

plt.plot(lista1, lista2)
plt.plot(lista3, lista4)
plt.plot(lista5, lista6)
plt.pause(5)
plt.show

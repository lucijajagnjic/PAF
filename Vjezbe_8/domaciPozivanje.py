import domaciRad as pr
import matplotlib.pyplot as plt

p1 = pr.Projectile(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
p1.__init__(60, 15, 0.01, 0, 0, 1, 1.29, 1, 0, 2)
lista1, lista2 = p1.sfera()
lista3, lista4 = p1.kocka() 
lista5, lista6 = p1.kocka2() 

plt.plot(lista1, lista2)
plt.plot(lista3, lista4)
plt.plot(lista5, lista6)
plt.pause(15)
plt.show
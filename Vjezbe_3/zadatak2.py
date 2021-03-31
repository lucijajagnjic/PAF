import math
import matplotlib.pyplot as plt 
import particle

dt_l = []
greska = []
p = particle.Particle(10, 60, 0, 0)
dt = 0
promjena = 0.001

for i in range(1000):
    dt = dt + promjena
    graf = math.fabs(((p.range(dt)-p.analitickoRacunanje())/p.analitickoRacunanje())*100)
    dt_l.append(dt)
    greska.append(graf)
    p.reset()

plt.plot(dt_l,greska)
plt.show()   
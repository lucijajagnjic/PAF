import math
import matplotlib.pyplot as plt 
import particle as prt

dt_l = []
greska = []
p = prt.Particle(10,60,0,0)
dt = 0
 
for i in range(100):
    
    p = prt.Particle(10,60,0,0)
    dt += 0.001
    gr = math.fabs(((p.range(dt)-p.analitickoRacunanje())/p.analitickoRacunanje())*100)
    dt_l.append(dt)
    pogreska.append(gr)
    p.reset()
plt.plot(dt_l,pogreska)
plt.show()
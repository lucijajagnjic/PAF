import universe as uni
import numpy as np
import matplotlib.pyplot as plt

au = 1.486*(10**11)
day = 60*60*24
year = 365.242*day

Sun = uni.Planet("Sunce","yellow",1.989 * (10**30),np.array((0,0)),np.array((0,0))) 
Mercury = uni.Planet("Merkur","orange",3.3 * (10**24),np.array((-47362,0)),np.array((0,0.466*au)))
Venus = uni.Planet("Venera","red",4.8685 * (10**24),np.array((0,35020)),np.array((0.723*au,0)))
Earth = uni.Planet("Zemlja","blue",5.9742 * (10**24),np.array((0,-29783)),np.array((-1*au,0)))
Mars = uni.Planet("Mars","brown",6.417 * (10**23),np.array((24007,0)),np.array((0,-1.667*au)))

p = uni.Universe()
p.addPlanet(Sun)
p.addPlanet(Mercury)
p.addPlanet(Venus)
p.addPlanet(Earth)
p.addPlanet(Mars)


p.interact(5*year)

plt.figure("Solar system", figsize = (8,8))
plt.plot(Sun.x_,Sun.y_, c = Sun.color, label = Sun.name, linewidth = 2)
plt.plot(Mercury.x_,Mercury.y_, c = Mercury.color, label = Mercury.name)
plt.plot(Venus.x_,Venus.y_, c = Venus.color, label = Venus.name)
plt.plot(Earth.x_,Earth.y_, c = Earth.color, label = Earth.name)
plt.plot(Mars.x_,Mars.y_, c = Mars.color, label = Mars.name)

plt.scatter(Mercury.x_[-1],Mercury.y_[-1], c = Mercury.color)
plt.scatter(Venus.x_[-1],Venus.y_[-1], c = Venus.color)
plt.scatter(Earth.x_[-1],Earth.y_[-1], c = Earth.color)
plt.scatter(Mars.x_[-1],Mars.y_[-1], c = Mars.color)

plt.show()
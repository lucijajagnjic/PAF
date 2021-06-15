import universe as uni
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

au = 1.486*(10**11)
day = 60*60*24
year = 365.242*day

Sun = uni.Planet("Sun","yellow",1.989 * (10**30),np.array((0,0)),np.array((0,0))) 
Mercury = uni.Planet("Mercury","orange",3.3 * (10**24),np.array((-47362,0)),np.array((0,0.466*au)))
Venus = uni.Planet("Venus","red",4.8685 * (10**24),np.array((0,35020)),np.array((0.723*au,0)))
Earth = uni.Planet("Earth","blue",5.9742 * (10**24),np.array((0,-29783)),np.array((-1*au,0)))
Mars = uni.Planet("Mars","brown",6.417 * (10**23),np.array((24007,0)),np.array((0,-1.667*au)))
Comet = uni.Planet("Comet", "black", 10**14, np.array((20000,-15000)), np.array((-4*au,4*au)))


p = uni.Universe() 
p.addPlanet(Sun)
p.addPlanet(Mercury)
p.addPlanet(Venus)
p.addPlanet(Earth)
p.addPlanet(Mars)
p.addPlanet(Comet)

p.interact(5*year)

fig = plt.figure("Sunvec sustav") 
axis = plt.axes(xlim = (-2*au,2*au),
                ylim = (-2*au,2*au)) 

axis.plot(Sun.x_,Sun.y_, c = Sun.color, label = Sun.name, linewidth = 2)
axis.plot(Mercury.x_,Mercury.y_, c = Mercury.color, label = Mercury.name)
axis.plot(Venus.x_,Venus.y_, c = Venus.color, label = Venus.name)
axis.plot(Earth.x_,Earth.y_, c = Earth.color, label = Earth.name)
axis.plot(Mars.x_,Mars.y_, c = Mars.color, label = Mars.name)
axis.plot(Comet.x_,Comet.y_, c = Comet.color, label = Comet.name)

lines = []
planets = [Sun, Mercury, Venus, Earth, Mars, Comet]

for obj in planets:
    line = axis.plot([],[], "o" , c = obj.color)[0]
    lines.append(line)
   
def init():
    for line in lines: 
        line.set_data([], []) 
    return lines

def animate(i):
    for index, obj in enumerate(planets):
        x = obj.x_[i] 
        y = obj.y_[i]
        lines[index].set_data(x,y) 
      
    return lines
     
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                               frames = len(Earth.x_), interval = 25) 


plt.show()
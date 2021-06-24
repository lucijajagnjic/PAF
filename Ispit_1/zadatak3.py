import matplotlib.pyplot as plt 
import zadatak1 as zad1 

b1 = zad1.Bullet()
b1.init(2, 100, 0, 0)
b1.gibanje(0.01)

plt.subplot(311)
plt.plot(b1.y, b1.x)
plt.subplot(312)
plt.plot(b1.t, b1.x)
plt.subplot(313)
plt.plot(b1.t, b1.y)
plt.show()

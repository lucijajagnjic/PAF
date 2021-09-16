import zadatak1 as z1 
import matplotlib.pyplot as plt

p = z1.Pendulum(20, 5, 1, 0.01)
theta, t = p.oscillate(5)

plt.plot(t, theta)
plt.title("Graf ovisnosti kuta otklona o vremenu")
plt.show()
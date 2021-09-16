import zadatak1 as z1 
import matplotlib.pyplot as plt

p = z1.Pendulum(20, 5, 1, 0.05)
theta, t = p.oscillate_ar(5, 1000, 5, 0.1)

plt.plot(t, theta)
plt.title("Graf ovisnosti kuta otklona o vremenu uz otpor zraka")
plt.show()
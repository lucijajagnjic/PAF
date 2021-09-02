import matplotlib as plt
import zadatak1 as z1 

p1 = z1.Pendulum(9, 14, 5)
p1.runEvent(2)

p3 = z1.Pendulum(9, 1, 0.01)
p3.oscillate(0.01, 5)
p3.period(0.01, 5)
p3.plot_trajectory(0.01, 5)



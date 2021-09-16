import zadatak1 as z1 


p = z1.Pendulum(20, 5, 1, 0.05)
p.oscillate_ar(5, 1000, 5, 0.1)
p.stopping(1000, 5, 0.1)
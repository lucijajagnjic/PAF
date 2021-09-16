import zadatak1 as z1 

p = z1.Pendulum(20, 5, 1, 0.01)
p.change_theta("rad", 40)

p_ = z1.Pendulum(5, 2, 1, 0.01)
p_.change_theta("deg", 50)
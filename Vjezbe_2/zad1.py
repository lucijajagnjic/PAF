import matplotlib.pyplot as plt
F = float(input("Sila u N:"))
m = float(input("Masa u kg: "))
g = 9.8
a = F/m 
dt = 0.1
t = 0
v = 0
x = 0
brzina = []
pomak = []
vrijeme = []
akceleracija = []
for i in range(100): #t konacno je 10, a dt je 0.1 pa range mora biti 100
    v = v + a*dt
    x = x + v*dt
    t += dt
    brzina.append(v)
    pomak.append(x)
    vrijeme.append(t)
    akceleracija.append(a)

plt.subplot(311)
#prvi broj-br redova; drugi broj-br stupaca; treci broj-polozaj
plt.plot(vrijeme,pomak)
plt.subplot(312)
plt.plot(vrijeme, brzina)
plt.subplot(313)
plt.plot(akceleracija,vrijeme)

plt.show()
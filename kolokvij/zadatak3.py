import zadatak1 as zad1
import matplotlib.pyplot as plt 
import math

dt = 0.01
N = int(t/dt)
t = 0
vlista = []
hlista = []
tlista = []
    

for i in range(N):
    v =
    h =
    t += dt

    vlista.append(v)
    hlista.append(h)
    tlista.append(t)

plt.subplot(311)
plt.plot(hlista, tlista)

plt.subplot(312)
plt.plot(vlista, tlista)

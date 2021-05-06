import math
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, k, m, x0, v0):
        self.Xlista = []
        self.Vlista = []
        self.Alista = []
        self.Tlista = []
        self.k = k
        self.m = m
        self.x = x0
        self.v = v0
        self.a = -(self.k * self.x) / self.m
        self.t = 0
        self.Xlista.append(self.t)
        self.Vlista.append(self.a)
        self.Alista.append(self.x)
        self.Tlista.append(self.v)


    def oscillate(self, dt, t):
        N = int(t/dt)
        
        for i in range(N):
            self.a = -(self.k * self.x) / self.m
            self.v = self.v + self.a * dt
            self.x = self.x + self.v * dt
            self.t += dt
            self.Xlista.append(self.x)
            self.Vlista.append(self.v)
            self.Alista.append(self.a)
            self.Tlista.append(self.t)

        return self.Xlista, self.Vlista, self.Alista, self.Tlista

    def plot_trajectory(self, dt, t):
        x,v,a,t = self.oscillate(dt,t)
        plt.subplot(1,3,1)
        plt.plot(t,x)

        plt.subplot(1,3,2)
        plt.plot(t,v)

        plt.subplot(1,3,3)
        plt.plot(t,a)

        plt.show()

    def reset(self):
        del self.k
        del self.m
        del self.x
        del self.v
        del self.a
        del self.t
        del self.Xlista
        del self.Vlista
        del self.Alista
        del self.Tlista

    def preciznost(self, dt, t=2):
        self.oscillate(dt,t)
        plt.scatter(self.Tlista,self.Xlista)

    def analitickoRacunanje(self, dt, t1=2):
        self.Xlista = []
        self.Tlista = []
        self.omega = math.sqrt(self.k/self.m)
        self.t = 0

        while self.t <= t1:
            x = self.x * math.cos(self.omega*self.t)
            self.t += dt
            self.Xlista.append(x)
            self.Tlista.append(self.t)

        return self.Xlista, self.Tlista

    def period(self, dt, t):
        A = self.x
        T = 0
        self.oscillate(dt,t)
        for x in self.Xlista:
                if x > 0:
                    T += dt
                else:
                    break
        print(4*T)

    def T_analiticki(self):
        T = 2 * math.pi * math.sqrt(self.m / self.k)
        print(T)


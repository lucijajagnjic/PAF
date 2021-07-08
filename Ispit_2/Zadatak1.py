from math import radians, pi, sqrt
import matplotlib.pyplot as plt
import numpy as np

class Pendulum:
    def __init__(self, theta, l, m):
        self.theta = theta
        self.l = l
        self.m = m
        self.__podaci__(theta, l, m)

    def __podaci__(self, theta, l, m):
        print("Kut otklona je {}, duljina niti {}, a masa kuglice {}.".fomrat(theta, l, m))

    def __provjeraKuta__(self, theta):

        if self.theta > 10:
            print("Kut otklona je velik, veci je od 10 stupnjeva.")
        else:
            print("Kut oklona je malen, manji od 10 stupnjeva.")

    def pendulum_sim(self, theta, t, l, m, b=0, g=9.81):
        self.theta = radians(theta)
        theta1 = self.theta[1]
        theta2 = -b/self.m*self.theta[1] - g/self.l*np.sin(self.theta[0])

        return theta1, theta2

    def pendulum_sim(self, theta, t, l, m, b=0, g=9.81):
        self.theta = (theta/360)*2*pi
        theta1 = self.theta[1]
        theta2 = -b/self.m*self.theta[1] - g/self.l*np.sin(self.theta[0])

        return theta1, theta2

    def eulrovaMetoda(self, l, m, k):
        self.k =  k
        for i in range(5):
            self.m = (self.l * self.k) / 9.81
            self.k = (self.m * 9.81) / self.l
            self.l = (self.m * 9.81) / self.k
            self.Mlista.append(self.m)
            self.Klista.append(self.k)
            self.Llista.append(self.l)


        return self.Mlista, self.Klista, self.Llista

    def eulrovaMetodaOZ(self, l, m, k, S, C = 0.47, rho = .128):
        self.k = k
        self.S = S
        for i in range(5):
            self.m = (self.l * self.k) / 9.81 * self.C * self.rho * self.S
            self.k = (self.m * self.C * self.rho * self.S * 9.81) / self.l
            self.l = (self.m * self.C * self.rho * self.S * 9.81) / self.k
            self.Mlista.append(self.m)
            self.Klista.append(self.k)
            self.Llista.append(self.l)

    def period(self, l):
        T = 2*pi*sqrt(self.l/9.81)
        if T > 0:
            print("Vrijeme je {}.".format(t))
        else:
            break
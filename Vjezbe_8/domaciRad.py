import matplotlib.pyplot as plt
import math
import numpy as np

class Projectile:
    def __init__(self, theta, v0, dt, x, y, m, rho, Cd, S, r):
        self.theta =(theta/180)*math.pi
        self.kx = math.cos(self.theta)
        self.ky = math.sin(self.theta)
        self.v0 = v0
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        self.dt = dt
        self.x = x
        self.y = y
        self.m = m
        self.rho = rho
        self.Cd = Cd
        self.S = S
        self.r = r

    def reset(self):
        self.v0 = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.dt = 0.0
        self.x = 0.0
        self.y = 0.0
        self.m = 0.0
        self.rho = 0.0
        self.Cd = 0.0
        self.S = 0.0
        self.theta = 0.0
        self.kx = 0.0
        self.ky = 0.0
        self.r = 0.0

    def eulerovaMetoda(self):
        t = 0
        self.xSmjer = []
        self.ySmjer = []
        for i in range(1000):
            ax = - np.sign(self.vx) * ((self.rho*self.Cd*self.S)/2*self.m) * (self.vx)**2
            self.vx = self.vx + ax * self.dt 
            self.x = self.x + self.vx * self.dt
            self.xSmjer.append(self.x)
            ay = - 9.81 - np.sign(self.vy)*((self.rho*self.Cd*self.S)/2*self.m)*(self.vy)**2
            self.vy = self.vy + ay * self.dt 
            self.y = self.y + self.vy * self.dt
            self.ySmjer.append(self.y)

            if self.y <= 0:
                break

        return(self.xSmjer, self.ySmjer)

    def _akeceleracijaX(self, o):
        return (np.sign(self.vx + o) * ((self.rho*self.Cd*self.S)/2*self.m) * (self.vx + o)**2)
       
    def _akceleracijaY(self, o):
        return (9.81 - np.sign(self.vy + o)*((self.rho*self.Cd*self.S)/2*self.m)*(self.vy + o)**2)

    def rungeKutta(self):
        self.x2Smjer = []
        self.y2Smjer = []
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        self.x = 0
        self.y = 0

        for i in range(1000):
            k1v = self._ax(0) * self.dt
            k1x = self.vx * self.dt 
            k2v = self._ax(k1v/2) * self.dt
            k2x = (self.vx + (k1v/2)) * self.dt 
            k3v = self._ax(k2v/2) * self.dt 
            k3x = (self.vx + (k2v/2)) * self.dt
            k4v = self._ax(k3v) * self.dt 
            k4x = (self.vx + k3v) * self.dt 
            self.vx = self.vx + (1/6) * (k1v + 2*k2v + 2*k3v + k4v)
            self.x = self.x + (1/6) * (k1x + 2*k2x + 2*k3x + k4x)
            self.x2Smjer.append(self.x)
            
            k1vy = self._ay(0) * self.dt
            k1y = self.vy * self.dt 
            k2vy = self._ay(k1vy/2) * self.dt 
            k2y = (self.vy + (k1vy/2)) * self.dt 
            k3vy = self._ay(k2vy/2) * self.dt 
            k3y = (self.vy + (k2vy/2)) * self.dt
            k4vy = self._ay(k3vy) * self.dt 
            k4y = (self.vy + k3vy) * self.dt 
            self.vy = self.vy + (1/6) * (k1vy + 2*k2vy + 2*k3vy + k4vy)
            self.y = self.y + (1/6) * (k1y + 2*k2y + 2*k3y + k4y)
            self.y2Smjer.append(self.y)

            if self.y <= 0:
                break
        return(self.x2Smjer, self.y2Smjer)

    def range(self): 
        x = self.x
        self.rungeKutta()
        d = self.x - x
        return d
    
    def plot_trajectory(self):
        plt.plot(self.x_smjer, self.y_smjer)
        plt.pause(5)
        plt.close 

    def sOtporomZraka(self):   
        while self.y >= 0:
            self.rungeKutta()
        return self.x2Smjer, self.y2Smjer

    def sfera(self):
        self.S = math.pi * self.r**2
        lista1, lista2 = self.eulerovaMetoda()
        return(lista1, lista2)

    def kocka(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        a = math.sqrt(math.pi)*self.r
        self.S = a**2
        lista3, lista4 = self.eulerovaMetoda()
        return(lista3, lista4)

    def kocka2(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0 * self.kx
        self.vy = self.v0 * self.ky
        a = math.sqrt(math.pi)*self.r
        b = 90 - self.theta
        c = a / math.cos(b)
        self.S = a*c
        lista5, lista6 = self.eulerovaMetoda()
        return(lista5, lista6)

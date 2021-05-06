from math import pi, cos, sin, sqrt, radians
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, alfa, x0, y0):
        self.v0 = v0
        self.alfa = radians(alfa)
        self.x = x0
        self.y = y0
        self.x_ = []
        self.y_ = []
        self.x_.append(x0)
        self.y_.append(y0)
        self.vx = v0 * cos(self.alfa)
        self.vy = v0 * sin(self.alfa)
        self.t = 0
        self.vy_ = []

    def printInfo(self):
        print(self.v0,self.alfa,self.x,self.y)

    def reset(self):
        self.v0 = 0
        self.alfa = 0
        self.x0 = 0
        self.y0 = 0
        self.x_ = []
        self.y_ = []
        self.vy_ = []

    def __move(self, dt):
        self.x = self.x + self.vx * dt
        self.vy = self.vy - 9.81 * dt
        self.y = self.y + self.vy * dt
        self.x_.append(self.x)
        self.y_.append(self.y)
        self.vy_.append(self.vy)
       
       
    def range(self,dt):
        x = self.x
        while True:
            self.__move(dt)
            if self.y <= 0:
                break
                
        return self.x - x

    def plotTrajectory(self):
        plt.plot(self.x_,self.y_)
        plt.show()

    def analitickoRacunanje(self):
        domet = (self.v0**2*sin(2*self.alfa))/9.81
        return domet
from math import pi, cos, sin
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, alfa, x0, y0):
        self.v0 = v0
        self.alfa = (alfa/360)*2*pi
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.vx = v0 * cos(self.alfa)
        self.vy = v0 * sin(self.alfa)
        self.x_ = []
        self.y_ = []

    def printInfo(self):
        print("v0 = {0:.2f}, alfa = {1:.2f}, x0 = {2:.2f}, y0 = {3:.2f}".format(self.v0, self.alfa, self.x0, self.y0))

    def reset(self):
        self.v0 = 0
        self.alfa = 0
        self.x0 = 0
        self.y0 = 0
        self.vx = 0
        self.vy = 0

    def __move(self, dt):
       self.vy = self.vy - 9.81 * dt
       self.x = self.x + self.vx * dt
       self.y = self.y + self.vy * dt
       self.x_.append(self.x)
       self.y_.append(self.y)
       
       
       def range(self):
           x = self.x
           while True:
               self.__move(0.1)
               if self.y <= 0:
                   break
            
            print(self.x - x)

        def plotTrajectory(self):
            plt.plot(self.x_,self.y_)
            plt.show()

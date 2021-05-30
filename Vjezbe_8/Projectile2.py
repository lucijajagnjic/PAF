import matplotlib.pyplot as plt
import math as m
from math import pi, cos, sin
import numpy as np

class Projectile:
    def __init__(self, theta, v0, S, m, p, q, r, t, dt = 0.01, C = 0.47, rho = 1.28):
        self.x = 0
        self.y = 0
        self.m = m
        self.theta =(theta/180)*pi
        self.v0 = v0
        self.dt = dt
        self.t = 0
        self.ax = 0
        self.ay = 0
        self.x_ = []
        self.y_ = []
        self.x_x = []
        self.y_y = []
        self.d_ = []
        self.vx = v0 * cos(self.theta)
        self.vy = v0 * sin(self.theta)
        self.S = S 
        self.C = C
        self.rho = rho
        self.g = 9.81
        self.p = p
        self.q = q
        self.r = r
        self.d = 0


    def reset(self):
        self.x = 0
        self.y = 0
        self.v0 = 0
        self.tehta = 0
        self.dt = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.p = 0
        self.q = 0
        self.r = 0
        self.d = 0
        self.x_ = []
        self.y_ = []
        self.x_x = []
        self.y_y = []
        self.d_ = []


    def eulerovaMetoda_otporZ(self):
        while self.y >= 0:
            self.vx += self.ax * self.dt 
            self.x += self.vx * self.dt
            self.ax = - abs((self.vx ** 2) * self.rho * self.C * self.S) / (2*self.m)
            self.x_.append(self.x)

            self.vy += self.ay * self.dt      
            self.y += self.vy * self.dt
            self.ay = - self.g - abs((self.vy ** 2) * self.rho* self.C * self.S) / (2*self.m)
            self.y_.append(self.y)

    def _akeceleracijaX(self, vx):
        return (- abs((self.vx**2) * self.rho * self.C * self.S) / (2*self.m))
       
    def _akceleracijaY(self, vy):
        return (- self.g - abs((self.vy ** 2) * self.rho * self.C * self.S) / (2*self.m))

    def rungeKutta(self):
            k1vx = self._akeceleracijaX(self.vx) * self.dt
            k1x = self.vx * self.dt 
            k2v = self._akeceleracijaX(k1v/2) * self.dt
            k2vx = (self.vx + (k1vx/2)) * self.dt 
            k3vx = self._akeceleracijaX(self.vx + (self.k2v/2)) * self.dt 
            k3x = (self.vx + (k2vx/2)) * self.dt
            k4vx = self._akeceleracijaX(self.vx + k3vx) * self.dt 
            k4x = (self.vx + k3vx) * self.dt 
            self.vx += (1/6) * (k1vx + 2*k2vx + 2*k3vx+ k4vx)
            self.x += (1/6) * (k1x + 2*k2x + 2*k3x + k4x)
            self.x_x.append(self.x)
            
            k1vy = self._akceleracijaY(self.vy) * self.dt
            k1y = self.vy * self.dt 
            k2vy = self._akceleracijaY(self.vy + (k1vy/2)) * self.dt 
            k2y = (self.vy + (k1vy/2)) * self.dt 
            k3vy = self._akceleracijaY(self.vy + (k2vy/2)) * self.dt 
            k3y = (self.vy + (k2vy/2)) * self.dt
            k4vy = self._akceleracijaY(self.vy + k3vy) * self.dt 
            k4y = (self.vy + k3vy) * self.dt 
            self.vy += (1/6) * (k1vy + 2*k2vy + 2*k3vy + k4vy)
            self.y += (1/6) * (k1y + 2*k2y + 2*k3y + k4y)
            self.y_y(self.y)

    def otporZrakaRK(self):
        while self.y >= 0:
            self.rungeKutta()
        return self.x_x, self.y_y


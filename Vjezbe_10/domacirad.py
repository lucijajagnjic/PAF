import Particle as prt
import numpy as np
import matplotlib.pyplot as plt

def __akceleracija2(self, v0, Bz):
    self.B = np.array([0.0, 0.0, Bz])
    return (self.q / self.m) * (np.add(self.E, np.cross(v0, self.B)))


def moveE2(self, T):
    self.Bz = 0.0
    while self.t <= T:            
        self.Bz = self.t / 10
        self.a = self.__akceleracija2(self.v0, self.Bz)
        self.v0 = np.add(self.v0, self.a * self.dt)
        self.r = np.add(self.r, self.v0 * self.dt)
        self.x_x1.append(self.r[0])
        self.y_y1.append(self.r[1])
        self.z_z1.append(self.r[2])
        self.t += self.dt
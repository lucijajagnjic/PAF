import math as m
import numpy as np
import matplotlib.pyplot as plt


class ElMangnPolje:

    def init(self, m, q, r, v0, B, E, dt = 0.01):
        self.m = m
        self.q = q
        self.dt = dt       
        self.r = r
        self.v0 = v0
        self.B = B
        self.E = E
        self.a = 0.0
        self.t = 0.0
        self.x_ = []
        self.y_ = []
        self.z_ = []
        self.x_x = []
        self.y_y = []
        self.z_z = []
        self.x_x1 =[]
        self.y_y1 = []
        self.z_z1 = []

    def reset(self):
        self.m = 0.0
        self.q = 0.0
        self.r = 0.0
        self.v0 = 0.0
        self.B = 0.0
        self.E = 0.0
        self.a = 0.0
        self.t = 0.0
        self.dt = 0.0
        self.x_.clear()
        self.y_.clear()
        self.z_.clear() 
        self.x_x.clear()
        self.y_y.clear()
        self.z_z.clear()
        self.x_x1.clear()
        self.y_y1.clear()
        self.z_z1.clear()      

    def moveE(self, T):
        while self.t <= T:
            self.a = (self.q / self.m) * (np.add(self.E, np.cross(self.v0, self.B)))
            self.v0 = np.add(self.v0, self.a * self.dt)
            self.r = np.add(self.r, self.v0 * self.dt)
            self.x_.append(self.r[0])
            self.y_.append(self.r[1])
            self.z_.append(self.r[2])
            self.t += self.dt

    def __akceleracija(self, v0):
        return (self.q / self.m) * (np.add(self.E, np.cross(v0, self.B)))

    def moveR(self, T):
        while self.t <= T:
            k_1v0 = np.dot((self.__akceleracija(self.v0)), self.dt)
            k_1r = np.dot(self.v0, self.dt)
            k_2v0 = np.dot(self.__akceleracija(np.add(self.v0, (k_1v0 / 2))), self.dt)
            k_2r = np.dot(np.add(self.v0, k_1v0 / 2), self.dt)
            k_3v0 = np.dot(self.__akceleracija(np.add(self.v0, (k_2v0 / 2))), self.dt)
            k_3r = np.dot(np.add(self.v0, (k_2v0 / 2)), self.dt)
            k_4v0 = np.dot(self.__akceleracija(np.add(self.v0, k_3v0)), self.dt)
            k_4r = np.dot(np.add(self.v0, k_3v0), self.dt)
            self.v0 = np.add(self.v0, (1/6) * np.add(np.add(k_1v0, 2*k_2v0), np.add(2*k_3v0, k_4v0)))
            self.r = np.add(self.r, (1/6) * np.add(np.add(k_1r, 2*k_2r), np.add(2*k_3r, k_4r)))           
            self.x_x.append(self.r[0])
            self.y_y.append(self.r[1])
            self.z_z.append(self.r[2])
            self.t += self.dt

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
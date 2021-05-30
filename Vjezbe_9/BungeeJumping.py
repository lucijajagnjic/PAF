import math as m

class BungeeJumping:

    def init(self, m, k, h0, l, v0, S, dt = 0.001, C = 0.47, rho = 1.28):
        self.m = m
        self.k = k
        self.h0 = h0
        self.y = h0
        self.l = l
        self.v0 = v0
        self.S = S
        self.C = C
        self.rho = rho
        self.dt = dt
        self.g = 9.81
        self.a = 0.0
        self.d = 0.0
        self.t = 0.0
        self.U = 0.0
        self.K = 0.0
        self.Eel = 0.0
        self.E = 0.0
        self.U_ = []
        self.K_ = []
        self.Eel_ = []
        self.E_ = []
        self.t_ = []
        self.y_ = []

    
    def reset(self):
        self.m = 0
        self.k = 0
        self.h0 = 0
        self.y = 0
        self.l = 0
        self.v0 = 0
        self.S = 0
        self.dt = 0
        self.C = 0
        self.rho = 0
        self.a = 0
        self.d = 0
        self.t = 0
        self.U = 0
        self.K = 0
        self.Eel= 0
        self.E = 0
        self.t_ = 0
        self.y_ = 0
        self.U_ = 0
        self.K_ = 0
        self.Eel_ = 0
        self.E_ = 0


    def __potencijalnaE(self, d):
        return (self.g * self.m * d)


    def __kinetickaE(self):
        return (self.m * (self.v0**2)) / 2


    def __elasticnaE(self, d):
        if d > 0.0:
            Eel = (self.k * (d**2)) / 2
        else:
            Eel = 0.0
        return Eel


    def __ukupnaE(self):
        return (self.U + self.K + self.Eel)


    def __akceleracija(self, d, v0):   
        if d > 0:
            aEl = (self.k/self.m) * d
        else:
            aEl = 0
        if v0 > 0:
            aAr = - abs((v0**2) * self.rho * self.C * self.S) / (2*self.m)
        else:
            aAr = abs((v0**2) * self.rho * self.C * self.S) / (2*self.m)
        return (-self.g + aEl + aAr)


    def move(self, T):
        while self.t <= T:
            self.d = self.h0 - self.l - self.y
            self.a = self.__akceleracija(self.d, self.v0)  
            self.v0 += self.a * self.dt
            self.y += self.v0 * self.dt

            self.t += self.dt
            self.y_.append(self.y)
            self.t_.append(self.t)

            self.U = self.__potencijalnaE(self.y)
            self.K = self.__kinetickaE()
            self.Eel = self.__elasticnaE(self.d)
            self.U_.append(self.U)
            self.K_.append(self.K)
            self.Eel_.append(self.Eel)
            self.E = self.__ukupnaE()
            self.E_.append(self.E) 
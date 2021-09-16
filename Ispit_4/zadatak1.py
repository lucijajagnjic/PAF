import math 

class Pendulum:
    def __init__(self, theta, l, m, dt):
        self.theta = theta
        self.theta0 = theta
        self.l = l
        self.m = m
        self.__kut()
        self.dt = dt
        self.t = 0
        self.omega = 0
        self.thetal = []
        self.thetal.append(self.theta)
        self.tl = []
        self.tl.append(self.t)
        print("Pocetni kut je", self.theta, "duljina niti je", self.l, "masa kuglice  je", self.m)

    def __kut(self):
        if self.theta < 10:
            print("Theta je mali kut, manji od 10 stupnjeva.")
        else:
            print("Theta je veliki kut, veci od 10 stupnjeva.")

    def change_theta(self, mjerna_jedinica, theta):
        self.theta = theta
        if mjerna_jedinica == "rad":
            print("Novi kut je", self.theta,"radijana.")
        elif mjerna_jedinica == "deg":
            print("Novi kut je", self.theta, "stupnjeva.")
        self.__kut()
        if self.theta < self.theta0:
            print("Novi kut je manji od starog.")
        else:
            print("Novi kut je veci od starog.")

    def __oscillate(self):
        self.alpha = -9.81 * math.sin(self.theta)
        self.omega = self.omega + self.alpha * self.dt
        self.theta = self.theta + self.omega * self.dt
        self.t = self.t + self.dt

        self.thetal.append(self.theta)
        self.tl.append(self.t)

    def oscillate(self, t):
        while self.t <= t:
            self.__oscillate()

        return self.thetal, self.tl

    def __oscillate_ar(self):
        self.alpha = abs(self.omega * self.l * ro  * cd  * A  * math.sin(self.theta) / 2*self.m - 9.81) * math.sin(self.theta) 
        self.omega = self.omega + self.alpha * self.dt
        self.theta = self.theta + self.omega * self.dt
        self.t = self.t + self.dt

        self.thetal.append(self.theta)
        self.tl.append(self.t)

    def oscillate_ar(self, t, ro, cd, A):
        while self.t <= t:
            self.__oscillate()

        return self.thetal, self.tl


    def stopping(self, ro, cd, A):
        while self.omega >= 0:
                self.__oscillate_ar()
        print("Vrijeme potrebno da se zaustavi je" , self.t)


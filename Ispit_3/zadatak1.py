from math import pi, radians 
import matplotlib as plt

class Pendulum:
    def __init__(self, theta, l, m):
        self.thetal = []
        self.ll = []
        self.ml = []
        self.tl = []
        self.xl = []
        self.theta = theta
        self.l = l
        self.m = m
        self.t = 0
        self.x = 0
        self.thetal.append(self.theta)
        self.ll.append(self.l)
        self.ml.append(self.m)
        self.tl.append(self.t)
        self.xl.append(self.x)

    def printInfo(self):
        print(self.theta, self.l, self.m)

    def __kut__(self, tehta):
        if self.theta > 10:
            print("Radi se o velimom kutu:")
        else:
            print("Radi se o malom kutu.")
        
    def runEvent(self, theta):
        self.__kut__(theta)

#znam da ne radi __stupnjevi, __radijani; pocevanjeSmanjenje, ali na taj nacin bi napravila 
    def __stupnjevi(self, theta):
        s = (self.theta/360)*2*pi
        return s

    def __radijani(self, theta):
        r = radians(self.theta)
        return r

    def povecanjeSmanjenje(self, theta):
        self.__stupnjevi(theta)
        self.__radijani(theta)

        while True():
            m = int(input("Unesi odabir radijani ili stupnjevi, za radijanje 1, za stupnjeve 2."))

            if m == 1:
                r = __radijani(theta)
                print("Kut je u radijanima.")
            elif m == 2:
                s = __stupnjevi(theta)
                print("Kut je u stupnjevima.")
            else:
                print("Pogresan unos, treba biti 1 ili 2.")

            self.thetal.append(r, s)


    def oscillate(self, dt, t):
        N = int(t/dt)
        g = 9.81

        for i in range(N):
            self.t += dt
            self.theta = self.theta + g
            self.thetal.append(self.theta)

        return self.thetal


    def period(self, dt, t):
        A = self.x
        T = 0
        self.oscillate(dt,t)
        for x in self.xl:
                if x > 0:
                    T += dt
                else:
                    break
        print(4*T)    

    def plot_trajectory(self, dt, t):
        theta = self.oscillate(dt, t)
        plt.plot(theta, t)   

        plt.show()

    def oscillateUzOtporZraka(self, dt, t): 
        N = int(t/dt)
        g = 9.81

        for i in range(N):
            self.t += dt
            self.theta = self.theta + g * (-self.l/self.t)
            self.thetal.append(self.theta)


        return self.thetal

    def zaustavljanje(self, theta, t):
        

    






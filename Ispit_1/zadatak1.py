class Bullet:
    def __init__(self, h0, v0, x0, y0):
        self.h0 = h0
        self.h = self.h0
        self.v0 = v0
        self.v = self.v0
        self.t = 0
        self.x = x0
        self.y = y0
        self.h_ = []
        self.v_ = []
        self.t_ = []
        self.x_ = []
        self.y_ = []
        self.h_.append(h)
        self.v_.append(v)
        self.t_.append(t)
        self.x_.append(x)
        self.y_.append(y)
        self.vx = v0 * cos(self.alfa)
        self.vy = v0 * sin(self.alfa)
        self.vy_ = []

        print("Bullet je uspjesno stvoren.")
        print("Pocetna visina iznosi: {:.2f}m, a pocetna brzina: {:.2f}m/s".format(h0,v0))

    def __printInfo(self):
        print(self.h0, self.v0)

    def usporenjeUbrzanje(self, v2):
        self.v0 = v2
        self.v = self.v0
        print("Nova pocetna brzina iznosi: {:.2f}m/s".format(self.v0))
        
    def promjenaVisine(self, h2):
        self.h0 = h2
        self.h = self.h0
        print("Nova pocetna visina iznosi: {:.2f}m".format(self.h0))

    def gibanje(self, dt):
        self.x = self.x + self.vx * dt
        self.vy = self.vy - 9.81 * dt
        self.y = self.y + self.vy * dt
        self.x_.append(self.x)
        self.y_.append(self.y)
        self.vy_.append(self.vy)
        
    def range(self, dt):
        while True:
            self.gibanje(dt)
            if self.x == 0:
                break

        


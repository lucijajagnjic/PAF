import math
class Particle:
    def __init__(self, mass, x_0):
        self.mass = mass 
        self.x_0 = x_0

    def printInfo(self):
         print("Cestica ima masu {0:.2f} i u pocetnom trenutku se nalazi u polozaju x={1:.2f}.".format(self.mass, self.x_0))

    def udaljenostOdIspodista(self):
        x = math.fabs(self.x_0)
        print("Udaljenost od ishodista je {}".format(x))


p1 = Particle(10, -5) 
p1.printInfo()
p1.udaljenostOdIspodista()

p2 = Particle(20, -10)
p2.printInfo()
p2.udaljenostOdIspodista()
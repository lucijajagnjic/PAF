import Projectile2 as pro
import matplotlib.pyplot as plt
import numpy as np

p1 = pro.Projectile(0, 0, 0, 0, 0, 0, 0, 0.2)

p1.__init__(60, 10, 0.5, 10, 0, 0, 0, 0.2)
x1, y1 = p1.eulerovaMetoda_otporZ()
plt.plot(x1, y1)
p1.reset()

p1.__init__(60, 10, 0.5, 10, 0, 0, 0, 0)
x2, y2 = p1.otporZrakaRK()
plt.plot(x2, y2)
plt.legend()
plt.show()
p1.reset()
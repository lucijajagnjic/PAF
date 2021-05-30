import BungeeJumping as bng
import matplotlib.pyplot as plt

b0 = bng.BungeeJumping()
b0.init(70.0, 50.0, 200.0, 100.0, 0.0, 0.0, 0.001, 0.0, 0.0)
b0.move(50)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(b0.t_, b0.y_)

ax2.plot(b0.t_, b0.U_)
ax2.plot(b0.t_, b0.K_)
ax2.plot(b0.t_, b0.Eel_)
ax2.plot(b0.t_, b0.E_)

b0.reset()

b1 = bng.BungeeJumping()
b1.init(70.0, 50.0, 200.0, 100.0, 0.0, 0.125)
b1.move(50)

ax3.plot(b1.t_, b1.y_)

ax4.plot(b1.t_, b1.U_)
ax4.plot(b1.t_, b1.K_)
ax4.plot(b1.t_, b1.Eel_)
ax4.plot(b1.t_, b1.E_)
plt.show()
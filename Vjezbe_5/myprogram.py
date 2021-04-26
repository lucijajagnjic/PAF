import matplotlib.pyplot as plt
import harmonic_oscillator as ho

h1 = ho.HarmonicOscillator(10,0.1,0.3,0)
h1.preciznost(0.01)
h1.reset()
h1 = ho.HarmonicOscillator(10,0.1,0.3,0)
h1.preciznost(0.05)
h1.reset()
h1 = ho.HarmonicOscillator(10,0.1,0.3,0)
h1.preciznost(0.1)
h1.reset()
h1 = ho.HarmonicOscillator(10,0.1,0.3,0)
x,t= h1.analitickoRacunanje(0.01)
plt.plot(t,x)
plt.show()
h1.reset()
from math import sqrt
import matplotlib.pyplot as plt
def udaljenostTocke(x1,y1,x2,y2,r):
    plt.xlim([5,15]) #granica na x koor.
    plt.ylim([5,15]) #granica na y koor.
    kruznica = plt.circle((x2,y2),r)
    plt.gca().add_artist(kruznica) #na koor. osi dodaje kružnicu; gca-get current axes
    plt.plot(x1,y1)
    x = (x1-x2)**2 + (y1-y2)**2
    d = sqrt(x)
    oblik = int(input("Unesi '1' za prikaz slike, unesi '2' za spremanje."))
    if oblik == 1:
        plt.show()
    elif oblik == 2:
        ime = input("Unesi željeno ime slike: ")
        plt.savefig(f'{ime}.pdf')

    epsilon = 0.01
    if d < r:
        print(f'Točka je unutar kružnice, {d} je udaljenost.')
    elif r-epsilon < d < r+epsilon:
        print(f'Točka je na kružnici, {d} je udaljenost.')
    else:
        print(f'Točka je izvan kružnice, {d} je udaljenost.')
#određivanje položaja točke u odnosu na kružnicu

udaljenost = udaljenostTocke
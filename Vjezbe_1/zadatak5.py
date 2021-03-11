import matplotlib.pyplot as plt 
def odrediPravac(x1,y1,x2,y2,znak):
    #znak kao odabir hoce li biti slika ili znak
    xKoordinate = [x1,x2]
    yKoordinate = [y1,y2]
    plt.plot(xkoordinate,yKoordinate)
    if znak == 0:
        plt.show()
        #prikazuje na ekranu
    elif znak == 1:
        ime = input("Unesite ime slike: ")
        plt.savefig(f'{ime}.pdf')
        #sprema kao pdf

odrediPravac(1,2,6,5)
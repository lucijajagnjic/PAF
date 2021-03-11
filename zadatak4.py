def odrediPravac(x1,y1,x2,y2):
    k = (y2 - y1)/(x2 - x1)
    l = -k*x1+y1
    if l < 0:
        print(f" y = {k}x {l}")
    elif l == 0:
        print(f" y = {k}x")
    else:
        print(f" y = {k}x + {l}")
pravac = odrediPravac(3,4,6,7)
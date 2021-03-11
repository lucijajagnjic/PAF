x1 = float(input("Unesi koordinatu x1: "))
y1 = float(input("Unesi koordinatu y1: "))
x2 = float(input("Unesi koordinatu x2: "))
y2 = float(input("Unesi koordinatuz y2: "))
k = (y2 - y1)/(x2 - x1)
l = -k*x1+y1
if l < 0:
    print(f" y = {k}x {l}")
elif l == 0:
    print(f" y = {k}x")
else:
    print(f" y = {k}x + {l}")

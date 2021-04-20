"""
Entradas
puntoUno(x1,y1)--->str--->p1
puntodos(x2,y2)--->str-->p2
Salidas
distancia--float-->d
"""
p1=input()#str
(x1,y1)=p1.split(" ")
x1=float(x1)
y1=float(y1)
p2=input()#str
(x2,y2)=p2.split(" ")
x2=float(x2)
y2=float(y2)
d=((x2-x1)**2+(y2-y1)**2)**0.5
print("{:.4f}".format(d))
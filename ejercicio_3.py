"""
Entrandas
venta1-->float-->v1
Venta2-->float-->v2
venta3--->float-->v3
sueldobase-->float-->sb
Salidas
comision-->float-->co
tota-->float-->total
"""
#entradas
v1=float(input("Digite la venta1: "))
v2=float(input("Digite la venta2: "))
v3=float(input("Digite la venta3: "))
sb=float(input("Digite Suedo base: "))
#caja negra
co=((v1+v2+v3)/3)*0.10
total=sb+co
#salidas
print("la comision es: "+str(co)," sueldo total: "+str(total))
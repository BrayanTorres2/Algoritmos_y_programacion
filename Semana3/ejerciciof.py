"""
Escriba un algoritmo, que dado como dato el sueldo de un trabajador, le aplique un aumento del 15% si su salario bruto es inferior a $900.000 COP y 12% en caso contrario. Imprima el nuevo sueldo del trabajador.
Entradas
salariobruto-->float--sb
Salidas
Salarioneto-->float--sn
"""

sb=float(input("Digite salario bruto: "))
if(sb<900000):
  cn=sb+(sb*0.15)
  print("Salario neto es igual: "+str(cn))
else:
  cn=sb+(sb*0.12)
  print("Salario neto es igual: "+str(cn))  

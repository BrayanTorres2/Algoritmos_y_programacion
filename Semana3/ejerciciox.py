"""
Entradas
temperatura---float--t
Salida
tipo_de_natacion-->str--tipo
"""
t=float(input("Digite temperatura: "))
if(t>85):
  print("natación")
elif(t>71 and t<=85):
  print("tenis")
elif(t>33 and t<=70):
  print("Golf")
elif(t>11 and t<=32):
  print("Esquí")
elif(t<=10):
  print("Marcha")
else:
  print("No se identifico deporte")      

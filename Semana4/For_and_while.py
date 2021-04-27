#imprimir los multiplos de 3 hasta 100
#Determinado
contador=0
while(contador<=100):
  if(contador%3==0):
    print(contador)
  contador=contador+1  
#For determinado
for juancho in range(0,101):
  if(juancho%3==0 or juancho%5==0):
    print(juancho) 
#indeterminado
edad=int(input("Ingrese Edad: "))
while edad<0:
  print("Por favor ingrese una edad positiva")
  edad=int(input("Ingrese Edad"))
print("muchas sentencias")
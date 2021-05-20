import random
#fila=[0,0,0,0,0,0,0,0,0,0]

busca_minas=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]#10x7
for i in range(0,10):
  fila_random=random.randint(0, 9)
  columna_random=random.randint(0,6)
  busca_minas[columna_random][fila_random]=4
c=0
g=0
print(busca_minas)
while True: 
  c=c+1  
  fila=int(input("digite Fila: "))
  columna=int(input("digite columna: ")) 
  if(g==5):
    print("¡¡¡Ganaste!!!")  
    break
  if(c==6):
    print("Demaciados intentos :(")
    break 
  if(busca_minas[fila][columna]==4):
    print("Perdiste :v ")
    break
  else:
    print("Uffff la mina está muy cerca")
    g+=1    
    

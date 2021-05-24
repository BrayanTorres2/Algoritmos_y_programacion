banco=[[1,50_000],[2,10_000],[3,80_000],[4,50_00],[7,10_000]]
cuenta_mayor=banco[0][1]
for fila in range(0,4):
    if(banco[fila][1]>cuenta_mayor):
      cuenta_mayor=banco[fila][1]
print(cuenta_mayor)

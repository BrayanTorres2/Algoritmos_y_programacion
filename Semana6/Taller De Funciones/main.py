frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
elemento->str-->elemento
Salidas
lista-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
 

#Realizar una funcion que retorne la copia de una lista que pasa por parametro 
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""
def copia_lista(lista):
  return lista.copy() 
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""  
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux    
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""  
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista


#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
Salidas
"""  
def letra():
  pass  
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamano
"""   
def tamano_lista(lis):
  pass

#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Salidas
"""  
def informacion_lista():
  pass
#Retornar una lista con los numero negativos  
"""
Entradas:
Salidas
"""  
def numeros_negativos(lista):
  pass
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
def posicion_elemento(elemento):
  pass
#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(elemento):
  pass
#Realizar una funcion que cuente el numero de veces que se repite un elemento  
def repetir(elemento):
  pass
  
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  nueva_dos=numeros_pares(nueva)
  print(elimina_elemento_lista(nueva_dos,"10"))

frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
Salidas
"""
def eliminar_un_caracter_de_toda_la_lista(lista):
 pass
#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
Salidas
"""
def copia_lista(lista):
  return lista.copy() 
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
Salidas
"""  
def numeros_pares():
  pass#RetornaUnaLista
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
Salidas
"""  
def elimina_elemento_lista():
  pass#RetornaUnaLista 

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
Salidas
"""   
def tamano_lista():
  pass #RetornaUnEntero
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
  lista=[1,2,3,4,4]
  copy=copia_lista(lista)
  print(copy)
from colorama import init, Fore, Back, Style
#-----------------------------------------------------------------------------
#Validaciones
def validar_letras(p):#Solo Letras
  while(p.isalpha()==False):
    p=input("DIGITE SOLO LETRAS🅰:   ")
    if(p.isalpha()==True):
      break
  return p  
  #Solo Numeros Positivos
#---------------------------------------------------------------------  
def validar_numeros(N):
 while True:
  try:
    while(N<0):
      N=int(input("digite un numero Positivo ➕"))
    break
  except:
    print("valor no valido digite un numero🤦")
 return N 
#------------------------------------------------------------------------  
def error(d):
  print((Fore.RED+Style.BRIGHT+d))
  return d, print(Style.RESET_ALL + "")
def error_1(E):
  print((Fore.BLUE+Style.BRIGHT+E))
  return E, print(Style.RESET_ALL + "")
def verde(m):
  print((Fore.GREEN+Style.BRIGHT+m))
  return m, print(Style.RESET_ALL + "")
def hora(k):
  print((Fore.CYAN+Style.BRIGHT+k))
  return k, print(Style.RESET_ALL + "")
#-------------------------------------------------------------------------------
      

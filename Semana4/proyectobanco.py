import random
import string
from tkinter import *
from colorama import init, Fore, Back, Style
from file1 import validar_letras,validar_numeros,error,error_1,verde,hora
import time
from datetime import datetime
import os
#-----------------------------------------------------------------------------------------------------
finish=0
n_1=0
cuenta_debito_usuario=[]
banco=[]
para_usu=0
para_contra=0
usuario=[]
MU=[]
contraseña=[]
MC=[]
capital=[]
MA=[]
contraseña1=[]
while finish==0:
#----------------------------------------------------------------------------------------------------------
  r="Bienvenido a Tu Banco💰"
  error_1(r)
  while True:
      try: 
        print(time.strftime("%x"))
        g=int(input("1.Iniciar Sesión 2.Registrar Cuenta 3.Olvidaste Tu Contraseña o Usuario 4.Si quieres cancelar "))
        break
      except:
        a="Error Lo Que Digito No Es Un Numero🤦"
        error(a)
  while(g>4 or g<1):
    a="Numero Digitado No Es Valido Intente Nuevamente 🤦"
    error(a)
    while True:
      try: 
          g=int(input("1.Iniciar Sesión 2.Registrar Cuenta 3.Olvidaste Tu Contraseña o Usuario 4.Si quieres cancelar "))  
          break
      except:
        a="Error Lo Que Digito No Es Un Numero🤦"
        error(a)
  (validar_numeros(g))
#---------------------------------------------------------------------------------------------------------------
  while (g==2):
    nombre_usuario=input("Digite su nombre de usuario🙍")
    f1=usuario.count(nombre_usuario)
    if(f1==0):
        usuario.append(validar_letras(nombre_usuario))
        MU.append(validar_letras(nombre_usuario))
        for x in range(4):#contraseña
            a=(random.choice(string.digits))
            contraseña.append(a)
            lcontraseña=''.join(contraseña)
        contraseña1.append(lcontraseña)
        MC.append(lcontraseña)
        contraseña=[]
        #cuenta
        while True:
          try: 
            capital_usuario=int(input("Digite El dinero Que Depositara En La Cuenta De Ahorros💰:  "))
            break
          except:
            a="Error Lo Que Digito No Es Un Numero🤦"
            error(a)
        while(capital_usuario<100000):
            a="La Cuenta Se Abre Con Un Monto Minimo De 100.000  🤦"
            error(a)
            while True:
              try: 
                capital_usuario=int(input("Digite El dinero Que Depositara En La Cuenta De Ahorros💰:  ")) 
                break
              except:
                  a="Error Lo Que Digito No Es Un Numero🤦"
                  error(a)
        capital.append(validar_numeros(capital_usuario))
        MA.append(validar_numeros(capital_usuario))  
           #Generar cuenta
        lusuario=''.join(usuario)
        print("tu usuario es👤: ",MU)
        print("tu contraseña es🔑:  ",MC)
        print("Dinero Depositado En La Cuenta Es Igual💶:   ",MA,"$")
        a="Inicia Sesion para teminar el proceso"
        verde(a)
        n=0
        n=n+1
        MC=[]
        MU=[]
        MA=[]
        break
    if(f1==1):
      a="Ya Existe Esta Cuenta"
      error(a)
      break
#-------------------------------------------------------------------------------------------
  while (g==3):
    while True:
      try: 
         n3=int(input("Si Olvidaste Tu Usuario Digita 1, Si Olvidaste Tu Contraseña Digita 2:   "))
         break
      except:
        a="Error Lo Que Digito No Es Un Numero🤦"
        error(a)
    while(n3>2 or n3<1):
      a="Numero Digitado No Es Valido Intente Nuevamente 🤦"
      error(a)
      while True:
        try: 
          n3=int(input("Si Olvidaste Tu Usuario Digita 1, Si Olvidaste Tu Contraseña Digita 2:   ")) 
          break
        except:
         a="Error Lo Que Digito No Es Un Numero🤦"
         error(a)
    (validar_numeros(n3))
    if(n3==1):
      C=input("Digite Su Contraseña🔑:  ")
      f=contraseña1.count(C)
      if(f==1):
        while True:
          try: 
            c1=int(input("Digite Dinero Actual Que Tiene La Cuenta💰:  "))
            break
          except:
            a="Error Lo Que Digito No Es Un Numero🤦"
            error(a)
        validar_numeros(c1)
        e=capital.count(c1)
        if(e==1):
          h=capital.index(c1)
          a="Ten presente Desde ahora Recordar Tu Cuenta: "
          hora(a)
          print("Tu Usuario Es-",usuario[h],"-")
          break
        if(e==0):
          a="No Encontrado"
          error(a)
          break
      if(f==0):
        a="No Encontrado"
        error(a)
        break
    if(n3==2):
      u=input("Digite Su Usuario🙍:  ")
      f1=usuario.count(u)
      if(f1==1):
        while True:
          try: 
            c1=int(input("Digite Dinero Actual Que Tiene La Cuenta💰:   "))
            break
          except:
            a="Error Lo Que Digito No Es Un Numero🤦"
            error(a)
        validar_numeros(c1)    
        e=capital.count(c1)
        if(e==1):
          h=capital.index(c1)
          a="Ten presente Desde ahora Recordar Tu Cuenta: "
          hora(a)
          print("Tu Contraseña es-",contraseña1[h],"-")
          break
        if(e==0):
          a="No Encontrado"
          error(a)
          break
      if(f1==0):
        a="No Encontrado"
        error(a)
        break
#----------------------------------------------------------------------------------
  while(g==4):
    #clearScreen(g)
    while True:
      try: 
        g=int(input("1.Iniciar Sesión 2.Registrar Cuenta 3.Olvidaste Tu Contraseña o Usuario 4.Si quieres cancelar"))
        break
      except:
        a="Error Lo Que Digito No Es Un Numero🤦"
        error(a)
  while(g>4 or g<1):
    a="Numero Digitado No Es Valido Intente Nuevamente 🤦"
    error(a)
    while True:
      try: 
          g=int(input("1.Iniciar Sesión 2.Registrar Cuenta 3.Olvidaste Tu Contraseña o Usuario 4.Si quieres cancelar "))  
          break
      except:
        a="Error Lo Que Digito No Es Un Numero🤦"
        error(a)
  (validar_numeros(g))
#---------------------------------------------------------------------------------------------------------------
  while g==1:
    u=input("digite Usuario🙍:  ")
    (validar_letras(u))
    c=input("digite contraseña🔑:  ")
    m=usuario.count(u)
    f=contraseña1.count(c)
    if(m==1 and f==0):
      print("Contraseña incorrecta🤦")
      para_contra=para_contra+1
    elif(m==0 and f==1 ):
      print("usuario incorrecto🤦")
      para_usu=para_usu+1
    elif(m==0 and f==0):
        print("Usuario y Contraseña Incorrectas🤦")
        n_1=n_1+1
    if(n_1>4):
      print("Mas De 5 Intentos")
      i="Lo Sentimos el Sistema no funcionará por 2 horas Intentos Excesivos🤷"
      error(i)
      d="Llamado a La Policia🚔..."
      verde(d)
      time.sleep(60)#7200s==2h
      n_1=0
      break
    if(para_usu>2):
      print("Mas De 3 Intentos")
      i="Lo Sentimos el sistema se bloqueara por 5 minutos🤷"
      error(i)
      time.sleep(5)
      para_usus=0
      break
    if(para_contra>3):
      print("Mas De 3 Intentos")
      i="Lo Sentimos el sistema se bloqueara por 5 minutos🤷"
      error(i)
      time.sleep(5)  
      para_contra=0
      break
    if(m==1 and f==1):
      a=usuario.index(u)
      b=contraseña1.index(c)
      if(a==b):
        a="Bienvenido"
        verde(a)
        while True:
          try: 
            print("Digita Para: 1.Consulta de saldo 2.Transacciones 3.Eliminar cuenta 4.Retirar Dinero 5.Cambiar Contraseña 6.Agregar Dinero a la Cuenta 7.Cerrar Sesion")
            b=int(input(" "))#validarlo
            break
          except:
             a="Error Lo Que Digito No Es Un Numero🤦"
             error(a)
        while (b>7 or b<1):
            a="Numero Digitado No Es Valido Intente Nuevamente 🤦"
            error(a)
            print("Digita Para: 1.Consulta de saldo 2.Transacciones 3.Eliminar cuenta 4.Retirar Dinero 5.Cambiar Contraseña 6.Agregar Dinero a la Cuenta 7.Cerrar Sesion")
            b=int(input("  ")) 
        validar_numeros(b)
        while(b==1):
          a=usuario.index(u)
          print(capital[a])
          break
        while(b==2):
            s1=input("Digite usuario de transaccion ")
            validar_letras(s1)
            t=usuario.count(s1)
            if(t==0):
              ñ="Usuario de transaccion inexistente"
              error(ñ)
              break
            if(t==1):
                s=usuario.index(s1)
                while True:
                  try: 
                     t1=int(input("Digite valor de transaccion"))
                     break
                  except:
                     a="Error Lo Que Digito No Es Un Numero🤦"
                     error(a)
                while(t1<0):
                   a="La transaccion No puede ser negativa"
                   error(a)
                   while True:
                      try: 
                         t1=int(input("Digite valor de transaccion"))
                         break
                      except:
                       a="Error Lo Que Digito No Es Un Numero🤦"
                       error(a)
                validar_numeros(t1)
                a=usuario.index(u) 
                if capital[a]<t1:
                  f="Fondos insuficientes💸"
                  error(f)
                  break
                else:
                  capital[s]=capital[s]+t1
                  print("La cuenta",usuario[s],"ha recibido un total de",t1)
                  print('El saldo de ',usuario[s],'es de',capital[s])
                  capital[a]=capital[a]-t1
                  print("La cuenta",usuario[a],"ha transferido un total de",t1)
                  print('El saldo de ',usuario[a],'es de',capital[a])
            break  
        while(b==3):
          while True:
              try: 
                  e=int(input("Digite 1 para confirmar ✅ ,Digite 2 para Cancelar  🚫"))
                  break
              except:
                  a="Error Lo Que Digito No Es Un Numero🤦"
                  error(a)
          while(e>2 or e<1):
            a="Fuera del rango Digita Uno o Dos"
            error(a)
            while True:
              try: 
                e=int(input("Digite 1 para confirmar ✅ ,Digite 2 para Cancelar  🚫"))
                break
              except:
               a="Error Lo Que Digito No Es Un Numero🤦"
               error(a)
          validar_numeros(e)
          if(e==1):
              a=usuario.index(u)
              usuario.remove(usuario[a])
              contraseña1.remove(contraseña1[a])
              capital.remove(capital[a])
              a="Se ha eliminado tu cuenta👌🏻"
              verde(a)
              break
              #capital.remove() falta capital el cual tengo que pensar
          if(e==2):
              break
        while(b==4):
          a=usuario.index(u)
          while True:
            try: 
              jk=int(input("Ingrese la cantidad a retirar"))
              break
            except:
              a="Error Lo Que Digito No Es Un Numero🤦"
              error(a)
          while(jk<0):
            a="La Cantidad No puede ser negativa"
            error(a)
            while True:
              try: 
                jk=int(input("Ingrese la cantidad a retirar"))
                break
              except:
               a="Error Lo Que Digito No Es Un Numero🤦"
               error(a)
          validar_numeros(jk)
          if capital[a]<jk:
            print("No se puede retirar esa cantidad")
            print("Por favor consultar el saldo y volver a intentar")
            break
          else:
            capital[a]=capital[a]-jk
            print("Se han retirado",jk,"su cuenta tiene un saldo de",capital[a])
            break
        while(b==5):
          while True:
            try:
              c3=int(input("digite su nueva contraseña🔑:  "))
              if c3>=1000 and c3<=9999:
                c3=str(c3)
                lk=contraseña1.index(c)
                contraseña1.remove(c)
                contraseña1.insert(lk,c3)
                a="Se a Cambiado Tu Contraseña Exitosamente "
                verde(a)
                break
              else:
                print("La contraseña debe ser de 4 digitos")
                break
              break
            except:
              print("Ingresar solo numeros")
          break 
        while(b==6):
          try:
            a=usuario.index(u)
            while True:
              try: 
                cantidad=int(input("Digita Cantidad Que Quieres Agregar A La Cuenta💸:  "))
                break
              except:
                a="Error Lo Que Digito No Es Un Numero🤦"
                error(a)
            while(cantidad<0):
              a="La Cantidad No puede ser negativa"
              error(a)
              while True:
                try: 
                 cantidad=int(input("Digita Cantidad Que Quieres Agregar A La Cuenta💸:  "))
                 break
                except:
                 a="Error Lo Que Digito No Es Un Numero🤦"
                 error(a)
            validar_numeros(cantidad)
            capital[a]=capital[a]+cantidad
            print("Valor Total De La Cuenta💸:  ",capital[a])
            break
          except:
            print("Ingrese solo numeros")
        while(b==7):
            a="Gracias Por Utilizar Nuestros Servicios 😊"
            verde(a)
            break
        break
      else:
        break
#----------------------------------------------------------------------------
    

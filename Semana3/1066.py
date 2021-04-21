a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
e=int(input(""))
par=0
impar=0
positivo=0
negativo=0
#-----------Par e impar---------------------------------
#nuemro1
if(a%2==0):
  par=par+1
else:
  impar=impar+1  
#numero2  
if(b%2==0):
  par=par+1
else:
  impar=impar+1   
#numero3     
if(c%2==0):
  par=par+1
else:
  impar=impar+1  
#numero4    
if(d%2==0):
   par=par+1
else:
  impar=impar+1  
#numero5        
if(e%2==0):
  par=par+1
else:
  impar=impar+1  
#------------------------------negativos y positivo
#nuemro1
if(a<=-1):
  negativo+=1
if(a>=1):
  positivo+=1 
#numero2  
if(b<=-1):
   negativo+=1
if(b>=1):
  positivo+=1   
#numero3     
if(c<=-1):
  negativo+=1
if(c>=1):
  positivo+=1   
#numero4    
if(d<=-1):
  negativo+=1
if(d>=1):
  positivo+=1
#numero5        
if(e<=-1):
  negativo+=1
if(e>=1):
  positivo+=1
print(str(par)+" valor(es) par(es)")
print(str(impar)+" valor(es) impar(es)")
print(str(positivo)+" valor(es) positivo(s)")
print(str(negativo)+" valor(es) negativo(s)")

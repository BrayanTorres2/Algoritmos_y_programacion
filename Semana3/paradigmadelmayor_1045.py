t=input("")
(a,b,c)=t.split(" ")
a=float(a)
b=float(b)
c=float(c)
if(a==b==c):
  A=a
  B=b
  C=c
elif(a>=b and a>=c and b>=c):
   A=a
   B=b
   C=c
elif(a>=b and a>=c and c>=b):
   A=a
   B=c
   C=b  
elif(b>=c and b>=a and a>=c):
  A=b
  B=a
  C=c
elif(b>=c and b>=a and c>=a):
  A=b
  B=c
  C=a  
elif(c>=b and c>=a and b>=a):
  A=c
  B=b
  C=a  
elif(c>=b and c>=a and a>=b):
  A=c
  B=a
  C=b
print(A,B,C)       
if(A>=B+C):
  print("NAO FORMA TRIANGULO")
else:  
  if(A**2==B**2+C**2):
    print("TRIANGULO RETANGULO")  
  if((A**2)>(B**2+C**2)):
    print("TRIANGULO OBTUSANGULO")
  if(A**2<B**2+C**2):
    print("TRIANGULO ACUTANGULO")
  if(A==B==C):
    print("TRIANGULO EQUILATERO")   
  if(A==B and A!=C or B==C and B!=A or C==A and C!=B):
    print("TRIANGULO ISOSCELES")

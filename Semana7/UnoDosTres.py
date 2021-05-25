n=int(input(""))
c=0
while True:
  if(c==n):
    break
  c=c+1
  letra=input()
  s=len(letra)#tamaño
  if(s==5):
    print("3")
  elif(letra[0]=="t" and letra[1]=="w" or letra[0]=="t" and letra[2]=="o" or letra[1]=="w" and letra[2]=="o"):
    print("2")
  else:
    print(1)  

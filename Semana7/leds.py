n=int(input(""))
c=0
suma=0
while True:
  if(c==n):
    break
  c=c+1
  led=input("")
  for i in led:
    if(i=="1"):
      suma=suma+2
    elif(i=="2"):
      suma+=5
    elif(i=="3"):
      suma+=5
    elif(i=="4"):
      suma+=4
    elif(i=="5"):
      suma+=5
    elif(i=="6"):
      suma+=6 
    elif(i=="7"):
      suma+=3
    elif(i=="8"):
      suma+=7
    elif(i=="9"):
      suma+=6 
    elif(i=="0"):
      suma+=6
  print(str(suma)+" leds")
  suma=0 

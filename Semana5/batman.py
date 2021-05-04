c=0
a=int(input(""))
while True:
    if(c==a):
        break
    c=c+1
    n=input("")
    s=len(n)
    if(s>=0 and s<=25):
        print("Y",end="\n")
    else:
        print("N",end="\n")  

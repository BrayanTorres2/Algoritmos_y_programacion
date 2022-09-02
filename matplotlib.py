import matplotlib.pyplot as plt
#pip install matplotlib
def histograma_edad(lista_edad):
    fig, ax=plt.subplots()
    div=[10,20,30,40,50,60,70,80,90]
    plt.hist(lista_edad,div)
    plt.show()
#histograma_edad(edad)    

def bar_edad(lista_edad):
    fig, ax=plt.subplots()
    x=["10-19","20-29","30-39","40-49","50-59","60-69","70-79","80-90"]
    e1=0
    e2=0
    e3=0
    e4=0
    e5=0
    e6=0
    e7=0
    e8=0
    for i in lista_edad:
        if(i in range(10,20)):
            e1=e1+1
        elif(i in range(20,30)): 
            e2=e2+1
        elif(i in range(30,40)):
            e3=e3+1
        elif(i in range(40,50)):
            e4=e4+1
        elif(i in range(50,60)):
            e5=e5+1
        elif(i in range(60,70)):
            e6=e6+1
        elif(i in range(70,80)):
            e7=e7+1
        elif(i in range(80,91)):
            e8=e8+1                           
    y=[e1,e2,e3,e4,e5,e6,e7,e8]
    edad=ax.bar(x,y,color="green")
    ax.set_title("Barra de edad")
    ax.set_xlabel("Edad")
    ax.set_ylabel("Frecuencia")
    ax.grid()
    plt.show()        
bar_edad(edad)    

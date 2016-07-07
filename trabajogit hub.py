import time
import os
def divicion ():
    a=float(input("ingrese numero: "))
    b=float(input("ingrese numero: "))
    c=a/b
    os.system("cls")
    time.sleep(1)
    print("el resultado es: ",c)
def raiz():
    e=float(input("ingrese numero: "))
    d=e**2
    os.system("cls")
    print("resultado es: ",d)
        
divicion()

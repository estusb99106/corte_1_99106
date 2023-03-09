from digitos import dig as d
from primos import prim as p
print("1. programa digitos ")
print("2. programa primos ")
opc=int(input("ingrese una opcion: "))
if opc==1:
    num=int(input("ingrese un numero"))
    result=d
elif opc==2:
    num=int(input("ingrese un numero"))
    result=p
else:
    print("esa no es una opcion")
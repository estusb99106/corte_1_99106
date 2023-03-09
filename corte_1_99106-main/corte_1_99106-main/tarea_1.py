# tarea 1
#Realice un programa donde se soliciten dos números al usuario, después se de como resultado el residuo y el cociente de la división entre n1 y n2.
n1=int(input("de el primer numero "))
n2=int(input("de el segundo numero "))
residuo=n1//n2
cosiente=n1/n2
print(residuo, cosiente)
#Realice un programa que calcule el índice de masa corporal de una persona, donde le solicite al usuario la estatura en cm y el peso en Kg. Después imprima como resultado el índice de masa corporal mediante un mensaje que diga “Su IMC es valor” redondeado con dos decimales.
peso=int(input("de su peso en kilogramo "))
altura=int(input("de su altura en centimetros "))
valor=peso/(altura)**2
print("su IMC es ",valor)
#Realice un programa donde se solicite al usuario escribir el precio final de un artículo o producto, con el que después calculará e imprimirá en pantalla el valor del IVA y el valor bruto (precio antes de IVA) del artículo o producto.
articulo:int(input("ingrese la compra total del producto "))
aumento=int(input("ingrese el iva del producto "))
iva=aumento/100
Vbruto=articulo-iva
print("el iva de su producto es ", iva, "el producto sin iva es ", Vbruto )
#Realice un programa que permita calcular el costo anual del consumo de combustible de un vehículo, si el usuario ingresa la distancia recorrida (Km) anual, el consumo de combustible (L / 100Km) anual y el costo promedio anual del combustible por litros recorridos ( $/L)Ejm:Distanciarecorridaanual:12000KmConsumoanual:5L/100KmCostopromedioanual:0.72  / L Costo anual del consumo de combustible: $432
recorrido=float(input("ingrese el recorrido anual del vehiculo en kilometros "))
consumo=float(input("ingrese el consumo anual del vehiculo en litros "))
costo=float(input("ingrese el costo anual del combustible por litro "))
con=consumo/100
gastoT=recorrido*con*costo
print(gastoT)
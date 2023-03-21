print("1 realize un programa donde pida al usuario un numero entero positivo y despues imprima todos los numeros impares desde el uno hasta dicho numer separado por comas")
print("2 realize un programa que calcule el numero factorial de un numero seleccionado por el usuario")
print("3 realize un progrma que solicite un numero al usuario despues indique si es primo o no; ademas imprima los numeros primos primos hasta este numero")
opc=int(input("elige una opcion "))
if opc == 1:
    comprobar=True
    while comprobar:
        num=int(input("ingrese un numero positivo"))
    if num > 0:
      comprobar=False
      for i in range (1,num+1):
          if i % 2==0:
            print(i ,"es par,")
          else:
            print(i, "es impar,")
    else:
      print("el numero tine que ser positivo")
elif opc == 2:
   def factorial(num): 
    if num < 0: 
        print("Factorial de negativo no existe ")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 
    num=int(input("ingrese un numero ")); 
    print("Factorial de",num,"es", factorial(num))
elif opc == 3:
   comprobar=True
   while comprobar:

    num=int(input("ingrese un numero "))
    if num > 0:
      comprobar=False
      for i in range (2,num+1):
        cresiente=2
        esPrimo=True
        while esPrimo and cresiente < i :
          if i % cresiente==0:
            esPrimo=False
          else:
            cresiente+=1
        if esPrimo:
          print(i ,"es primo")
    else:
      print("el numero tine que ser positivo")
else :
    print("esa opcion no esta disponible ")
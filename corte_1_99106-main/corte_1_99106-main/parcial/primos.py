def prim():
    comprobar=True
    while comprobar:
        num=int(input("ingrese un numero "))
        if num > 0:
            comprobar=False
            for i in range (1,num+1):
                cresiente=2
                esPrimo=True
                while esPrimo and cresiente < i :
                    if i % cresiente==0:
                        esPrimo=False
                    else:
                        cresiente+=1
                if esPrimo:
                    print(i)
        else:
            print("el numero tine que ser positivo")
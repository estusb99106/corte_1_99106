def dig():
    num=int(input("ingrese un numero "))
    while num>0:
        A=num//10
        B=A*10
        C=num-B
        print(C)
import math

a= float(input("Informe o valor de a:"))
b= float(input("Informe o valor de b:"))
c= float(input("Informe o valor de c:"))
delta= b**2-4*a*c
X= (-b+math.sqrt(delta))/ (2*a)
Y= (-b-math.sqrt(delta))/ (2*a)

if delta == 0:
    X= (-b+math.sqrt(delta))/ (2*a)
    print("a raiz desta equação é", X)
else:
    if delta<0:
        print("esta equação não possui raízes reais.")
    else:
        X= (-b+math.sqrt(delta))/ (2*a)
        Y= (-b-math.sqrt(delta))/ (2*a)
        if X<Y:
            print("as raízes da equação são", X,"e", Y)
        else:
            print("a
            s raízes da equação são", Y,"e", X)
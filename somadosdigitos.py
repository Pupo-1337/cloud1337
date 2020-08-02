n1=(input('Digite um número: '))
for i in range(len(n1)):
    n1= int(n1)%10
    n2= int(n1)//10
    n3= int(n1+n2)
    print(n2)
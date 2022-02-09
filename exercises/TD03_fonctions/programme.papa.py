def Binaire(nombre):
    L1=[]
    quotient=1
    reste=1
    while quotient!=0:
        quotient=nombre//2
        reste=nombre%2
        nombre=quotient
        L1.append(reste)
Binaire(52)

programme qui affiche




#Initiatisation des listes
Set1=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,23, 25, 27, 29, 31]
Set2=[2,3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
Set3=[4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
Set4=[8 ,9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
Set5=[16, 17,18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
for i in range (5):
    bool=int(input("Est que le nombre est dans la liste")
    if True in Set1:
        a=Set1[0]
    else: 
        a=0
    if nombre in Set2:
        b=Set2[0]
    else:
    b=0
    if nombre in Set3 :
        c=Set3[0]
    else:
        c=0
    if nombre in Set4:
        d=Set4[0]
    else:
        d=0
    if nombre in Set5 :
        e=Set5[0]
    else:
        e=0
jour= a+b+c+d+e
print(jour)
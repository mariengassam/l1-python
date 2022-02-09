""""fonction qui divise les éléments de 2 listes et renvoie une 3eme liste avec la réponse 
Comme elle traite d'une opération par chaque indice, elle fat un range de la longueur de la liste, elle crée ensuite une variable v 
dans laquelle elle stock le résultat qu'elle ajoute grâce à un append dans une 3eme liste L3 initialisée en dehors de la fonction
""""
def Division(L1,L2):
    L3=[]
    for k in range(len(L1)):
        v=L1[k]//L2[k]
        L3.append(v)
    return L3
Division([3,4,5],[1,2,1])


"""Fonction qui compare chaque élément d'une liste à un élément v qui et qui donne le nombre de fois où l'élément est supérieur à v
Crée un compteur de boucle

Il fait ainsi un range de la longeur de la liste 
Puis une condition de comparaison
et il crée la variable n qui est le compteur""""
#On utilise une boucle ou on peut utiliser la fonction count
def Fonction(L1, Val):
    n=0 
    for k in range(len(L1)):
        if L1[k]>Val:
            n=n+1
    return n
Fonction([3,4,5],2)

"""Fonction qui demande à l'utilisateur de rentrer 10 entiers et qui les renvoie dans une liste
 les stocks dans la variable entier qu'il ajoutera à la liste L2 au préalable
Initialisée à l'exterieur de la fonction""""
def Fonction():
    L2=[]
    for i in range (0,11):
        entier=int(input("Donner un élément"))
        L2.append(entier)
    return L2
Fonction()


#quand une fonction dot renvoyer une liste on utilise append 
"""" Fonction qui retourne l'élement maximum d'une liste
Il faut initialiser le max comme le 1er élément de la liste car c'est lui qu'on va comparer 
on utilise le for k in liste car on compare des eléments d'une liste""""

#For k in liste traite des éléments k d'une liste
#For k in range (len(Liste)) Traite des indice ou liste[k] est un elément
def Maximum (Liste):
    max=Liste[0]
    for k in (Liste):
        if k>max:
            max= k 
    return max
Maximum([3,4,2,1,12])


#Fonction qui renvoie le maximum  d'une liste et son indice
def Maximum (Liste):
    max=Liste[0]
    indmax=0
    for k in range (len(Liste)):
        if Liste[k]>max:
            max= Liste[k]
            indmax= k
    return indmax,max
Maximum([3,4,2,1])


#Fonction qui inverse deux eléments
def reverse (a,b):
   # c=a
   # a=b
   # b=c
    a,b=b,a
    return a,b
reverse(2,5)

#fonction qui renvoie le nombre de fois qu'un élément apparaît dans une liste grâce à count(k)

def Compteur (Liste,k):
    b=Liste.count(k)
    return b
Compteur ([3,2,5,2,452,5,2], 2)

#Liste qui renvoie le nombre de dois ou c revient dans une liste sans la fonction count
def Compteur (Liste,c):
    for k in Liste:
        if c in Liste:
            k=k+1
    return k
Compteur ([3,2,5,2,452,5,2], 2)

"""Ecrire une fonction qui prend en parametre une liste dont des entiers
 et retourne la même liste dans lequel ont été supprimmé le plsu petit élémet et le plus grand élément 
"""
#Encore une fois on utilise le for k in liste parce qu'on compare des éléments 
def Remove1 (Liste):
    max=Liste[0]
    min=Liste[1]
    for k in Liste:
        if k>max:
            max=k
    for k in Liste:
        if k<min:
            min=k
    Liste.remove(min)
    Liste.remove(max)
    return Liste
Remove1([18,2,4,16,0,15])


#fonction qui renvoie une liste de la somme des puissance 2 jusqu'a un arguent n passé en paramêtre 
def puissance2(n):
    L3=[]
    Somme=0
    for k in range(n):
        Somme=Somme+2**k
        L3.append(Somme)
    return L3
puissance2(4)
#Sujet 21
#afficher une grille de morpion
#Pour sauter des lignes(end=""),tel que Tablejeux[i][j], end=""]
"""On voit qu'on à fait un for dans un for pour faire une liste imbrique+ le range est le nombre de colonne et de ligne et Tablejeux[i][j] correspond à la grille""""
def afficheJeu(TableJeux):
    for i in range (3):
        for j in range (3):
            print(TableJeux[i][j], end="")
        print("")
TableJeux=[[0,0,0],[0,0,0,],[0,0,0]]
afficheJeu(TableJeux)


#Fonction qui renvoie une liste de liste en ayant demandé à l'utilisateur le contenu d'une ligne il existe une seule boucle du coup
"""On traite de la liste par ligne pour cela on à donc besoin d'un seul  for """"
def Mat():
    Matrice=[]
    Ligne[]
    #Pour demander la taille de la matrice:
    n=input("rentrer le nombre de lignes")
    #Pour demander les valeurs de la matrice 
    for i in range (n):
        Ligne=input(f"Entrer la {i}eme ligne")
        Matrice.append(Ligne)
    #Renvoyer le contenu de Matrice
    return print(Matrice[], end="")


#Fonction qui calcule le temps d'execution d'une autre fonction

import time
def time_func(func):
#heure courante
    début= time.time()
    func()
    fin= time.time()
    tempsécoulé=fin-début
    return tempsécoulé


def f(): 
    time.sleep(3)

print(time_func(f))

#fonction qui permettait d'additionner les termes d'une liste si elles ont la même longueure 
def Verif (L1,L2):
    L3=[]
#Verfication de la longueur des deux listes
    if len(L1)==len(L2):
        for i in range(len(L1)):
            Somme=L1[i]+L2[i]
            L3.append(Somme)
    return L3
Verif([1,2,3],[4,2,6])


#Fonction qui utilise le tirage au sort
import random
def plan_jour(touslieux):
    #tirge au sort du nombre de lieux qu'on va visiter entre 0 et 3
    nb_lieux_visite=random.randint(0,3)
    lieux_visite=[]
    #Condion qui dit que une fois choisit, si 0 lieux de visite est choisi la fonction au jour renvoie []
    if nb_lieux_visite==0:
        return[]
    #Condition qui dit que dans la mesure des lieux visité, on fait maintenant un tirage au sort sur tous les lieux (5) et qu'on rentre dans une nouvelle liste lieux_visite
    else:   
        for i in range (nb_lieux_visite):
            choixtouslieux=random.randint(1,touslieux)
            lieux_visite.append(choixtouslieux)
    return lieux_visite
    #pour la semaine dans la mesure de 1 à 7 on crée une nouvelle variable qui se rajoute à chaque pas les éléments de éléments jours
def plan_semaine():
    lieux_visite_semaine=[]
    for i in range (7):
        lieux=plan_jour(5)
        lieux_visite_semaine.append(lieux)
    return lieux_visite_semaine
#plan_jour(5)
plan_semaine()



#from collections import Counter
def compteur(chainedecaractere):
    listedesoccurence=[]
    #for i in range (len(chainedecaractere)):
    for j in (chainedecaractere):
        compte = chainedecaractere.count(j)
        listedesoccurence.append([j,compte])
        if compte>=1:
            chainedecaractere.remove(j)
    return listedesoccurence
chaine= ["m","a","m","a","m","v","a"]
compteur(chaine)
# Programme qui renvoie les chiffres d'un nombre et le nombre de chiffres dans un nombre 
def fonction(n):
    q=n
    i=0
    L3=[]
    while q!=0:
        reste=n%10
        L3.append(reste)
        q=n//10
        n=q
        i=i+1 
    return i, L3
print(fonction(2453))




def Binaire(nombre):
    quotient=1
    reste=0
    puissance=1
    Totalreste=0
    L1=[]
    while quotient!=0:
        quotient=nombre//2
        reste=nombre%2
        nombre=quotient
        Totalreste=Totalreste+puissance*reste
        puissance=puissance*10 #p=10 puis p=100 
        L1.append(reste)
    L1.reverse()
        
    return L1, Totalreste
Binaire(50)





#Programme de loterie

import random
#nombre=random.randint(0,99)
nombre=20
reste=nombre%10
dizaine=nombre//10
reste2=loterie%10
dizaine2=loterie//10
loterie=67

if nombre==loterie:
    print("Récompense 10 000")
    
elif ((reste==reste2 or reste==dizaine2 )and  (dizaine==reste2 or dizaine==dizaine2)):
    print("Récompense de 3000")
elif ((reste==reste2 or reste==dizaine2 ) or  (dizaine==reste2 or dizaine==dizaine2)):

    print("Réponse 1000")
else:
     print("rat")
print(nombre)
print(loterie)
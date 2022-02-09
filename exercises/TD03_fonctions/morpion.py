grille=[[0,0,0],[0,0,0],[0,0,0]]
def verifie_ligne (grille,n):
    if grille[n-2]==[0,0,0] and grille[n-1]==[0,0,0] and grille[n-1]==[0,0,0]:
        x=1
    elif grille[0]==[0,0,0] and grille[1]==[0,0,0] and grille[2]==[0,0,0]:
        x=-1
    return x
verifie_ligne(grille,3)


#if grille[n-3]==[0,0,0] or grille[n-2]==[0,0,0] or grille[n-1]==[0,0,0]:
        #x=1
    #elif grille[n-3]==[1,1,1] or grille[n-2]==[1,1,1] or grille[n-1]==[1,1,1]:
        #x=-1
   # if grille[n-1]==[0,0,0]:
      #  x=1
   # else grille[n-1]==[1,1,1]:
   #     x=-1
  #  else x==9
  #  return x
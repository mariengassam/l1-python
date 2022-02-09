def Division(L1,L2):
    L3=[]
    for k in range(len(L1)):
        v=L1[k]//L2[k]
        L3.append(v)
    return L3
Division([3,4,5],[1,2,1])

print("which file do you want to open")
FF=input()
def reverse(K):
    G=[]
    for i in range(len(K)):
        G.append(K[len(K)-i-1])
while True:
    file=open(FF+".txt","r")

    exec("C="+file.readlines()[0])
    file.close()
    R=[]
    for c in C:
        R.append([0,c[1],c[2],c[0]])
    R.sort()
    for i in range(4):
        Rnext=[]
        while len(R)>1:
            print(R[0][2]+"("+str(R[0][1])+")"+" VS "+R[1][2]+"("+str(R[1][1])+")")
            T=""
            while not T in[R[0][2],R[1][2]]:
                T=input()
            if T==R[0][2]:
                change=8*(10**((R[1][1]-R[0][1])/20))/(10**((R[1][1]-R[0][1])/20)+1)
                R[0][1]+=round(change)
                R[1][1]-=round(change)
                Rnext.append([R[0][0]+1,R[0][1],R[0][2],R[0][3]])
                R.remove(R[0])
                Rnext.append([R[0][0],R[0][1],R[0][2],R[0][3]])
                R.remove(R[0])
            else:
                change=8*(10**((R[0][1]-R[1][1])/20))/(10**((R[0][1]-R[1][1])/20)+1)
                R[0][1]-=round(change)
                R[1][1]+=round(change)
                Rnext.append([R[0][0],R[0][1],R[0][2],R[0][3]])
                R.remove(R[0])
                Rnext.append([R[0][0]+1,R[0][1],R[0][2],R[0][3]])
                R.remove(R[0])
        Rnext.sort()
        R=Rnext
    C=[]
    print("MASTER'S TOURNOMENT")
    for r in R:
        C.append([r[3],r[1],r[2]])
    C.sort()
    WB=[C[-3],C[-10],C[-6],C[-7],C[-4],C[-9],C[-5],C[-8]]
    print(WB)
    LB=[]
    elim=[]
    while len(LB)>1 or len(WB)>0:

        if len(WB)>len(LB):
            WBnext=[]
            LBnext=[]
            while len(WB)>0:
                print(WB[0][2]+"("+str(WB[0][1])+")"+" VS "+WB[1][2]+"("+str(WB[1][1])+")")
                T=""
                while not T in[WB[0][2],WB[1][2]]:
                    T=input()
                if T==WB[0][2]:
                    change=8*(10**((WB[1][1]-WB[0][1])/20))/(10**((WB[1][1]-WB[0][1])/20)+1)
                    WB[0][1]+=round(change)
                    WB[1][1]-=round(change)
                    WBnext.append(WB[0])
                    WB.remove(WB[0])
                    LBnext.append(WB[0])
                    WB.remove(WB[0])
                else:
                    change=8*(10**((WB[0][1]-WB[1][1])/20))/(10**((WB[0][1]-WB[1][1])/20)+1)
                    WB[0][1]-=round(change)
                    WB[1][1]+=round(change)
                    LBnext.append(WB[0])
                    WB.remove(WB[0])
                    WBnext.append(WB[0])
                    WB.remove(WB[0])
        elif len(LB)>len(WB):
            LBnext=[]
            while len(LB)>0:
                print(LB[0][2]+"("+str(LB[0][1])+")"+" VS "+LB[1][2]+"("+str(LB[1][1])+")")
                T=""
                while not T in[LB[0][2],LB[1][2]]:
                    T=input()
                if T==LB[0][2]:
                    change=8*(10**((LB[1][1]-LB[0][1])/20))/(10**((LB[1][1]-LB[0][1])/20)+1)
                    LB[0][1]+=round(change)
                    LB[1][1]-=round(change)
                    LBnext.append(LB[0])
                    LB.remove(LB[0])
                    elim.append(LB[0])
                    LB.remove(LB[0])
                else:
                    change=8*(10**((LB[0][1]-LB[1][1])/20))/(10**((LB[0][1]-LB[1][1])/20)+1)
                    LB[0][1]-=round(change)
                    LB[1][1]+=round(change)
                    elim.append(LB[0])
                    LB.remove(LB[0])
                    LBnext.append(LB[0])
                    LB.remove(LB[0])
        elif len(LB)==1:
            LB.append(WB[0])
            WB.remove(WB[0])
        else:
            WBnext=[]
            LBnext=[]
            while len(WB)>0:
                print(WB[0][2]+"("+str(WB[0][1])+")"+" VS "+WB[1][2]+"("+str(WB[1][1])+")")
                T=""
                while not T in[WB[0][2],WB[1][2]]:
                    T=input()
                if T==WB[0][2]:
                    change=8*(10**((WB[1][1]-WB[0][1])/20))/(10**((WB[1][1]-WB[0][1])/20)+1)
                    WB[0][1]+=round(change)
                    WB[1][1]-=round(change)
                    WBnext.append(WB[0])
                    WB.remove(WB[0])
                    LBnext.append(WB[0])
                    WB.remove(WB[0])
                else:
                    change=8*(10**((WB[0][1]-WB[1][1])/20))/(10**((WB[0][1]-WB[1][1])/20)+1)
                    WB[0][1]-=round(change)
                    WB[1][1]+=round(change)
                    LBnext.append(WB[0])
                    WB.remove(WB[0])
                    WBnext.append(WB[0])
                    WB.remove(WB[0])
                print(LB[0][2]+"("+str(LB[0][1])+")"+" VS "+LB[1][2]+"("+str(LB[1][1])+")")
                T=""
                while not T in[LB[0][2],LB[1][2]]:
                    T=input()
                if T==LB[0][2]:
                    change=8*(10**((LB[1][1]-LB[0][1])/20))/(10**((LB[1][1]-LB[0][1])/20)+1)
                    LB[0][1]+=round(change)
                    LB[1][1]-=round(change)
                    LBnext.append(LB[0])
                    LB.remove(LB[0])
                    elim.append(LB[0])
                    LB.remove(LB[0])
                else:
                    change=8*(10**((LB[0][1]-LB[1][1])/20))/(10**((LB[0][1]-LB[1][1])/20)+1)
                    LB[0][1]-=round(change)
                    LB[1][1]+=round(change)
                    elim.append(LB[0])
                    LB.remove(LB[0])
                    LBnext.append(LB[0])
                    LB.remove(LB[0])
        LB=LBnext
        WB=WBnext
    elim.append(LB[0])
    K=[0,0,0,0,1,1,1,2]
    print("END")
    for j in range(len(elim)):
        elim[j][0]=K[j]
    R=[]
    for c in C:
        R.append([0,c[1],c[2],c[0]])
    R.sort()
    for i in range(4):
        Rnext=[]
        while len(R)>1:
            print(R[0][2]+"("+str(R[0][1])+")"+" VS "+R[1][2]+"("+str(R[1][1])+")")
            T=""
            while not T in[R[0][2],R[1][2]]:
                T=input()
            if T==R[0][2]:
                change=8*(10**((R[1][1]-R[0][1])/20))/(10**((R[1][1]-R[0][1])/20)+1)
                R[0][1]+=round(change)
                R[1][1]-=round(change)
                Rnext.append([R[0][0]+1,R[0][1],R[0][2],R[0][3]])
                R.remove(R[0])
                Rnext.append([R[0][0],R[0][1],R[0][2],R[0][3]])
                R.remove(R[0])
            else:
                change=8*(10**((R[0][1]-R[1][1])/20))/(10**((R[0][1]-R[1][1])/20)+1)
                R[0][1]-=round(change)
                R[1][1]+=round(change)
                Rnext.append([R[0][0],R[0][1],R[0][2],R[0][3]])
                R.remove(R[0])
                Rnext.append([R[0][0]+1,R[0][1],R[0][2],R[0][3]])
                R.remove(R[0])
        Rnext.sort()
        R=Rnext
    C=[]
    print("CHAMPION'S TOURNOMENT")
    for r in R:
        C.append([r[3],r[1],r[2]])
    C.sort()
    WB=[C[-1],C[-4],C[-2],C[-3]]
    print(WB)
    LB=[]
    elim=[]
    while len(LB)>1 or len(WB)>0:

        if len(WB)>len(LB):
            WBnext=[]
            LBnext=[]
            while len(WB)>0:
                print(WB[0][2]+"("+str(WB[0][1])+")"+" VS "+WB[1][2]+"("+str(WB[1][1])+")")
                T=""
                while not T in[WB[0][2],WB[1][2]]:
                    T=input()
                if T==WB[0][2]:
                    change=8*(10**((WB[1][1]-WB[0][1])/20))/(10**((WB[1][1]-WB[0][1])/20)+1)
                    WB[0][1]+=round(change)
                    WB[1][1]-=round(change)
                    WBnext.append(WB[0])
                    WB.remove(WB[0])
                    LBnext.append(WB[0])
                    WB.remove(WB[0])
                else:
                    change=8*(10**((WB[0][1]-WB[1][1])/20))/(10**((WB[0][1]-WB[1][1])/20)+1)
                    WB[0][1]-=round(change)
                    WB[1][1]+=round(change)
                    LBnext.append(WB[0])
                    WB.remove(WB[0])
                    WBnext.append(WB[0])
                    WB.remove(WB[0])
        elif len(LB)>len(WB):
            LBnext=[]
            while len(LB)>0:
                print(LB[0][2]+"("+str(LB[0][1])+")"+" VS "+LB[1][2]+"("+str(LB[1][1])+")")
                T=""
                while not T in[LB[0][2],LB[1][2]]:
                    T=input()
                if T==LB[0][2]:
                    change=8*(10**((LB[1][1]-LB[0][1])/20))/(10**((LB[1][1]-LB[0][1])/20)+1)
                    LB[0][1]+=round(change)
                    LB[1][1]-=round(change)
                    LBnext.append(LB[0])
                    LB.remove(LB[0])
                    elim.append(LB[0])
                    LB.remove(LB[0])
                else:
                    change=8*(10**((LB[0][1]-LB[1][1])/20))/(10**((LB[0][1]-LB[1][1])/20)+1)
                    LB[0][1]-=round(change)
                    LB[1][1]+=round(change)
                    elim.append(LB[0])
                    LB.remove(LB[0])
                    LBnext.append(LB[0])
                    LB.remove(LB[0])
        elif len(LB)==1:
            LB.append(WB[0])
            WB.remove(WB[0])
        else:
            WBnext=[]
            LBnext=[]
            while len(WB)>0:
                print(WB[0][2]+"("+str(WB[0][1])+")"+" VS "+WB[1][2]+"("+str(WB[1][1])+")")
                T=""
                while not T in[WB[0][2],WB[1][2]]:
                    T=input()
                if T==WB[0][2]:
                    change=8*(10**((WB[1][1]-WB[0][1])/20))/(10**((WB[1][1]-WB[0][1])/20)+1)
                    WB[0][1]+=round(change)
                    WB[1][1]-=round(change)
                    WBnext.append(WB[0])
                    WB.remove(WB[0])
                    LBnext.append(WB[0])
                    WB.remove(WB[0])
                else:
                    change=8*(10**((WB[0][1]-WB[1][1])/20))/(10**((WB[0][1]-WB[1][1])/20)+1)
                    WB[0][1]-=round(change)
                    WB[1][1]+=round(change)
                    LBnext.append(WB[0])
                    WB.remove(WB[0])
                    WBnext.append(WB[0])
                    WB.remove(WB[0])
                print(LB[0][2]+"("+str(LB[0][1])+")"+" VS "+LB[1][2]+"("+str(LB[1][1])+")")
                T=""
                while not T in[LB[0][2],LB[1][2]]:
                    T=input()
                if T==LB[0][2]:
                    change=8*(10**((LB[1][1]-LB[0][1])/20))/(10**((LB[1][1]-LB[0][1])/20)+1)
                    LB[0][1]+=round(change)
                    LB[1][1]-=round(change)
                    LBnext.append(LB[0])
                    LB.remove(LB[0])
                    elim.append(LB[0])
                    LB.remove(LB[0])
                else:
                    change=8*(10**((LB[0][1]-LB[1][1])/20))/(10**((LB[0][1]-LB[1][1])/20)+1)
                    LB[0][1]-=round(change)
                    LB[1][1]+=round(change)
                    elim.append(LB[0])
                    LB.remove(LB[0])
                    LBnext.append(LB[0])
                    LB.remove(LB[0])
        LB=LBnext
        WB=WBnext
    elim.append(LB[0])
    K=[1,2,3,4]
    print("END")
    for j in range(len(elim)):
        elim[j][0]=K[j]
    C.sort()
    file=open(FF+".txt","w")
    file.write(str(C))

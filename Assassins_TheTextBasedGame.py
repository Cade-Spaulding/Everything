Characters=[]
Creatures=[]
MAP=[]
P=6
actions=[]
InvNum=0
InvTime=-1
MapChaos=64
ride=[]
peace=5
events=[]
from copy import copy
print("How many players. max 10")
print()
print("this game is REALLY not designed to be single player")
print("the more players, the more fun")
G=input()
if G=="1":
    P=1
if G=="2":
    P=2
if G=="3":
    P=3
if G=="4":
    P=4
if G=="5":
    P=5
if G=="6":
    P=6
if G=="7":
    P=7
if G=="8":
    P=8
if G=="9":
    P=9
if G=="10":
    P=10  
import random
Invs=["Goblin"]
random.shuffle(Invs)

print("please dont repeat names")
def Attack(target,C):
    if C in Characters:
        target["Health"]-=C["Strength"]/GetPower(C["Inventory"])
    else:
        target["Health"]-=C["Strength"]/12
    if target in Characters:
        C["Health"]-=target["Strength"]/GetPower(target["Inventory"])
    else:
        C["Health"]-=target["Strength"]/12
    if target["Health"]<=0 and target in Creatures:
        print("It's dead")
        for i in target["Drop"]:
            items.append([i,C["Xpos"],C["Ypos"]])
        Creatures.remove(target)
def GetPower(Inventory):
    if "axe-wood" in C["Inventory"]:
       return 3
    elif "Stick" in C["Inventory"]:
       return 5
    else:
       return 6
def CreatureAction(InvNum,InvTime):
    Ho=0
    Mon=0
    if InvNum % len(Invs) and InvTime==0:
        random.shuffle(Invs)
    invType=Invs[InvNum-1]
    if InvTime==0:
        print("The "+invType+"s have invaded")
        if invType=="Goblin":
            p=1
            for i in range(len(MAP)):
                for j in range(len(MAP)):
                    if MAP[i][j]=="cave  ":
                        if random.random()<p/11:
                            items.append(["Goblin Gem",i,j])
                            p=-100
                        else:
                            p+=1
    for C in Creatures:
        C["Health"]=round(C["Health"]*100)/100
        C["Strength"]=round(C["Strength"]*100)/100

        Loc=[C["Xpos"],C["Ypos"]]
        Tar=C["Target"]
        SPr=C["Speed"]
        while SPr>=2:
            if Loc[0]<Tar[0]:
                Loc[0]+=1
                SPr-=1
            if Loc[0]>Tar[0]:
                Loc[0]-=1
                SPr-=1
            if Loc[1]<Tar[1]:
                Loc[1]+=1
                SPr-=1
            if Loc[1]>Tar[1]:
                Loc[1]-=1
                SPr-=1
            SPr-=1
        C["Xpos"]=Loc[0]
        C["Ypos"]=Loc[1]
        if C["Name"]=="Goblin" and "backpack" in C["Drop"]:
            k=random.choice(C["Drop"])
            if not k=="backpack" and not k=="GobelGoop":
                C["Drop"].remove(k)
                items.append([k,Loc[0],Loc[1]])
        if Loc==Tar:
            target=None
            if C["Name"]=="Horse":
                Ho+=1
                Best=[random.randint(0,9),random.randint(0,9)]
                BestDis=20
                if C["Tag"]=="Tame":
                    Best=[Loc[0],Loc[1]]
                    BestDis=5
                for i in Characters:
                    if "Apple" in  i["Inventory"]:
                        if abs(Loc[0]-i["Xpos"])+abs(Loc[1]-i["Ypos"])<BestDis:
                            BestDis=abs(Loc[0]-i["Xpos"])+abs(Loc[1]-i["Ypos"])
                            Best=[i["Xpos"],i["Ypos"]]
                C["Target"]=Best
            if C["Name"]=="Goblin":
                Mon+=1
                Best=[random.randint(0,9),random.randint(0,9)]
                BestDis=20
                for i in Characters:
                    if abs(Loc[0]-i["Xpos"])+abs(Loc[1]-i["Ypos"])<BestDis and not "backpack" in  i["Inventory"]:
                        BestDis=abs(Loc[0]-i["Xpos"])+abs(Loc[1]-i["Ypos"])
                        Best=[i["Xpos"],i["Ypos"]]
                        target=i
                C["Target"]=Best
                if BestDis==0:
                    Attack(target,C)
                    events.append(copy([target["Name"],"A Goblin Attacked you"]))

                    continue
            if C["Name"]=="Goblin":
                BestDis=20
                for i in Characters:
                    if "backpack" in  i["Inventory"]:
                        if abs(Loc[0]-i["Xpos"])+abs(Loc[1]-i["Ypos"])<BestDis:
                            BestDis=abs(Loc[0]-i["Xpos"])+abs(Loc[1]-i["Ypos"])
                            Best=[i["Xpos"],i["Ypos"]]
                            target=i
                C["Target"]=Best
                if BestDis==0:
                    Attack(target,C)
                    for p in i["Inventory"]:
                        i["Inventory"].remove(p)
                        C["Drop"].append(p)
                        C["Speed"]=1
                        events.append(copy([i["Name"],"A Goblin Attacked you"]))
                        continue
            if C["Name"]=="Goblin" and "backpack" in C["Drop"]:
                T=False
                BestDis=20
                for i in Characters:
                    if "Goblin Gem" in  i["Inventory"]:
                        if abs(Loc[0]-i["Xpos"])+abs(Loc[1]-i["Ypos"])<BestDis:
                            BestDis=abs(Loc[0]-i["Xpos"])+abs(Loc[1]-i["Ypos"])
                            Best=[i["Xpos"],i["Ypos"]]
                for i in items:
                    if i[0]=="Goblin Gem":
                        if abs(Loc[0]-i[1])+abs(Loc[1]-i[2])<BestDis:
                            BestDis=abs(Loc[0]-i[1])+abs(Loc[1]-i[2])
                            Best=[i[1],i[2]]
                            T==True
                C["Target"]=Best
                if BestDis==0 and T==True:
                    Creatures.remove(C)
                    continue

    if Ho<5:
        Creatures.append({"Name":"Horse","Health":8,"Strength":6,"Speed":5,"Xpos":random.randint(0,9),"Ypos":random.randint(0,9),"Drop":["Lether"],"Tag":None,"Target":[random.randint(0,9),random.randint(0,9)]})
    if Mon<(InvNum*InvTime)**1/2 and invType=="Goblin":
        for i in items:
            if i[0]=="Goblin Gem":
                LOC=[i[1],i[2]]
        for i in Characters:
            if "Goblin Gem" in i["Inventory"]:
                LOC=[i["Xpos"],i["Ypos"]]
        for i in Creatures:
            if i["Tag"]=="King":
                LOC=[i["Xpos"],i["Ypos"]]

        Creatures.append({"Name":"Goblin","Health":3*(InvNum*InvTime)**.5,"Strength":1*(InvNum*InvTime)**.5,"Speed":4,"Xpos":LOC[0],"Ypos":LOC[1],"Drop":["GobelGoop"],"Tag":None,"Target":[random.randint(0,9),random.randint(0,9)]})

                
for i in range(P):
    Characters.append({"Name":input(),"Health":15,"Strength":5,"Stamina":8,"MentalHealth":10,"Intelegence":10,"Energy":10,"Xpos":0,"Ypos":0,"Inventory":[],"Hunger":10})
FP=Characters[-1]
for i in range(12):
    row=[]
    for j in range(10):
        if i>9:
            row.append("ocean ")
        elif i+j<2:
            row.append("sand  ")
        elif i+j<8:
            row.append("forest")
        elif i>3 and i<6 and j>3 and j<6:
            row.append("grass ")
        elif j>7 and i+j>12:
            row.append("cave  ")
        elif i<4:
            row.append("sand  ")
        elif j>4:
            row.append("grass ")
        elif j<3:
            row.append("sand  ")
        else:
            row.append("forest")

            
            
        
    row.append("ocean ")
    row.append("ocean ")
    MAP.append(row)

for p in range(MapChaos):
    i=random.randint(1,8)
    j=random.randint(1,8)
    k=[-1,1][random.randint(0,1)]
    l=[-1,1][random.randint(0,1)]
    MAP[i][j],MAP[i+k][j+l]=MAP[i+k][j+l],MAP[i][j]
I=[-2,-1,0,1,2]
items=[]
while True:

    C=Characters[0]
    C["Health"]=round(C["Health"]*100)/100
    C["Strength"]=round(C["Strength"]*100)/100
    C["Energy"]=round(C["Energy"]*100)/100
    C["Stamina"]=round(C["Stamina"]*100)/100
    C["Intelegence"]=round(C["Intelegence"]*100)/100
    C["MentalHealth"]=round(C["MentalHealth"]*100)/100
    C["Hunger"]=round(C["Hunger"]*100)/100
    Done=[]
    for event in events:
        if event[0]==C["Name"]:
            print(event[1])
            Done.append(event)
    for event in Done:
        events.remove(event)
    CMD=input().upper()
    if CMD=="FIND LIFE":
        if C["Energy"]>=1 and C["Stamina"]>=1 and C["Intelegence"]>=3:
            print("success")
            C["Stamina"]-=1
            C["Energy"]-=1
            found=[]
            if C["MentalHealth"]<1.5:
                
                for ch in Characters:
                    if ch["Xpos"]==C["Xpos"] and ch["Ypos"]==C["Ypos"]:
                        if random.random()>.75:
                            print("?Friend?")
                            if ch["Intelegence"]>12 and ch["MentalHealth"]>12:
                                C["MentalHealth"]+=.5
                                print("They say They want to help you")
                                events.append(copy([ch["Name"],C["Name"]+" Is going crazy, They need help"]))
                        else:
                            print("?Monster?")
                            found.append(ch)

                for ch in Creatures:
                    if ch["Xpos"]==C["Xpos"] and ch["Ypos"]==C["Ypos"]:
                        if random.random()>.75:
                            print("?Monster?")
                            found.append(ch)

                        else:
                            print("?Friend?")
                if len(found)>0 and C["Strength"]>2 and C["Stamina"]>.8:
                    C["Strength"]+=.6
                    C["Stamina"]-=.8
                    print("Would you like to attack something")
                    print("1-Yes")
                    print("2-No (Unrecognised options will be read as No)")
                    if input()=="1":
                        CMD="END"
                        target=random.choose(found)
                        if target in Characters:
                            events.append(copy([target["Name"],C["Name"]+" attacked you."]))
                            C["MentalHealth"]-=.5
                        Attack(target,C)

            else:
                for ch in Characters:
                    if ch["Xpos"]==C["Xpos"] and ch["Ypos"]==C["Ypos"]:
                        if not ch==C:
                            print(ch["Name"])
                            if ch["MentalHealth"]>7:
                                C["MentalHealth"]+=.5
                            if ch["MentalHealth"]<2 and C["MentalHealth"]<8:
                                C["MentalHealth"]-=.5
                            if ch["MentalHealth"]<2 and C["MentalHealth"]>=12 and C["Intelegence"]>=12:
                                ch["MentalHealth"]+=.5
                            print("would you like to attack")
                            print("1-Yes")
                            print("2-No (Unrecognised options will be read as No)")
                            if input()=="1" and C["Strength"]>2 and C["Stamina"]>.8 and C["Energy"]>1:
                                C["Strength"]+=.6
                                C["Stamina"]-=.8
                                C["Energy"]-=1
                                C["MentalHealth"]-=.5
                                target=ch
                                events.append(copy([target["Name"],C["Name"]+" attacked you."]))

                                Attack(target,C)
                                CMD="END"
                               
                for ch in Creatures:
                    if ch["Xpos"]==C["Xpos"] and ch["Ypos"]==C["Ypos"]:
                        print(ch["Name"])
                        if ch["Name"]=="Horse":
                            print("Would you like to do something")
                            print("1-Feed")
                            print("2-Attack")
                            print("3-No (Unrecognised options will be read as No)")
                            op=input()
                            if op=="1" and "Apple" in C["Inventory"]:
                                C["Inventory"].remove("Apple")
                                print("would you like to get on")
                                print("1-Yes")
                                print("2-No (Unrecognised options will be read as No)")
                                if input()=="1":
                                    ride=[ch,5]
                                else:
                                    ch["Tag"]="Tame"
                            if op=="2" and C["Strength"]>2 and C["Stamina"]>.8 and C["Energy"]>1:
                                C["Strength"]+=.6
                                C["Stamina"]-=.8
                                C["Energy"]-=1
                                target=ch
                                Attack(target,C)
                                CMD="END"

                        if ch["Name"]=="Goblin":
                            if ch["Tag"]=="King":
                                print("It seems to be wearing a crown.")
                            print("would you like to attack")
                            print("1-Yes")
                            print("2-No (Unrecognised options will be read as No)")
                            if input()=="1" and C["Strength"]>2 and C["Stamina"]>.8 and C["Energy"]>1:
                                C["Strength"]+=.6
                                C["Stamina"]-=.8
                                C["Energy"]-=1
                                target=ch
                                Attack(target,C)
                                CMD="END"

    if CMD=="REST":
        print("Rest causes you to drop all your items remember to use Find Things next turn")
        if C["Stamina"]<C["Strength"]+C["Health"]/3:
            C["Stamina"]+=1.5
        if C["Energy"]<C["MentalHealth"]+C["Stamina"]/3:
            C["Energy"]+=1.5
        for i in C["Inventory"]:
            items.append([i,C["Xpos"],C["Ypos"]])
        C["Inventory"]=[]
        CMD="END"
    if CMD=="EAT APPLE":

        if "Apple" in C["Inventory"]:
            print("success")

            C["Inventory"].remove("Apple")
            C["Hunger"]+=1.2
    if CMD=="EAT ROASTED-GOBLE":
        if "Roasted-Goble" in C["Inventory"]:
            print("success")

            C["Inventory"].remove("Roasted-Goble")
            C["Health"]+=2.5
            C["MentalHealth"]-=.4
    if CMD=="BUILD CAMP":
        if C["Energy"]>=4 and C["Stamina"]>=4 and C["Intelegence"]>=12 and "wood" in C["Inventory"] and "Stick" in C["Inventory"] and MAP[C["Xpos"]][C["Ypos"]]=="grass ":
            print("success")
            C["Energy"]-=4
            C["Stamina"]-=4
            C["Inventory"].remove("wood")
            C["Inventory"].remove("Stick")
            C["Intelegence"]+=1.5
            
            MAP[C["Xpos"]][C["Ypos"]]="camp  "
    if CMD=="FIND THINGS":
        if C["Energy"]>=2 and C["Stamina"]>=1.5 and C["Intelegence"]>=5:
            print("success")

            C["Stamina"]-=1.5
            C["Energy"]-=2
            Rem=[]
            for ch in items:
                if ch[1]==C["Xpos"] and ch[2]==C["Ypos"]:
                    if len(C["Inventory"])<3 or (len(C["Inventory"])<10 and "backpack" in C["Inventory"]):
                        print("Would you like to pick up "+ch[0])
                        print("1-Yes")
                        print("2-No (Unrecognised options will be read as No)")
                        if input()=="1":
                            C["Inventory"].append(ch[0])
                            #items.remove(ch)
                            Rem.append(ch)
                        C["Intelegence"]+=.2
                    print(ch[0])
            for i in Rem:
                items.remove(i)
    if CMD=="HYPER FOCUS":
        if C["MentalHealth"]>=1.2:
            print("success")

            C["Energy"]+=1.2
            C["MentalHealth"]-=1.2
    if CMD=="CLEAN":
        if C["Energy"]>=1.5 and C["Stamina"]>=1.5 and C["MentalHealth"]>=6.5:
            print("success")
            C["Energy"]-=1.5
            C["Stamina"]-=1.5
            for ch in items:
                if ch[1]==C["Xpos"] and ch[2]==C["Ypos"]:
                    C["MentalHealth"]-=.4
                    items.remove(ch)
    if CMD=="LOOK AROUND":
        if C["Energy"]>=1:
            print("success")

            C["Energy"]-=1
            for i in I:
                ST=""
                for j in I:
                    if i==0 and j==0:
                        ST+=(MAP[C["Xpos"]+j][C["Ypos"]+i]+" ").upper()
                    else:
                        ST+=MAP[C["Xpos"]+j][C["Ypos"]+i]+" "
                print(ST)
    if CMD=="CRAFT AXE-WOOD":
        if C["Energy"]>=2 and C["Stamina"]>=3 and C["Intelegence"]>=6 and C["Strength"]>=5 and "wood" in C["Inventory"] and "Stick" in C["Inventory"] and MAP[C["Xpos"]][C["Ypos"]]=="camp  ":
            print("success")

            C["Stamina"]-=3
            C["Energy"]-=2
            C["Intelegence"]+=1
            C["Inventory"].remove("Stick")
            C["Inventory"].remove("wood")
            C["Inventory"].append("axe-wood")
    if CMD=="CRAFT BACKPACK":
        if C["Energy"]>=6 and C["Intelegence"]>=15 and "Lether" in C["Inventory"] and MAP[C["Xpos"]][C["Ypos"]]=="camp  ":
            print("success")

            C["Energy"]-=6
            C["Intelegence"]+=2.5
            C["Inventory"].remove("Lether")
            C["Inventory"].append("backpack")
    if CMD=="CRAFT ROASTED-GOBEL":
        if C["MentalHealth"]>=8 and C["Energy"]>=3 and "GobelGoop" in C["Inventory"] and MAP[C["Xpos"]][C["Ypos"]]=="camp  ":
            print("success")

            C["Energy"]-=3
            C["MentalHealth"]-=1.5
            C["Inventory"].remove("GobelGoop")
            C["Inventory"].append("Roasted-Gobel")
    if CMD=="CRAFT GOBLIN-KING":
        if C["MentalHealth"]>=10 and "Roasted-Gobel" in C["Inventory"] and "Goblin Gem" in C["Inventory"] and MAP[C["Xpos"]][C["Ypos"]]=="camp  ":
            print("success")

            C["MentalHealth"]+=3
            C["Health"]-=3
            C["Inventory"].remove("Roasted-Gobel")
            C["Inventory"].remove("Goblin Gem")
            Creatures.append({"Name":"Goblin","Health":10*(InvNum*InvTime)**1/2,"Strength":3*(InvNum*InvTime)**1/2,"Speed":2,"Xpos":C["Xpos"],"Ypos":C["Ypos"],"Drop":["Peace"],"Tag":"King","Target":[C["Xpos"],C["Ypos"]]})
    if CMD=="GET WOOD":
        if (len(C["Inventory"])<3 or (len(C["Inventory"])<10 and "backpack" in C["Inventory"])):
            if "axe-wood" in C["Inventory"]:

                if C["Stamina"]>=3 and C["Energy"]>=3 and C["Strength"]>=4 and MAP[C["Xpos"]][C["Ypos"]]=="forest":
                    print("success")

                    C["Stamina"]-=3
                    C["Energy"]-=3
                    C["Strength"]+=2
                    C["Inventory"].append("wood")
                    if (len(C["Inventory"])<3 or (len(C["Inventory"])<10 and "backpack" in C["Inventory"])) and C["Intelegence"]>4:
                        print("you found an apple tree")
                        C["Intelegence"]+=.5
                        C["Inventory"].append("Apple")
                        items.append(["Apple",C["Xpos"],C["Ypos"]])
                        items.append(["Apple",C["Xpos"],C["Ypos"]])
                        items.append(["Apple",C["Xpos"],C["Ypos"]])
                    for i in range(10):
                        if random.random()>.8:
                            items.append(["Stick",C["Xpos"],C["Ypos"]])

                
            else:
                if (len(C["Inventory"])<3 or (len(C["Inventory"])<10 and "backpack" in C["Inventory"])) and C["Stamina"]>=5 and C["Energy"]>=5 and C["Strength"]>=6 and MAP[C["Xpos"]][C["Ypos"]]=="forest":
                    print("success")

                    C["Stamina"]-=5
                    C["Energy"]-=5
                    C["Strength"]+=2
                    C["Health"]-=1
                    C["Inventory"].append("wood")
                    if (len(C["Inventory"])<3 or (len(C["Inventory"])<10 and "backpack" in C["Inventory"])) and C["Intelegence"]>4:
                        print("you found an apple tree")
                        C["Intelegence"]+=.5
                        C["Inventory"].append("Apple")
                        items.append(["Apple",C["Xpos"],C["Ypos"]])
                        items.append(["Apple",C["Xpos"],C["Ypos"]])
                        items.append(["Apple",C["Xpos"],C["Ypos"]])
                    for i in range(10):
                        if random.random()>.8:
                            items.append(["Stick",C["Xpos"],C["Ypos"]])
    if ride==[]:
        if CMD=="GO UP":
            if C["Stamina"]>=1 and C["Energy"]>=1 and not MAP[C["Xpos"]][C["Ypos"]-1]=="ocean ":
                print("success")
                C["Stamina"]-=1
                C["Energy"]-=1
                C["Ypos"]-=1
        if CMD=="GO DOWN":
            if C["Stamina"]>=1 and C["Energy"]>=1 and not MAP[C["Xpos"]][C["Ypos"]+1]=="ocean ":
                print("success")

                C["Stamina"]-=1
                C["Energy"]-=1
                C["Ypos"]+=1
        if CMD=="GO LEFT":
            if C["Stamina"]>=1 and C["Energy"]>=1 and not MAP[C["Xpos"]-1][C["Ypos"]]=="ocean ":
                print("success")

                C["Stamina"]-=1
                C["Energy"]-=1
                C["Xpos"]-=1
        if CMD=="GO RIGHT":
            if C["Stamina"]>=1 and C["Energy"]>=1 and not MAP[C["Xpos"]+1][C["Ypos"]]=="ocean ":
                print("success")

                C["Stamina"]-=1
                C["Energy"]-=1
                C["Xpos"]+=1
        if CMD=="RUN UP":
            if C["Strength"]>=3 and C["Stamina"]>=2 and C["Energy"]>=.4 and not MAP[C["Xpos"]][C["Ypos"]-1]=="ocean ":
                print("success")

                C["Stamina"]-=2
                C["Energy"]-=.4
                C["Strength"]+=.5
                C["Ypos"]-=1
        if CMD=="RUN DOWN":
            if C["Strength"]>=3 and C["Stamina"]>=2 and C["Energy"]>=.4 and not MAP[C["Xpos"]][C["Ypos"]+1]=="ocean ":
                print("success")

                C["Stamina"]-=2
                C["Energy"]-=.4
                C["Strength"]+=.5
                C["Ypos"]+=1
        if CMD=="RUN LEFT":
            if C["Strength"]>=3 and C["Stamina"]>=2 and C["Energy"]>=.4 and not MAP[C["Xpos"]-1][C["Ypos"]]=="ocean ":
                print("success")

                C["Stamina"]-=2
                C["Energy"]-=.4
                C["Strength"]+=.5
                C["Xpos"]-=1
        if CMD=="RUN RIGHT":
            if C["Strength"]>=3 and C["Stamina"]>=2 and C["Energy"]>=.4 and not MAP[C["Xpos"]+1][C["Ypos"]]=="ocean ":
                print("success")

                C["Stamina"]-=2
                C["Energy"]-=.4
                C["Strength"]+=.5
                C["Xpos"]+=1
    else:
        if CMD=="RIDE UP":
            if ride[0]>0 and not MAP[C["Xpos"]][C["Ypos"]-1]=="ocean ":
                print("success")

                ride[0]-=1
                C["Ypos"]-=1
                ride[1]["Ypos"]-=1
        if CMD=="RIDE DOWN":
            if ride[0]>0 and not MAP[C["Xpos"]][C["Ypos"]+1]=="ocean ":
                print("success")

                ride[0]-=1
                C["Ypos"]+=1
                ride[1]["Ypos"]+=1
        if CMD=="RIDE LEFT":
            if ride[0]>0 and not MAP[C["Xpos"]-1][C["Ypos"]]=="ocean ":
                print("success")

                ride[0]-=1
                C["Xpos"]-=1
                ride[1]["Xpos"]-=1
        if CMD=="RIDE RIGHT":
            if ride[0]>0 and not MAP[C["Xpos"]+1][C["Ypos"]]=="ocean ":
                print("success")

                ride[0]-=1
                C["Xpos"]+=1
                ride[1]["Xpos"]+=1
    if CMD=="STATS":
        print(C)
    if CMD=="END":
        ride=[]
        C["MentalHealth"]-=.1
        if C["Stamina"]<C["Strength"]+C["Health"]/3:
            if MAP[C["Xpos"]][C["Ypos"]]=="camp  ":
                C["Stamina"]+=2*C["Health"]/5-.1
            else:
                
                C["Stamina"]+=C["Health"]/5-.1
        if C["Energy"]<C["MentalHealth"]+C["Stamina"]/3:
            if MAP[C["Xpos"]][C["Ypos"]]=="camp  ":
                C["Energy"]+=2*C["MentalHealth"]/5-.1
            else:
                C["Energy"]+=C["MentalHealth"]/5-.1
        if C["Energy"]<2:
            C["MentalHealth"]-=1
        if C["MentalHealth"]<4:
            C["Intelegence"]-=1
        if C["MentalHealth"]<0:
            C["Intelegence"]+=C["MentalHealth"]
        if C["Health"]<4:
            C["Strength"]-=1

        if C["Stamina"]<2:
            C["Health"]-=1
        if C["Hunger"]<1:
            C["Health"]-=1
        else:
            C["Hunger"]-=1
        if C["Hunger"]>=7.5 and C["Health"]<=10:
            C["Health"]+=.5
        
        if C["Health"]<=0:
            items.append(["body",C["Xpos"],C["Ypos"]])
            for i in C["Inventory"]:
                items.append([i,C["Xpos"],C["Ypos"]])
            if C==FP:
                FP=Characters[-1]
            Characters.remove(C)
        if ["Peace",C["Xpos"],C["Ypos"]] in items:
            peace=5
            InvTime=-1
            items.remove(["Peace",C["Xpos"],C["Ypos"]])
        Characters.append(C)
        Characters.remove(C)
        print(Characters[0]["Name"]+"'s turn.")
        if C==FP:
            CreatureAction(InvNum,InvTime)
            if peace==0:
                InvTime+=1
            else:
                peace-=1
                if peace==0:
                    InvNum+=1
                    InvTime=0
        for i in items:
            L=False
            for c in Characters:
                if i[1]==c["Xpos"] and i[2]==c["Ypos"]:
                    c["MentalHealth"]-=.3/len(Characters)
                    L=True
            if L==False:
                if random.random()<.6/len(Characters) and not i[0]=="Goblin Gem" and not i[0]=="Peace":
                    items.remove(i)
            
            

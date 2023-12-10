import pygame,time,random
from pygame.locals import*
from copy import deepcopy
import sys
import math
import wx
ST=True
app = wx.App(False)
width, Height = wx.GetDisplaySize()
pygame.init()
mountain=(0,0,0)
water=(0,0,255)
ocean=(0,0,200)
sand=(255,255,0)
King=(200,200,50)
grass=(0,255,0)
forest=(0,127,0)
error=(255,0,255)
worker=(255,127,0)
port=(0,255,255)
rock=(50,50,50)
boat=sand
farm=sand
darkRed=(127,0,0)
darkBlue=(0,0,127)
darkGreen=(0,127,0)
darkYellow=(127,127,0)
darkBrown=(127,63,0)
P1=darkBlue
P2=darkGreen
P3=darkRed
P4=darkYellow
P5=darkBrown
wood=(127,63,0)
stone=(127,127,127)
lumber=(63,21,0)
jet=(200,200,200)
bomber=(100,100,100)
Bless=(200,200,90)
CurseG=(130,0,0)
CurseA=(25,25,25)
Ice=(127,127,255)
Fairy=(200,100,150)
Builder=(100,0,0)
Artillary=(0,0,90)
Armory=(150,150,150)
RedBarracks=(75,0,0)

Govenor=(30,30,30)

airport=error
Human="p1"
Elf="p2"
Dwarf="p3"
Orc="p4"
Monster="p5"
windowSurface=pygame.display.set_mode((width,Height),FULLSCREEN)
print(pygame.Surface.get_height(windowSurface))
print(pygame.Surface.get_width(windowSurface))
#units=[["worker",7,37,True,"p1",5],["worker",37,7,True,"p2",5],["worker",7,7,True,"p3",5],["worker",37,37,True,"p4",5],["diplomat",5,37,True,"p2",4,"",[None,0],[None,0]],["diplomat",6,37,True,"p1",4,"",[None,0],[None,0]],["diplomat",8,32,True,"p1",4,"",[None,0],[None,0]],["diplomat",9,32,True,"p3",4,"",[None,0],[None,0]]]
pygame.display.set_caption('conquestia')
Hstart=[["worker",6,37,True,Human,5],["king",7,38,True,Human,15]]
Estart=[["worker",6,7,True,Elf,5],["king",7,6,True,Elf,15]]
Dstart=[["builder",38,37,True,Dwarf,5],["king",37,38,True,Dwarf,15]]
Ostart=[["worker",38,7,True,Orc,5],["king",37,6,True,Orc,15]]
Mstart=[["worker",7,37,True,Monster,5],["king",6,38,True,Monster,15]]
units=Hstart+Estart+Dstart+Ostart
players=[1,1,1,1]
buildings=[]
resourses=[[10,0,2,0,0,0],[10,0,2,0,0,0],[10,0,2,0,0,0],[10,0,2,0,0,0]]
turn="p1"
inAGame=False
def coin():
        return random.random()>.5
MAP=[]
p1MAP=[]
p2MAP=[]
p3MAP=[]
p4MAP=[]
pMAP=[]
for n in range(5):
    line=[]
    for m in range(45):
        line.append(True)
    pMAP.append(line)
for a in range(35):
    line=[]
    for n in range(5):
        line.append(True)
    for b in range(35):
        line.append(True)
    for n in range(5):
        line.append(True)
    pMAP.append(line)
for n in range(5):
    line=[]
    for m in range(45):
        line.append(True)
    pMAP.append(line)
def BuildOwn(Loc, Units,P):
    own1=False
    own2=False
    own3=False
    own4=False
    d1=[-1,0,1]
    d2=[-2,-1,0,1,2]
    d3=[-3,-2,-1,0,1,2,3]
    for unit in Units:
        dif=[Loc[0]-unit[1],Loc[1]-unit[2]]
        if unit[0]=="govenor" or unit[0]=="king" and dif[0] in d3 and dif[1] in d3:
            JJ=True
            for unit2 in Units:
                if unit2[4]!=unit[4] and not unit2[0]=="jet" and not unit2[0]=="bomber" and unit2[1]-unit[1] in d2 and unit2[2]-unit[2] in d2:
                    JJ=False
            if JJ:
                if unit[4]=="p1":
                    own1=True
                if unit[4]=="p2":
                    own2=True
                if unit[4]=="p3":
                    own3=True
                if unit[4]=="p4":
                    own4=True
        if not unit[0] in ["jet","bomber"] and dif[0] in d1 and dif[1] in d1:
            if unit[4]=="p1":
                own1=True
            if unit[4]=="p2":
                own2=True
            if unit[4]=="p3":
                own3=True
            if unit[4]=="p4":
                own4=True
    if own1+own2+own3+own4==1:
        if own1:
            return P=="p1"
        if own2:
            return P=="p2"
        if own3:
            return P=="p3"
        if own4:
            return P=="p4"
def genWorld(MAP,p1MAP,p2MAP,p3MAP,p4MAP):
    zones=[]
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(True)
        p1MAP.append(line)
    for a in range(35):
        line=[]
        for n in range(5):
            line.append(True)
        for b in range(35):
            line.append(False)
        for n in range(5):
            line.append(True)
        p1MAP.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(True)
        p1MAP.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(True)
        p2MAP.append(line)
    for a in range(35):
        line=[]
        for n in range(5):
            line.append(True)
        for b in range(35):
            line.append(False)
        for n in range(5):
            line.append(True)
        p2MAP.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(True)
        p2MAP.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(True)
        p3MAP.append(line)
    for a in range(35):
        line=[]
        for n in range(5):
            line.append(True)
        for b in range(35):
            line.append(False)
        for n in range(5):
            line.append(True)
        p3MAP.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(True)
        p3MAP.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(True)
        p4MAP.append(line)
    for a in range(35):
        line=[]
        for n in range(5):
            line.append(True)
        for b in range(35):
            line.append(False)
        for n in range(5):
            line.append(True)
        p4MAP.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(True)
        p4MAP.append(line)
    for m in range(9):
        line=[]
        for n in range(9):
            if m==4 or n==4 or m==0 or n==0 or m==8 or n==8:
                line.append(water)
            elif (m==1 or m==7) and (n==1 or n==7):
                line.append(forest)
            elif (m==3 or m==5) and (n==3 or n==5):
                line.append(mountain)
            elif coin():
                if coin():
                    line.append(mountain)
                else:
                    line.append(forest)
            else:
                if coin():
                    line.append(grass)
                else:
                    line.append(water)
        zones.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(water)
        MAP.append(line)
    for a in range(35):
        line=[]
        for n in range(5):
            line.append(water)
        for b in range(35):
            line.append(error)
        for n in range(5):
            line.append(water)
        MAP.append(line)
    for n in range(5):
        line=[]
        for m in range(45):
            line.append(water)
        MAP.append(line)
    for a in range(7):
        for b in range(7):

            MAP[5*a+5+2][5*b+5+2]=zones[a+1][b+1]
            MAP[5*a+5+1][5*b+5+2]=zones[a+1][b+1]
            MAP[5*a+5+3][5*b+5+2]=zones[a+1][b+1]
            MAP[5*a+5+2][5*b+5+1]=zones[a+1][b+1]
            MAP[5*a+5+2][5*b+5+3]=zones[a+1][b+1]
    for a in range(7):
        for b in range(7):
            for c in range(2):
                if coin():
                    MAP[5*a+5+2][5*b+5+2+round(4*(c-.5))]=MAP[5*a+5+2][5*b+5+2]
                else:
                    if MAP[5*a+5+2][5*b+5+2] in [water,grass] and MAP[5*a+5+2][5*b+5+2+round(10*(c-.5))] in [water,grass]:
                        MAP[5*a+5+2][5*b+5+2+round(4*(c-.5))]=sand
                    elif MAP[5*a+5+2][5*b+5+2] in [mountain,forest] and MAP[5*a+5+2][5*b+5+2+round(10*(c-.5))] in [mountain,forest]:
                        MAP[5*a+5+2][5*b+5+2+round(4*(c-.5))]=water
                    else:
                        MAP[5*a+5+2][5*b+5+2+round(4*(c-.5))]=MAP[5*a+5+2][5*b+5+2+round(10*(c-.5))]
 
                if coin():
                    MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2]=MAP[5*a+5+2][5*b+5+2]
                else:
                    if MAP[5*a+5+2][5*b+5+2] in [water,grass] and MAP[5*a+5+2+round(10*(c-.5))][5*b+5+2] in [water,grass]:
                        MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2]=sand
                    elif MAP[5*a+5+2][5*b+5+2] in [mountain,forest] and MAP[5*a+5+2+round(10*(c-.5))][5*b+5+2] in [mountain,forest]:
                        MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2]=water
                    else:
                        MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2]=MAP[5*a+5+2+round(10*(c-.5))][5*b+5+2]
    for a in range(7):
        for b in range(7):
            for c in range(2):
                for d in range(2):
                    if coin():
                        MAP[5*a+5+2+round(2*(c-.5))][5*b+5+2+round(2*(d-.5))]=zones[a+1][b+1]
                    else:
                        if zones[a+1][b+1] in [mountain,forest]:
                            MAP[5*a+5+2+round(2*(c-.5))][5*b+5+2+round(2*(d-.5))]=grass
                        elif zones[a+1][b+1]==grass:
                            MAP[5*a+5+2+round(2*(c-.5))][5*b+5+2+round(2*(d-.5))]=rock
                        elif zones[a+1][b+1]==water:
                            MAP[5*a+5+2+round(2*(c-.5))][5*b+5+2+round(2*(d-.5))]=ocean
                            
    for a in range(7):
        for b in range(7):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        x=MAP[5*a+5+2+2*round(2*(c-.5))*e][5*b+5+2+2*round(2*(d-.5))*(1-e)]
                        y=MAP[5*a+5+2+round(2*(c-.5))][5*b+5+2+round(2*(d-.5))]
                        z=MAP[5*a+5+2+round(2*(c-.5))+round(2*(c-.5))*e][5*b+5+2+round(2*(d-.5))+round(2*(d-.5))*(1-e)]
                        if x==y:
                            if coin():
                                MAP[5*a+5+2+round(2*(c-.5))+round(2*(c-.5))*e][5*b+5+2+round(2*(d-.5))+round(2*(d-.5))*(1-e)]=x
                            else:
                                if x in [mountain,forest]:
                                    MAP[5*a+5+2+round(2*(c-.5))+round(2*(c-.5))*e][5*b+5+2+round(2*(d-.5))+round(2*(d-.5))*(1-e)]=grass
                                if x==water:
                                    MAP[5*a+5+2+round(2*(c-.5))+round(2*(c-.5))*e][5*b+5+2+round(2*(d-.5))+round(2*(d-.5))*(1-e)]=ocean
                                if x==grass:
                                    MAP[5*a+5+2+round(2*(c-.5))+round(2*(c-.5))*e][5*b+5+2+round(2*(d-.5))+round(2*(d-.5))*(1-e)]=forest
                                if x==sand:
                                    MAP[5*a+5+2+round(2*(c-.5))+round(2*(c-.5))*e][5*b+5+2+round(2*(d-.5))+round(2*(d-.5))*(1-e)]=rock
                        else:
                            if coin():
                                MAP[5*a+5+2+round(2*(c-.5))+round(2*(c-.5))*e][5*b+5+2+round(2*(d-.5))+round(2*(d-.5))*(1-e)]=x
                            else:
                                MAP[5*a+5+2+round(2*(c-.5))+round(2*(c-.5))*e][5*b+5+2+round(2*(d-.5))+round(2*(d-.5))*(1-e)]=y

    for a in range(7):
        for b in range(7):
            for c in range(2):
                for d in range(2):
                    x=MAP[5*a+5+2+round(2*(c-.5))][5*b+5+2+round(4*(d-.5))]
                    y=MAP[5*a+5+2+2*round(2*(c-.5))][5*b+5+2+round(2*(d-.5))]
                    z=MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]

                    if x==y:
                        if coin():
                            MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=x
                        else:

                            if x in [mountain,forest]:
                                MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=grass
                            elif x==water:
                                MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=ocean
                            elif x == grass:
                                MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=water
                            
                            if x==sand:
                                MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=rock
                            if x==rock:
                                MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=sand
                            if x==ocean:
                                MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=water
                            

                    else:
                        if coin():
                            MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=x
                        else:
                            MAP[5*a+5+2+round(4*(c-.5))][5*b+5+2+round(4*(d-.5))]=y
#ADD IN THE NEW UNITS WHEN UPDATE IS "FINISHED"
def drawMAP(MAP,p1MAP):
    H=pygame.Surface.get_height(windowSurface)
    W=pygame.Surface.get_width(windowSurface)
    C=(W-H)/2
    width,Height=wx.GetDisplaySize()
    Coef=round(1/45*Height)
    Add1=round(3/20*Coef)
    Add2=Coef-Add1
    Add3=round(Add1*3.5)
    Add4=Coef-Add3
    Add5=round(Add1*2)
    Add6=Coef-Add5
    windowSurface.fill((255,255,255))
    for a in range(45):
        for b in range(45):
            if p1MAP[a][b]:
                pygame.draw.polygon(windowSurface,MAP[a][b],((Coef*a+C,Coef*b),(Coef*a+C,Coef*b+Coef),(Coef*a+Coef+C,Coef*b+Coef),(Coef*a+Coef+C,Coef*b)))
    for building in buildings:
        if p1MAP[building[1]][building[2]]:
            unit=building
            if building[0]=="fishing spot":
                pygame.draw.polygon(windowSurface,wood,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
  
            if building[0]=="port":
                pygame.draw.polygon(windowSurface,port,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="farm":
                pygame.draw.polygon(windowSurface,farm,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="wood mine":
                pygame.draw.polygon(windowSurface,wood,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="stone mine":
                pygame.draw.polygon(windowSurface,stone,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="lumber hut":
                pygame.draw.polygon(windowSurface,lumber,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="house":
                if building[5]==1:
                    pygame.draw.polygon(windowSurface,wood,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
                else:
                    pygame.draw.polygon(windowSurface,stone,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="barracks":
                pygame.draw.polygon(windowSurface,(255,255,255),((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="wall":
                pygame.draw.polygon(windowSurface,mountain,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="airport":
                pygame.draw.polygon(windowSurface,error,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="wood statue":
                pygame.draw.polygon(windowSurface,lumber,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="stone statue":
                pygame.draw.polygon(windowSurface,forest,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="metal statue":
                pygame.draw.polygon(windowSurface,port,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="gold statue":


                pygame.draw.polygon(windowSurface,(255,255,167),((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="artillary":


                pygame.draw.polygon(windowSurface,Artillary,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="hospital":


                pygame.draw.polygon(windowSurface,Hospital,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="armory":


                pygame.draw.polygon(windowSurface,Armory,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))
            if building[0]=="bank":


                pygame.draw.polygon(windowSurface,Bank,((Coef*unit[1]+Add1+C,Coef*unit[2]+Add1),(Coef*unit[1]+Add1+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add2),(Coef*unit[1]+Add2+C,Coef*unit[2]+Add1)))

            unit=building
    for unit in units:
        if p1MAP[unit[1]][unit[2]]:
            if unit[0]=="king":
                pygame.draw.polygon(windowSurface,King,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))

            if unit[0]=="govenor":
                pygame.draw.polygon(windowSurface,(30,30,30),((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))

            if unit[0]=="worker":
                pygame.draw.polygon(windowSurface,worker,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if type(unit[0])==list:
                pygame.draw.polygon(windowSurface,sand,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="swordman":

                pygame.draw.polygon(windowSurface,(255,0,0),((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="builder":
                pygame.draw.polygon(windowSurface,Builder,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="blessed one":
                pygame.draw.polygon(windowSurface,Bless,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="cursed one ground":
                pygame.draw.polygon(windowSurface,CurseG,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="cursed one air":
                pygame.draw.polygon(windowSurface,CurseA,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="ice wizard":
                pygame.draw.polygon(windowSurface,Ice,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="fairy":
                pygame.draw.polygon(windowSurface,Fairy,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))

            if unit[0]=="runner" or unit[0]=="green":
                pygame.draw.polygon(windowSurface,(0,99,0),((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="archer":
                pygame.draw.polygon(windowSurface,(0,0,255),((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="bomber":
                pygame.draw.polygon(windowSurface,bomber,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="jet":
                pygame.draw.polygon(windowSurface,jet,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[4]=="p1":
                pygame.draw.polygon(windowSurface,P1,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[4]=="p2":
                pygame.draw.polygon(windowSurface,P2,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[4]=="p3":
                pygame.draw.polygon(windowSurface,P3,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[4]=="p4":
                pygame.draw.polygon(windowSurface,P4,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))


            if not unit[3]:
                pygame.draw.polygon(windowSurface,mountain,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
    if not pygame.display.get_caption()==():
        text(pygame.display.get_caption()[0],mountain,Height/2+C,Height*1/18,round(Height*1/60))
    pygame.display.update()
genWorld(MAP,p1MAP,p2MAP,p3MAP,p4MAP)
def damageCalc(AT,DEF,units,buildings):
    D2=[-2,-1,0,1,2]
    D3=[-3,-2,-1,0,1,2,3]
    ATP=1
    if AT[0]=="swordman" or AT[0]=="red":
        ATP=4*AT[6]
    if AT[0]=="archer" or type(AT[0])==list:
        if type(AT[0])==list:
                ATP=2*AT[0][1][6]
        else:
 
                ATP=2*AT[6]
    if AT[0]=="runner" or AT[0]=="green":
        ATP=1*AT[6]
    if AT[4]==Orc or AT[4]==Monster:
        ATP*=2
    if AT[4]==Human or AT[4]==Monster:
        for unit in units:
            if unit[0]=="blessed one" and unit[4]==AT[4]:
                if unit[1]-AT[1] in D2 and unit[2]-AT[2] in D3:
                    ATP*=3
                    break
    for unit in units:
        if unit[0]=="cursed one ground" and not unit[4]==AT[4]:
            if unit[1]-AT[1] in D3 and unit[2]-AT[2] in D3:
                ATP/=3
                break
    if AT[4]==Elf:
        for unit in units:
            if unit[0]=="fairy":
                if unit[1]-AT[1] in D2 and unit[2]-AT[2] in D3:
                    ATP*=2
                    break
    else:
        for unit in units:
            if unit[0]=="ice wizard":
                if unit[1]-AT[1] in D3 and unit[2]-AT[2] in D3:
                    ATP/=3
                    break
    if not AT[4]==Dwarf and not AT[4]==Monster and AT[6]==3.5:
        P=.5
        for unit in units:
            if unit[6]==3.5:
                if unit[1]-AT[1] in D3 and unit[2]-AT[2] in D3:
                    P+=.5
        ATP*=min(P,3.5)
    if AT[4]==Dwarf and AT[6]==3.5:
        P=1
        for unit in units:
            if unit[6]==3.5:
                if unit[1]-AT[1] in D3 and unit[2]-AT[2] in D3:
                    P+=1
        ATP*=min(P,6)
    for building in buildings:
        if building[0]=="armory":
            if unit[1]-DEF[1] in D3 and unit[2]-DEF[2] in D3:
                if AT[4]==Dwarf:
                    ATP/=3
                elif not AT[4]==Monster:
                    ATP/=2
                break
    return round(ATP)
def buildInfo(unit,resourses,player):
    string=" "
    string="health-"+str(unit[4])
    if len(unit)>5:
        if player==Human:
            string+=" 1-worker 2-swordman 3-runner 4-archer 5-Govenor"
        if player==Orc or player==Monster:
            string+=" 1-worker 2-knifer 3-dog 4-snake 5-Govenor"
        if player==Elf:
            string+=" 1-worker 2-swordman 3-runner 4-archer 5-Govenor"
        if player==Dwarf:
            string+=" 1-builder 2-swordman 3-runner 4-archer 5-Govenor"

    if unit[0]=="airport":
        string+=" 1-bomber 2-jet"

    return string
def text(words,color,x,y,size):
    basicFont=pygame.font.SysFont(None,size)
    text=basicFont.render(words,True,color,(255,255,255))

    textRect=text.get_rect()
    textRect.centerx=x
    textRect.centery=y
    windowSurface.blit(text,textRect)
def unitInfo(unit,resourses,MAP):
    string=" "
    string="health-"+str(unit[5])
    if len(unit)==7:
        string+=" lv-"+str(unit[6])
    if type(unit[0])==list:
        if unit[0][1][0]=="green":
            string+=" "+"runner"
        else:
                string+=" "+unit[0][1][0]
    return string
def DWARF(P):
    for building in buildings:
        if building[0]=="red barracks" and building[3]==P:
            return False
    J=0
    for unit in units:
        if unit[4]==P:
            if len(unit)==7 and unit[6]==3.5 or (type(unit[0])==list and unit[0][1][6]==3.5):
                J+=1
    if J>=3:
        return False
    else:
        for unit in units:
            if unit[4]==P:
                if len(unit)==7 and unit[6]==3.5:
                    unit[6]=3
    return True
                
def ELF():
    X=0
    IC=False
    for unit in units:
        if unit[0]=="fairy" or (type(unit[0])==list and unit[0][1][0]=="fairy"):
            X+=1
        if unit[0]=="ice wizard" or (type(unit[0])==list and unit[0][1][0]=="ice wizard"):
            IC=True
    if resourses[1][5]>=10:
        if not IC:
            for unit in units:
                if unit[0]=="king" and unit[4]==Elf:
                    if guyCheck([unit[1],unit[2]+1],units)==False and MAP[unit[1]][unit[2]+1] not in [water,ocean]:
                        units.append(["ice wizard",unit[1],unit[2]+1,False,Elf,10])
                        return
                    elif guyCheck([unit[1],unit[2]-1],units)==False and MAP[unit[1]][unit[2]-1] not in [water,ocean]:
                        units.append(["ice wizard",unit[1],unit[2]-1,False,Elf,10])
                        return
                    elif guyCheck([unit[1]+1,unit[2]],units)==False and MAP[unit[1]+1][unit[2]] not in [water,ocean]:
                        units.append(["ice wizard",unit[1]+1,unit[2],False,Elf,10])
                        return
                    elif guyCheck([unit[1-1],unit[2]],units)==False and MAP[unit[1]-1][unit[2]] not in [water,ocean]:
                        units.append(["ice wizard",unit[1]-1,unit[2],False,Elf,10])
                        return
        elif X<2:
            for unit in units:
                if unit[0]=="king" and unit[4]==Elf:
                    if guyCheck([unit[1],unit[2]+1],units)==False and MAP[unit[1]][unit[2]+1] not in [water,ocean]:
                        units.append(["fairy",unit[1],unit[2]+1,False,Elf,10])
                        return
                    elif guyCheck([unit[1],unit[2]-1],units)==False and MAP[unit[1]][unit[2]-1] not in [water,ocean]:
                        units.append(["fairy",unit[1],unit[2]-1,False,Elf,10])
                        return
                    elif guyCheck([unit[1]+1,unit[2]],units)==False and MAP[unit[1]+1][unit[2]] not in [water,ocean]:
                        units.append(["fairy",unit[1]+1,unit[2],False,Elf,10])
                        return
                    elif guyCheck([unit[1-1],unit[2]],units)==False and MAP[unit[1]-1][unit[2]] not in [water,ocean]:
                        units.append(["fairy",unit[1]-1,unit[2],False,Elf,10])
                        return
def HUMAN():
    X=False
    IC=False
    for unit in units:
        if unit[0]=="blessed one" or (type(unit[0])==list and unit[0][1][0]=="blessed one"):
            IC=True
        if unit[0] in ["cursed one air","cursed one ground"] or (type(unit[0])==list and unit[0][1][0] in  ["cursed one air","cursed one ground"]):
            X=True
    if resourses[0][5]>=10:
        if not IC:
            for unit in units:
                if unit[0]=="king" and unit[4]==Human:
                    if guyCheck([unit[1],unit[2]+1],units)==False and MAP[unit[1]][unit[2]+1] not in [water,ocean]:
                        units.append(["blessed one",unit[1],unit[2]+1,False,Human,15])
                        return
                    elif guyCheck([unit[1],unit[2]-1],units)==False and MAP[unit[1]][unit[2]-1] not in [water,ocean]:
                        units.append(["blessed one",unit[1],unit[2]-1,False,Human,15])
                        return
                    elif guyCheck([unit[1]+1,unit[2]],units)==False and MAP[unit[1]+1][unit[2]] not in [water,ocean]:
                        units.append(["blessed one",unit[1]+1,unit[2],False,Human,15])
                        return
                    elif guyCheck([unit[1-1],unit[2]],units)==False and MAP[unit[1]-1][unit[2]] not in [water,ocean]:
                        units.append(["blessed one",unit[1]-1,unit[2],False,Human,15])
                        return
        elif not X:
            for unit in units:
                if unit[0]=="king" and unit[4]==Human:
                    if guyCheck([unit[1],unit[2]+1],units)==False and MAP[unit[1]][unit[2]+1] not in [water,ocean]:
                        units.append(["cursed one air",unit[1],unit[2]+1,False,Human,10])
                        return
                    elif guyCheck([unit[1],unit[2]-1],units)==False and MAP[unit[1]][unit[2]-1] not in [water,ocean]:
                        units.append(["cursed one air",unit[1],unit[2]-1,False,Human,10])
                        return
                    elif guyCheck([unit[1]+1,unit[2]],units)==False and MAP[unit[1]+1][unit[2]] not in [water,ocean]:
                        units.append(["cursed one air",unit[1]+1,unit[2],False,Human,10])
                        return
                    elif guyCheck([unit[1-1],unit[2]],units)==False and MAP[unit[1]-1][unit[2]] not in [water,ocean]:
                        units.append(["cursed one air",unit[1]-1,unit[2],False,Human,10])
                        return
    if resourses[4][5]>=10:
        if not IC:
            for unit in units:
                if unit[0]=="king" and unit[4]==Monster:
                    if guyCheck([unit[1],unit[2]+1],units)==False and MAP[unit[1]][unit[2]+1] not in [water,ocean]:
                        units.append(["blessed one",unit[1],unit[2]+1,False,Monster,15])
                        return
                    elif guyCheck([unit[1],unit[2]-1],units)==False and MAP[unit[1]][unit[2]-1] not in [water,ocean]:
                        units.append(["blessed one",unit[1],unit[2]-1,False,Monster,15])
                        return
                    elif guyCheck([unit[1]+1,unit[2]],units)==False and MAP[unit[1]+1][unit[2]] not in [water,ocean]:
                        units.append(["blessed one",unit[1]+1,unit[2],False,Monster,15])
                        return
                    elif guyCheck([unit[1-1],unit[2]],units)==False and MAP[unit[1]-1][unit[2]] not in [water,ocean]:
                        units.append(["blessed one",unit[1]-1,unit[2],False,Monster,15])
                        return
        elif not X:
            for unit in units:
                if unit[0]=="king" and unit[4]==Monster:
                    if guyCheck([unit[1],unit[2]+1],units)==False and MAP[unit[1]][unit[2]+1] not in [water,ocean]:
                        units.append(["cursed one air",unit[1],unit[2]+1,False,Monster,10])
                        return
                    elif guyCheck([unit[1],unit[2]-1],units)==False and MAP[unit[1]][unit[2]-1] not in [water,ocean]:
                        units.append(["cursed one air",unit[1],unit[2]-1,False,Monster,10])
                        return
                    elif guyCheck([unit[1]+1,unit[2]],units)==False and MAP[unit[1]+1][unit[2]] not in [water,ocean]:
                        units.append(["cursed one air",unit[1]+1,unit[2],False,Monster,10])
                        return
                    elif guyCheck([unit[1-1],unit[2]],units)==False and MAP[unit[1]-1][unit[2]] not in [water,ocean]:
                        units.append(["cursed one air",unit[1]-1,unit[2],False,Monster,10])
                        return
def testForPort(loc,buildings):
    for build in buildings:
        if build[0]=="port" and [build[1],build[2]]==loc:
            return True
    return False
def waterMovement(MAP,unit,resourses,p1MAP,buildings,targets=[]):
    if unit[1]>39 or unit[1]<5 or unit[2]>39 or unit[2]<5 or (not p1MAP[unit[1]][unit[2]]):
        return []
    elif not [unit[1],unit[2]] in targets:
        targets.append([unit[1],unit[2]])
    if not unit[0]=="hi":
        speed=3
    if unit[0]=="hi":
        speed=unit[3]
    for a in range(3):
        for b in range(3):
            if guyCheck([unit[1]+a*round(2*(.5-b)),unit[2]+(1-a)*round(2*(.5-b))],units) not in [unit[4],False]:
                speed=0
            if p1MAP[unit[1]+(1-b)][unit[2]+(1-a)] and not [[unit[1]+(1-b)],[unit[2]+(1-a)]] in targets:
                if MAP[unit[1]+(1-b)][unit[2]+(1-a)]==water and speed>=1:
                    test=deepcopy(unit)
                    waterMovement(MAP,["hi",test[1]+1-b,test[2]+1-a,speed-1,test[4]],resourses,p1MAP,buildings,targets)
                elif MAP[unit[1]+(1-b)][unit[2]+(1-a)]==ocean and speed>=2:
                    test=deepcopy(unit)
                    waterMovement(MAP,["hi",test[1]+1-b,test[2]+1-a,speed-2,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+(1-b)][unit[2]+(1-a)]==mountain and speed>=3:
                    test=deepcopy(unit)
                    landMovement(MAP,["hi",test[1]+1-b,test[2]+1-a,speed-5,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+(1-b)][unit[2]+(1-a)]==forest and speed>=3:
                    test=deepcopy(unit)
                    landMovement(MAP,["hi",test[1]+1-b,test[2]+1-a,speed-5,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+(1-b)][unit[2]+(1-a)]==grass and speed>=3:
                    test=deepcopy(unit)
                    landMovement(MAP,["hi",test[1]+1-b,test[2]+1-a,speed-3,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+(1-b)][unit[2]+(1-a)]==sand and speed>=2:
                    test=deepcopy(unit)
                    landMovement(MAP,["hi",test[1]+1-b,test[2]+1-a,speed-2,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+(1-b)][unit[2]+(1-a)]==rock and speed>=3:
                    test=deepcopy(unit)
                    landMovement(MAP,["hi",test[1]+1-b,test[2]+1-a,speed-4,test[4]],resourses,p1MAP,buildings,targets)
    s1=len(targets)
    s2=0
    while not s1==s2:
            for t in targets:
                    while t in targets:
                        targets.remove(t)
                    targets.append(t)
            s2=s1
            s1=len(targets)
    return targets
def landMovement(MAP,unit,resourses,p1MAP,buildings,targets=[]):
    if unit[0]=="cursed one ground":
        return []
    if unit[1]>39 or unit[1]<5 or unit[2]>39 or unit[2]<5 or (not p1MAP[unit[1]][unit[2]]):
        return []
    elif not [unit[1],unit[2]] in targets:
        targets.append([unit[1],unit[2]])
    if unit[0]=="worker" or unit[0]=="builder":
        speed=6
    if unit[0]=="general" or unit[0]=="govenor" or unit[0]=="blessed one":
        speed=6
    if unit[0]=="swordman" or unit[0]=="king" or unit[0]=="ice wizard":
        speed=4
    if unit[0]=="red":
        speed=2
    if unit[0]=="archer":
        speed=6
    if unit[0]=="runner" or unit[0]=="fairy" or unit[0]=="cursed one air":
        speed=7
    if unit[0]=="hi":
        speed=unit[3]
    if unit[0]=="green":
        speed=5
    for a in range(2):
        for b in range(2):
            if guyCheck([unit[1]+a*round(2*(.5-b)),unit[2]+(1-a)*round(2*(.5-b))],units) not in [unit[4],False]:
                speed=0
            if p1MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))] and not [[unit[1]+a*round(2*(.5-b))],[unit[2]+(1-a)*round(2*(.5-b))]] in targets:
                if MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))]==water and ((unit[0] in ["worker","builder"] and resourses[0]>=6)or(testForPort([unit[1]+a*round(2*(.5-b)),unit[2]+(1-a)*round(2*(.5-b))],buildings))):
                    if not(unit[1]+a*round(2*(.5-b))>39 or unit[1]+a*round(2*(.5-b))<5 or unit[2]+(1-a)*round(2*(.5-b))>39 or unit[2]+(1-a)*round(2*(.5-b))<5):
                        targets.append([unit[1]+a*round(2*(.5-b)),unit[2]+(1-a)*round(2*(.5-b))])
                elif MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))]==mountain and speed>=4:
                    test=deepcopy(unit)
                    test[1]=test[1]+a*round(2*(.5-b))
                    test[2]=test[2]+(1-a)*round(2*(.5-b))
                    landMovement(MAP,["hi",test[1],test[2],speed-4,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))]==forest and speed>=3:
                    test=deepcopy(unit)
                    test[1]=test[1]+a*round(2*(.5-b))
                    test[2]=test[2]+(1-a)*round(2*(.5-b))
                    landMovement(MAP,["hi",test[1],test[2],speed-3,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))]==grass and speed>=2:
                    test=deepcopy(unit)
                    test[1]=test[1]+a*round(2*(.5-b))
                    test[2]=test[2]+(1-a)*round(2*(.5-b))
                    landMovement(MAP,["hi",test[1],test[2],speed-2,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))]==sand and speed>=1:
                    test=deepcopy(unit)
                    test[1]=test[1]+a*round(2*(.5-b))
                    test[2]=test[2]+(1-a)*round(2*(.5-b))
                    landMovement(MAP,["hi",test[1],test[2],speed-1,test[4]],resourses,p1MAP,buildings,targets)

                elif MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))]==rock and speed>=3:
                    test=deepcopy(unit)
                    test[1]=test[1]+a*round(2*(.5-b))
                    test[2]=test[2]+(1-a)*round(2*(.5-b))
                    landMovement(MAP,["hi",test[1],test[2],speed-3,test[4]],resourses,p1MAP,buildings,targets)
    s1=len(targets)
    s2=0
    while not s1==s2:
            for t in targets:
                    while t in targets:
                        targets.remove(t)
                    targets.append(t)
            s2=s1
            s1=len(targets)
    return targets
def airMovement(MAP,unit,resourses,p1MAP,buildings,targets=[]):
    if unit[1]>39 or unit[1]<5 or unit[2]>39 or unit[2]<5 or (not p1MAP[unit[1]][unit[2]]):
        return []
    elif not [unit[1],unit[2]] in targets:
        targets.append([unit[1],unit[2]])
    if not unit[0]=="hi":
        speed=3
    if unit[0]=="hi":
        speed=unit[3]
    for a in range(2):
        for b in range(2):
            if p1MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))] and not [[unit[1]+a*round(2*(.5-b))],[unit[2]+(1-a)*round(2*(.5-b))]] in targets:
                if speed>=1:
                    test=deepcopy(unit)
                    test[1]=test[1]+a*round(2*(.5-b))
                    test[2]=test[2]+(1-a)*round(2*(.5-b))
                    airMovement(MAP,["hi",test[1],test[2],speed-1],resourses,p1MAP,buildings,targets)
    s1=len(targets)
    s2=0
    while not s1==s2:
            for t in targets:
                    while t in targets:
                        targets.remove(t)
                    targets.append(t)
            s2=s1
            s1=len(targets)
    return targets
def rangeAT(P1MAP,unit):
    targets=[]
    d3=[-3,-2,-1,0,1,2,3]
    for U in units:
        if U[4]!=unit[4] and not U[0] in ["jet","bomber"] and unit[1]-U[1] in d3 and unit[2]-U[2] in d3 and P1MAP[U1][U2]==True:
            targets.append([U1,U2])
    return targets
def guyCheck(loc,guys):
    for guy in guys:
        if loc==[guy[1],guy[2]]:
            for n in guy:
                if n=="p1":
                    return "p1"
                if n=="p2":
                    return "p2"
                if n=="p3":
                        return "p3"
                if n=="p4":
                        return "p4"
                if n=="p5":
                    return "p5"
    return False
def takeTurn(res,player,p1MAP,MAP,buildings,units,T=False):
    H=pygame.Surface.get_height(windowSurface)
    W=pygame.Surface.get_width(windowSurface)
    C=(W-H)/2
    width, Height = wx.GetDisplaySize()

    Coef=round(1/45*Height)
    Add1=round(Coef*7/20)
    Add2=Coef-Add1
    p1=player[0]
    if not T:
        pygame.display.set_caption('wood-'+str(res[0])+' stone-'+str(res[1])+' food-'+str(res[2])+' metal-'+str(res[3])+' gold-'+str(res[4])+' pop-'+str(res[5]))
    else:
        if res[0]<5 and MAP[units[0][1]][units[0][2]]==forest:
            pygame.display.set_caption('click on your worker, then press 1 to cut down the tree. press enter to end your turn')
        elif res[2]==0 and MAP[units[0][1]][units[0][2]]==grass:
            pygame.display.set_caption('now see if you can build a farm. press enter to end your turn')
        elif MAP[units[0][1]][units[0][2]]==forest and res[0]==5:
            pygame.display.set_caption('build a lumber hut to collect wood')
        elif res[0]<=5:
            pygame.display.set_caption('move him to a forest tile. then press enter')
        elif res[5]==0:
            pygame.display.set_caption('now you need a house and a statue. lets see if you can build that')
        elif res[4]<3:
            pygame.display.set_caption('lets wait for for our resourses to be collected')
        elif len(units)<2:
            pygame.display.set_caption('click on your house and train a new worker')
        else:
            buildings.append(["default",5,5,p1,1])
            buildings.append(["default",5,39,p1,1])
            buildings.append(["default",39,39,p1,1])
            buildings.append(["default",39,5,p1,1])
            pygame.display.set_caption('Those are the basics. Press enter to return to the menu. Have fun')
        




            
    drawMAP(MAP,p1MAP)
    for unit in units:
        if unit[4]==turn:
            for n in range(3):
                for m in range(3):
                        p1MAP[unit[1]+n-1][unit[2]+m-1]=True
                                    
    unitFound=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYUP and event.key==K_RETURN:
            for unit in units:
                unit[3]=True
            return 1
        if event.type==pygame.MOUSEBUTTONUP:
            drawMAP(MAP,p1MAP)
            pos=pygame.mouse.get_pos()
            pos=[round((pos[0]-C)/Coef-.5),round(pos[1]/Coef-.5)]
            for unit in units:
                markers=[]
                if [unit[1],unit[2]]==pos and p1MAP[unit[1]][unit[2]] and unit[4]==p1 and unit[3]:
                    unitFound=True
                    pygame.display.set_caption(unitInfo(unit,res,MAP))
                    drawMAP(MAP,p1MAP)


                    if type(unit[0])==list:
                        markers=waterMovement(MAP,unit,res,p1MAP,buildings,targets=[])+rangeAT(p1MAP,unit)
                    elif unit[0]=="archer":
                        markers=landMovement(MAP,unit,res,p1MAP,buildings,targets=[])+rangeAT(p1MAP,unit)

                    elif unit[0] in ["jet", "bomber"]:
                        markers=airMovement(MAP,unit,res,p1MAP,buildings,targets=[])
                    else:
                        markers=landMovement(MAP,unit,res,p1MAP,buildings,targets=[])
                    for marker in markers:
                        a=marker[0]
                        b=marker[1]
                        pygame.draw.polygon(windowSurface,(0,100,0),((Coef*a+Add1+C,Coef*b+Add1),(Coef*a+Add1+C,Coef*b+Add2),(Coef*a+Add2+C,Coef*b+Add2),(Coef*a+Add2+C,Coef*b+Add1)))
                    x=True
                    pygame.display.update()
                    while x and unit[3]:
                        for event in pygame.event.get():
                            if event.type==pygame.KEYUP and guyCheck(pos,buildings)==False and type(unit[0])==list and unit[0][1][0] in ["worker","builder"]:
                                if event.key == pygame.K_1 and MAP[unit[1]][unit[2]]==water and res[0]>=6:
                                    res[0]-=6
                                    buildings.append(["port",pos[0],pos[1],p1,8])
                                    unit[3]=False
                                if event.key == pygame.K_1 and MAP[unit[1]][unit[2]]==ocean and res[0]>=5:
                                    res[0]-=5
                                    buildings.append(["fishing spot",pos[0],pos[1],p1,6])
                                    unit[3]=False
                            if event.type==pygame.KEYUP and guyCheck(pos,buildings)==False and unit[0]=="builder":
                                if event.key == pygame.K_a and res[3]>=5:
                                    buildings.append(["armory",unit[1],unit[2],p1,10])
                                    res[3]-=5
                                    unit[3]=False
                                if event.key == pygame.K_s and res[3]>=5:
                                    buildings.append(["artillary",unit[1],unit[2],p1,10])
                                    res[3]-=5
                                    unit[3]=False
                                if event.key == pygame.K_d and DWARF() and res[5]>=10:
                                    buildings.append(["red barracks",unit[1],unit[2],p1,6])
                                    unit[3]=False
                            if event.type==pygame.KEYUP and guyCheck(pos,buildings)==False and unit[0]=="worker":
                                if event.key == pygame.K_a and res[3]>=10:
                                    buildings.append(["armory",unit[1],unit[2],p1,10])
                                    res[3]-=10
                                    unit[3]=False
                                if event.key == pygame.K_s and res[3]>=10:
                                    buildings.append(["artillary",unit[1],unit[2],p1,10])
                                    res[3]-=10
                                    unit[3]=False
                                if event.key == pygame.K_d and DWARF() and res[5]>=10:
                                    buildings.append(["red barracks",unit[1],unit[2],p1,6])
                                    unit[3]=False                            
                            if event.type==pygame.KEYUP and guyCheck(pos,buildings)==False and unit[0] in ["worker","builder"]:
                                if event.key == pygame.K_1 and MAP[unit[1]][unit[2]]==grass and res[2]>=1:
                                    buildings.append(["farm",unit[1],unit[2],p1,6])
                                    res[2]-=1
                                    unit[3]=False
                                if event.key == pygame.K_3 and (MAP[unit[1]][unit[2]]==mountain or MAP[unit[1]][unit[2]]==rock) and res[0]>=8:
                                    buildings.append(["wood mine",unit[1],unit[2],p1,8])
                                    unit[3]=False
                                    res[0]-=8
                                if event.key == pygame.K_4 and (MAP[unit[1]][unit[2]]==mountain or MAP[unit[1]][unit[2]]==rock) and res[1]>=20:
                                    buildings.append(["stone mine",unit[1],unit[2],p1,10])
                                    unit[3]=False
                                    res[1]-=20
                                if event.key == pygame.K_2 and MAP[unit[1]][unit[2]]==forest and res[0]>=5:
                                    buildings.append(["lumber hut",unit[1],unit[2],p1,6])
                                    unit[3]=False
                                    res[0]-=5
                                if event.key==pygame.K_5 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock and res[0]>=5 and res[2]>=3:
                                    buildings.append(["house",unit[1],unit[2],p1,6,1])
                                    unit[3]=False
                                    res[0]-=5
                                    res[2]-=3
                                if event.key==pygame.K_6 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock and res[1]>=15 and res[2]>=5:
                                    buildings.append(["house",unit[1],unit[2],p1,8,2])
                                    unit[3]=False
                                    res[1]-=15
                                    res[2]-=5
                                if event.key==pygame.K_7 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and res[3]>=10:
                                    buildings.append(["barracks",unit[1],unit[2],p1,10,3])
                                    unit[3]=False
                                    res[3]-=10
                                if event.key==pygame.K_8 and not MAP[unit[1]][unit[2]]==water and res[3]>=12:
                                    buildings.append(["airport",unit[1],unit[2],p1,15])
                                    unit[3]=False
                                    res[3]-=12
                                if event.key==pygame.K_q and res[0]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                                    buildings.append(["wood statue",unit[1],unit[2],p1,10])
                                    unit[3]=False
                                    res[0]-=10
                                if event.key==pygame.K_w and res[1]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                                    buildings.append(["stone statue",unit[1],unit[2],p1,15])
                                    unit[3]=False
                                    res[1]-=10
                                if event.key==pygame.K_e and res[3]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                                    buildings.append(["metal statue",unit[1],unit[2],p1,20])
                                    unit[3]=False
                                    res[3]-=10
                                if event.key==pygame.K_r and res[3]>=10 and res[4]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                                    buildings.append(["gold statue",unit[1],unit[2],p1,5])
                                    unit[3]=False
                                    res[3]-=10
                                    res[4]-=10
                            if event.type==pygame.KEYUP and unit[0]=="bomber":
                                if event.key == pygame.K_1:
                                    for a in range(3):
                                        for b in range(3):
                                            for building in buildings:
                                                if [pos[0]+1-a,pos[1]+1-b]==[building[1],building[2]]:
                                                    building[4]=0
                                            for un in units:
                                                if [pos[0]+1-a,pos[1]+1-b]==[un[1],un[2]] and not(un[0]=="jet" or un[0]=="bomber"):
                                                    un[5]-=5
                                    unit[3]=False
                            if event.type==pygame.KEYUP and unit[0]=="fairy":
                                if event.key == pygame.K_1:

                                    if BuildOwn([unit[1],unit[2]],units,p1):
                                        unit[0]="fairyx"
                                        unit[3]=False
                                        for unitx in units:
                                            if unitx[0] in ["fairy","ice wizard"] or (type(unitx[0])==list and unitx[0][1][0] in ["fairy","ice wizard"]):
                                                if type(unitx[0])==list:
                                                        unitx[0][1][0]=="fairy"
                                                else:
                                                        unitx[0]="fairy"
                                                unitx[3]=False
                                        unit[0]="ice wizard"
                            if event.type==pygame.KEYUP and unit[0]=="cursed one ground":
                                if event.key == pygame.K_1:
                                    unit[0]="cursed one air"
                                    unit[3]=False
                                    continue
                            if event.type==pygame.KEYUP and unit[0]=="cursed one air":
                                if event.key == pygame.K_1:
                                    if BuildOwn([unit[1],unit[2]],units,p1):
                                        unit[0]="cursed one ground"
                                        unit[3]=False
                            if event.type==pygame.MOUSEBUTTONUP:
                                pos=pygame.mouse.get_pos()
                                pos=[round((pos[0]-C)/Coef-.5),round(pos[1]/Coef-.5)]
                                x=False
                                for marker in markers:
                                    if [marker[0],marker[1]]==pos and unit[3]:
                                        unitFound==True
                                        if guyCheck(pos,units)==False and (not (MAP[marker[0]][marker[1]]==water or MAP[marker[0]][marker[1]]==ocean) or unit[0]=="jet" or unit[0]=="bomber") and (guyCheck(pos,buildings)==False or guyCheck(pos,buildings)==p1):
                                            if unit[0]=="runner":
                                                unit[0]="green"
                                            elif unit[0]=="swordman":
                                                unit[0]="red"
                                            else:
                                                unit[3]=False
                                            unit[1],unit[2]=pos[0],pos[1]
                                            if type(unit[0])==list:
                                                if len(unit[0][1])==7:
                                                    unit.append(unit[0][1][6])
                                                if len(unit[0][1])==9:
                                                        unit.append(" ")
                                                        unit.append([None,0])
                                                        unit.append([None,0])
                                                unit[0]=unit[0][1][0]
                                                
                                        elif testForPort(pos,buildings) and guyCheck(pos,units)==False and not type(unit[0])==list and not unit[0]=="jet" and not unit[0]=="bomber":
                                            if unit in units:
                                                units.remove(unit)
                                                units.append([["ship",unit],pos[0],pos[1],False,unit[4],unit[5]])
                                                unit[3]==False
                                        elif unit[0]=="worker" or unit[0]=="builder" and guyCheck(pos,units)==False:
                                            if MAP[marker[0]][marker[1]]==water and res[0]>=6:
                                                buildings.append(["port",pos[0],pos[1],p1,8])
                                                res[0]-=6
                                                unit[3]=False
                                        elif type(unit[0])==list and guyCheck(pos,units)==False and (MAP[marker[0]][marker[1]]==water or MAP[marker[0]][marker[1]]==ocean):
                                            unit[3]=False
                                            unit[1],unit[2]=pos[0],pos[1]
                                
                                        elif guyCheck(pos,units)!=False and guyCheck(pos,units)!=p1 and (unit[0]=="jet" or unit[0]=="archer" or (type(unit[0])==list and len(unit[0][1])==7)):
                                            for un in units:
                                                if [un[1],un[2]]==pos:
                                                    if unit[0]=="archer" and not (un[0]=="jet" or un[0]=="bomber"):
                                                        
                                                        un[5]-=damageCalc(unit,un,units,buildings)

                                                        unit[3]=False
                                        
                                                    elif unit[0]=="jet" and (un[0]=="jet" or un[0]=="bomber"):
                                                        un[5]-=12
                                                        unit[3]=False
                                                        
                                                    elif type(unit[0])==list and not (un[0]=="jet" or un[0]=="bomber"):
                                                        un[5]-=unit[0][1][6]*2
                                                        unit[3]=False
                                        elif unit[0]=="green" or unit[0]=="runner" or unit[0]=="swordman" or unit[0]=="red":
                                            for a in range(2):
                                                for b in range(2):
                                                    if pos[0]==unit[1]+a*round(2*(.5-b)) and pos[1]==unit[2]+(1-a)*round(2*(.5-b)):
                                                        for un in units:
                                                            if [un[1],un[2]]==pos and not (un[0]=="jet" or un[0]=="bomber") and un[4]!=p1:
                                                                un[5]-=damageCalc(unit,un,units,buildings)

                                                                unit[3]=False                                

                elif[unit[1],unit[2]]==pos and p1MAP[unit[1]][unit[2]]:
                        unitFound=True
                        x=True
                        pygame.display.set_caption("health-"+str(unit[5]))
                        drawMAP(MAP,p1MAP)
                        while x:
                            for event in pygame.event.get():
                                if event.type==pygame.MOUSEBUTTONUP:
                                    pos=pygame.mouse.get_pos()
                                    pos=[round((pos[0]-C)/Coef-.5),round(pos[1]/Coef-.5)]
                                    x=False
            if not unitFound:
                    for unit in buildings:
                        x=True
                        if [unit[1],unit[2]]==pos and p1MAP[unit[1]][unit[2]] and not BuildOwn(pos,units,p1):
                                pygame.display.set_caption("health-"+str(unit[4]))
                                drawMAP(MAP,p1MAP)
                                while x:
                                        for event in pygame.event.get():
                                            if event.type==pygame.MOUSEBUTTONUP:
                                                pos=pygame.mouse.get_pos()
                                                pos=[round((pos[0]-C)/Coef-.5),round(pos[1]/Coef-.5)]
                                                x=False
                        if [unit[1],unit[2]]==pos and p1MAP[unit[1]][unit[2]] and BuildOwn(pos,units,p1):
                            pygame.display.set_caption(buildInfo(unit,res,p1))
                            drawMAP(MAP,p1MAP)
                            if (unit[0]=="artillary"):
                                M=rangeAT(p1MAP,unit)
                                while x:
                                    for event in pygame.event.get():
                                        if event.type==pygame.MOUSEBUTTONUP:
                                            pos=pygame.mouse.get_pos()
                                            pos=[round((pos[0]-C)/Coef-.5),round(pos[1]/Coef-.5)]
                                            x=False
                                            for un in units:
                                                if [un[1],un[2]]==pos:
                                                    if not (un[0]=="jet" or un[0]=="bomber"):
                                                        if p1==Dwarf:
                                                            un[5]-=1.5*damageCalc(["archer",unit[1],unit[2],True,p1,1,2],un,units,buildings)
                                                        else:
                                                            un[5]-=damageCalc(["archer",unit[1],unit[2],True,p1,1,2],un,units,buildings)

                            else:
                                while x:
                                    for event in pygame.event.get():
                                        

                                        if event.type==pygame.MOUSEBUTTONUP:
                                            pos=pygame.mouse.get_pos()
                                            pos=[round((pos[0]-C)/Coef-.5),round(pos[1]/Coef-.5)]
                                            x=False
                                        if event.type==pygame.KEYUP and (unit[0]=="house" or unit[0]=="barracks"):
                                            if unit[5]==1:
                                                re=0
                                            if unit[5]==2:
                                                re=1
                                            if unit[5]==3:
                                                re=3
                                            if event.key == pygame.K_1 and res[5]>=1 and res[4]>=3:
                                                res[5]-=1
                                                res[4]-=3
                                                if p1==Dwarf:
                                                    units.append(["builder",pos[0],pos[1],False,p1,5])
                                                else:
                                                    units.append(["worker",pos[0],pos[1],False,p1,5])
                                                x=False                                      
                                            if event.key == pygame.K_2 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                                res[5]-=unit[5]+1
                                                res[4]-=6+2*re
                                                res[re]-=5
                                                HP=round(8*(unit[5]))
                                                if p1==Orc:
                                                    HP*=1.2
                                                units.append(["swordman",pos[0],pos[1],False,p1,round(HP),unit[5]])
                                                x=False
                                            if event.key == pygame.K_3 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                                res[5]-=unit[5]+1
                                                res[4]-=6+2*re
                                                res[re]-=5
                                                HP=round(12*(unit[5]))
                                                if p1==Orc:
                                                    HP*=1.2
                                                units.append(["runner",pos[0],pos[1],False,p1,round(HP),unit[5]])
                                                x=False
                                            if event.key == pygame.K_4 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                                res[5]-=unit[5]+1
                                                res[4]-=6+2*re
                                                res[re]-=5
                                                HP=round(6*(unit[5]))
                                                if p1==Orc:
                                                    HP*=1.2
                                                units.append(["archer",pos[0],pos[1],False,p1,round(HP),unit[5]])
                                                x=False
                                            if event.key == pygame.K_5 and res[5]>=3 and res[4]>=10:
                                                res[5]-=3
                                                res[4]-=10
                                                units.append(["govenor",pos[0],pos[1],False,p1,10])
                                                x=False 
                                        if event.type==pygame.KEYUP and (unit[0]=="red barracks"):                                    
                                            if event.key == pygame.K_2:
                                                unit[4]-=1
                                                HP=8*3.5
                                                if p1==Orc or p1==Monster:
                                                    HP*=1.2
                                                units.append(["swordman",pos[0],pos[1],False,p1,round(HP),unit[5]])
                                                x=False
                                            if event.key == pygame.K_3:
                                                unit[4]-=1
                                                HP=12*3.5
                                                if p1==Orc or p1==Monster:
                                                    HP*=1.2
                                                units.append(["runner",pos[0],pos[1],False,p1,round(HP),unit[5]])
                                                x=False
                                            if event.key == pygame.K_4:
                                                HP=6*3.5
                                                if p1==Orc or p1==Monster:
                                                    HP*=1.2
                                                units.append(["archer",pos[0],pos[1],False,p1,round(HP),unit[5]])
                                                x=False
                                        if event.type==pygame.KEYUP and (unit[0]=="airport"):

                                            if event.key == pygame.K_1 and res[5]>=5 and res[4]>=10 and res[3]>=10:
                                                res[5]-=5
                                                res[4]-=10
                                                res[3]-=10
                                                units.append(["bomber",pos[0],pos[1],False,p1,12])
                                                x=False
                                            if event.key == pygame.K_2 and res[5]>=5 and res[4]>=10 and res[3]>=10:
                                                res[5]-=5
                                                res[4]-=10
                                                res[3]-=10
                                                units.append(["jet",pos[0],pos[1],False,p1,20])
                                                x=False
                                    

    for building in buildings:
        if building[4]<=0:
            buildings.remove(building)
    for unit in units:
        if unit[5]<=0:
            units.remove(unit)
def sig(x):
    return (2/(1+math.exp(-3*x)))-1

def SCORE(pos,relations):
    return 0

def AI(res,player,p1MAP,MAP,buildings,units,relations,needs,ST):
    return [res,MAP,buildings,units]

j=0
while True:
    H=pygame.Surface.get_height(windowSurface)
    W=pygame.Surface.get_width(windowSurface)
    C=(W-H)/2
    p1S=0
    p2S=0
    p3S=0
    p4S=0
    corner=[5,39]
    for building in buildings:
         if building[1] in corner and building[2] in corner:
                 if building[3]=="p1":
                         p1S+=1
                 if building[3]=="p2":
                         p2S+=1
                 if building[3]=="p3":
                         p3S+=1
                 if building[3]=="p4":
                         p4S+=1
    if p1S==4 or p2S==4 or p3S==4 or p4S==4:
        pygame.display.set_caption('conquestia')
        units=Hstart+Estart+Dstart+Ostart
        buildings=[]
        resourses=[[10,0,2,0,0,0],[10,0,2,0,0,0],[10,0,2,0,0,0],[10,0,2,0,0,0]]
        turn="p1"
        inAGame=False
        MAP=[]
        p1MAP=[]
        p2MAP=[]
        p3MAP=[]
        p4MAP=[]
        genWorld(MAP,p1MAP,p2MAP,p3MAP,p4MAP)
    if not inAGame:
        windowSurface.fill((255,255,255))
        text("Conquestia",(0,0,0),Height/2+C,Height/6,round(1/9*Height))
        text("4 PLAYERS",(0,255,0),Height/2+C,5/8*Height,round(4/45*Height))
        text("2 PLAYERS",(0,255,0),Height/2+C,6/8*Height,round(4/45*Height))
        text("1 PLAYER",(0,255,0),Height/2+C,4/8*Height,round(4/45*Height))
        text("tutorial",(0,255,0),Height/2+C,3/8*Height,round(4/45*Height))
        text("custom",(0,255,0),Height/2+C,7/8*Height,round(4/45*Height))

        
        pygame.display.update()
        pos=[0,0]
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
        relationsP1=[[0,0,0,0,0,0],[0,0,0,0]]
        relationsP2=[[0,0,0,0,0,0],[0,0,0,0]]
        relationsP3=[[0,0,0,0,0,0],[0,0,0,0]]
        relationsP4=[[0,0,0,0,0,0],[0,0,0,0]]
        needsp1=[None,None,None,None]
        needsp2=[None,None,None,None]
        needsp3=[None,None,None,None]
        needsp4=[None,None,None,None]

        S=True
        if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>9/16*Height and pos[1]<11/16*Height:
            inAGame=True
            P=4
            players=[1,1,1,1]
        if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>11/16*Height and pos[1]<13/16*Height:
            inAGame=True
            P=2
            players=[1,1,0,0]
            #units=[["worker",7,37,True,"p1",5],["worker",37,7,True,"p2",5]]
        if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>5/16*Height and pos[1]<7/16*Height:
            inAGame=True
            P=0
            players=[1,0,0,0]
            #units=[["worker",7,37,True,"p1",5]]
        if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>7/16*Height and pos[1]<9/16*Height:
            players=[1,-1,-1,-1]
            inAGame=True
            P=1
        if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>13/16*Height and pos[1]<15/16*Height:
            P=0
            turnx="p1"
            players=[]
            inAGame=True
            for n in range(4):
                while True:
                    pos=[0,0]
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONUP:
                            pos=pygame.mouse.get_pos()
                    windowSurface.fill((255,255,255))
                    text("PLAYER-"+turnx[1],(0,0,0),Height/2+C,1/9*Height,round(4/45*Height))
                    text("AI",(0,255,0),Height/2+C,5/8*Height,round(4/45*Height))
                    text("PLAYER",(0,255,0),Height/2+C,6/8*Height,round(4/45*Height))
                    text("NONE",(0,255,0),Height/2+C,4/8*Height,round(4/45*Height))
                    pygame.display.update()
                    if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>9/16*Height and pos[1]<11/16*Height:
                        players.append(-1)
                        P+=1
                        turnx="p"+str((int(turnx[1])+1))

                        break

                    if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>11/16*Height and pos[1]<13/16*Height:
                        inAGame=True
                        P+=1
                        players.append(1)
                        turnx="p"+str((int(turnx[1])+1))

                        break

                    if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>7/16*Height and pos[1]<9/16*Height:
                        players.append(0)
                        P+=1
                        #units.remove(units[P])
                        turnx="p"+str((int(turnx[1])+1))

                        break
    else:
        if not 1 in players:
            drawMAP(MAP,pMAP)
        T=int(turn[1])-1
        M=[p1MAP,p2MAP,p3MAP,p4MAP]
        R=[relationsP1,relationsP2,relationsP3,relationsP4]
        N=[needsp1,needsp2,needsp3,needsp4]        
        if players[T]==1:
            F=takeTurn(resourses[T],[turn],M[T],MAP,buildings,units)
        #elif players[T]==-1:
        #    F=AI(resourses[T],[turn],M[T],MAP,buildings,units,R[T],N[2],ST)
        #    ST=False
        elif players[T]==0:
            F=1
        if not F==1 and not F==None:
            [resourses[int(turn[1])-1],MAP,buildings,units]=F
        #if players[T]==-1 and (F==1 or F==None):
        #    j+=1
        if F==1:
            ST=True
            for unit in units:
                unit[3]=True
                if unit[0]=="green":
                    unit[0]="runner"
                if unit[0]=="red":
                    unit[0]="swordman"
            if not P==1 and not P==0:
                if turn=="p"+str(P):
                        turn="p1"

                else:
                    turn="p"+str((int(turn[1])+1))
            elif P==0:
                turn='p1'

            else:
                if turn=='p4':
                    turn="p1"
                else:
                    turn="p"+str((int(turn[1])+1))
            x=False
            T=int(turn[1])-1
            windowSurface.fill((255,255,255))
            if players[T]==1:
                
                pygame.display.set_caption("next turn")
                if turn=="p1":
                        X=P1
                if turn=="p2":
                        X=P2
                if turn=="p3":
                        X=P3
                if turn=="p4":
                        X=P4
                text("PLAYER-"+turn[1]+"'S TURN",X,Height/2+C,1/9*Height,round(4/45*Height))

            pygame.display.update()
            housing=0
            culture=0
            H=False
            E=False
            D=False
            O=False
            for unit in units:
                if unit[0]=="king":
                    if unit[4]==Human:
                        H=True
                    if unit[4]==Elf:
                        E=True
                    if unit[4]==Dwarf:
                        D=True
                    if unit[4]==Orc:
                        O=True
            if not H:
                players[0]=0
            if not E:
                players[1]=0
            if not D:
                players[2]=0
            if not O:
                players[3]=0
            for building in buildings:
                if turn=="p1" and BuildOwn([building[1],building[2]],units,"p1"):
                    HUMAN()
                    if building[0]=="farm":
                        resourses[0][2]+=2
                    if building[0]=="lumber hut":
                        resourses[0][0]+=3
                    if building[0]=="wood mine":
                        resourses[0][1]+=1
                    if building[0]=="stone mine":
                        resourses[0][1]+=2
                        resourses[0][3]+=1
                    if building[0]=="house":
                        housing+=3*building[5]
                    if building[0]=="fishing spot":
                        resourses[0][2]+=5
                    if building[0]=="wood statue":
                        culture+=1
                    if building[0]=="stone statue":
                        culture+=3
                    if building[0]=="metal statue":
                        culture+=6
                    if building[0]=="gold statue":
                        culture+=10
                elif turn=="p2" and BuildOwn([building[1],building[2]],units,"p2"):
                    ELF()
                    if building[0]=="farm":
                        resourses[1][2]+=2
                    if building[0]=="lumber hut":
                        resourses[1][0]+=3
                    if building[0]=="wood mine":
                        resourses[1][1]+=1
                    if building[0]=="stone mine":
                        resourses[1][1]+=2
                        resourses[1][3]+=1
                    if building[0]=="house":
                        housing+=3*building[5]
                    if building[0]=="fishing spot":
                        resourses[1][2]+=5
                    if building[0]=="wood statue":
                        culture+=1
                    if building[0]=="stone statue":
                        culture+=3
                    if building[0]=="metal statue":
                        culture+=6
                    if building[0]=="gold statue":
                        culture+=10
                elif turn=="p3" and BuildOwn([building[1],building[2]],units,"p3"):
                    DWARF()
                    if building[0]=="farm":
                        resourses[2][2]+=2
                    if building[0]=="lumber hut":
                        resourses[2][0]+=3
                    if building[0]=="wood mine":
                        resourses[2][1]+=1
                    if building[0]=="stone mine":
                        resourses[2][1]+=2
                        resourses[2][3]+=1
                    if building[0]=="house":
                        housing+=3*building[5]
                    if building[0]=="fishing spot":
                        resourses[2][2]+=5
                    if building[0]=="wood statue":
                        culture+=1
                    if building[0]=="stone statue":
                        culture+=3
                    if building[0]=="metal statue":
                        culture+=6
                    if building[0]=="gold statue":
                        culture+=10
                    
                elif turn=="p4" and BuildOwn([building[1],building[2]],units,"p4"):
                    if building[0]=="farm":
                        resourses[3][2]+=2
                    if building[0]=="lumber hut":
                        resourses[3][0]+=3
                    if building[0]=="wood mine":
                        resourses[3][1]+=1
                    if building[0]=="stone mine":
                        resourses[3][1]+=2
                        resourses[3][3]+=1
                    if building[0]=="house":
                        housing+=3*building[5]
                    if building[0]=="fishing spot":
                        resourses[3][2]+=5
                    if building[0]=="wood statue":
                        culture+=1
                    if building[0]=="stone statue":
                        culture+=3
                    if building[0]=="metal statue":
                        culture+=6
                    if building[0]=="gold statue":
                        culture+=10

            if turn=="p3":
                S=0
                for r in resourses[2]:
                    S+=r
                if S>=25:
                    i=0
                    for r in resourses[2]:
                        r=round(r-r/(S**.5))

                        if r>=10:
                                resourses[0][i]=r
                        i+=1
                resourses[2][5]=min(max(0,resourses[2][2]-1),housing,resourses[2][5]+culture)
                resourses[2][2]-=resourses[2][5]
                resourses[2][4]+=resourses[2][5]
            elif turn=="p4":
                S=0
                for r in resourses[3]:
                    S+=r
                if S>=25:
                    i=0
                    for r in resourses[3]:
                        r=round(r-r/(S**.5))
                        if r>=10:
                                resourses[0][i]=r
                        i+=1
                resourses[3][5]=min(max(0,resourses[3][2]-1),housing,resourses[3][5]+culture)

                resourses[3][2]-=resourses[3][5]
                resourses[3][4]+=resourses[3][5]
            elif turn=="p1":
                S=0
                for r in resourses[0]:
                    S+=r
                if S>=25:
                    i=0
                    for r in resourses[0]:
                        r=round(r-r/(S**.5))
                        if r>=10:
                                resourses[0][i]=r
                        i+=1
                resourses[0][5]=min(max(0,resourses[0][2]-1),housing,resourses[0][5]+culture)

                resourses[0][2]-=resourses[0][5]
                resourses[0][4]+=resourses[0][5]
            else:
                S=0
                for r in resourses[1]:
                    S+=r
                if S>=25:
                    i=0
                    for r in resourses[1]:
                        r=round(r-r/(S**.5))
                        if r>=10:
                                resourses[0][i]=r
                        i+=1
                resourses[1][5]=min(max(0,resourses[1][2]-1),housing,resourses[1][5]+culture)

                resourses[1][2]-=resourses[1][5]
                resourses[1][4]+=resourses[1][5]
            x=False
            while not x:
                if players[T]==-1 or players[T]==0:
                    x=True
                for event in pygame.event.get():
                    if event.type==pygame.KEYUP:
                        if event.key==K_RETURN:
                            x=True

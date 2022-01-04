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
grass=(0,255,0)
forest=(0,127,0)
error=(255,0,255)
worker=(255,127,0)
port=(0,255,255)
rock=(50,50,50)
boat=sand
farm=sand
darkRed=(127,0,0)
P1=darkRed
darkBlue=(0,0,127)
P2=darkBlue
darkGreen=(0,127,0)
P3=darkGreen
darkYellow=(127,127,0)
P4=darkYellow
wood=(127,63,0)
stone=(127,127,127)
lumber=(63,21,0)
jet=(200,200,200)
bomber=(100,100,100)
airport=error
windowSurface=pygame.display.set_mode((width,Height),FULLSCREEN)
print(pygame.Surface.get_height(windowSurface))
print(pygame.Surface.get_width(windowSurface))
#["diplomat",9,37,True,"p1",4,"",[None,0],[None,0]]
#units=[["worker",7,37,True,"p1",5],["worker",37,7,True,"p2",5],["worker",7,7,True,"p3",5],["worker",37,37,True,"p4",5],["diplomat",5,37,True,"p2",4,"",[None,0],[None,0]],["diplomat",6,37,True,"p1",4,"",[None,0],[None,0]],["diplomat",8,32,True,"p1",4,"",[None,0],[None,0]],["diplomat",9,32,True,"p3",4,"",[None,0],[None,0]]]
pygame.display.set_caption('conquestia')
units=[["worker",7,37,True,"p1",5],["worker",37,7,True,"p2",5],["worker",7,7,True,"p3",5],["worker",37,37,True,"p4",5]]
players=[1,1,1,1]
buildings=[]
resourses=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
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
            unit=building
            if unit[3]=="p1":
                pygame.draw.polygon(windowSurface,darkRed,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[3]=="p2":
                pygame.draw.polygon(windowSurface,darkBlue,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[3]=="p3":
                pygame.draw.polygon(windowSurface,darkGreen,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[3]=="p4":
                pygame.draw.polygon(windowSurface,darkYellow,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))



    for unit in units:
        if p1MAP[unit[1]][unit[2]]:
            if unit[0]=="spy" or unit[0]=="diplomat":
                pygame.draw.polygon(windowSurface,(30,30,30),((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))

            if unit[0]=="worker":
                pygame.draw.polygon(windowSurface,worker,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if type(unit[0])==list:
                pygame.draw.polygon(windowSurface,sand,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="swordman":
                pygame.draw.polygon(windowSurface,(255,0,0),((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="runner" or unit[0]=="green":
                pygame.draw.polygon(windowSurface,(0,99,0),((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="archer":
                pygame.draw.polygon(windowSurface,(0,0,255),((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="bomber":
                pygame.draw.polygon(windowSurface,bomber,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[0]=="jet":
                pygame.draw.polygon(windowSurface,jet,((Coef*unit[1]+Add5+C,Coef*unit[2]+Add5),(Coef*unit[1]+Add5+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add6),(Coef*unit[1]+Add6+C,Coef*unit[2]+Add5)))
            if unit[4]=="p1":
                pygame.draw.polygon(windowSurface,darkRed,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[4]=="p2":
                pygame.draw.polygon(windowSurface,darkBlue,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[4]=="p3":
                pygame.draw.polygon(windowSurface,darkGreen,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
            if unit[4]=="p4":
                pygame.draw.polygon(windowSurface,darkYellow,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))


            if not unit[3]:
                pygame.draw.polygon(windowSurface,mountain,((Coef*unit[1]+Add3+C,Coef*unit[2]+Add3),(Coef*unit[1]+Add3+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add4),(Coef*unit[1]+Add4+C,Coef*unit[2]+Add3)))
    if not pygame.display.get_caption()==():
        text(pygame.display.get_caption()[0],mountain,Height/2+C,Height*1/18,round(Height*1/60))
    pygame.display.update()
genWorld(MAP,p1MAP,p2MAP,p3MAP,p4MAP)

def buildInfo(unit,resourses):
    string=" "
    string="health-"+str(unit[4])
    if len(unit)>5:
        string+=" 1-worker 2-swordman 3-runner 4-archer 5-diplomat"
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
    if type(unit[0])==list and unit[0][1][0]=="worker" and MAP[unit[1]][unit[2]]==ocean and resourses[0]>=5:
            string+=" 1-build fishing spot"
    if type(unit[0])==list and unit[0][1][0]=="worker" and MAP[unit[1]][unit[2]]==water and resourses[0]>=6:
            string+=" 1-build port"
    if unit[0]=="worker":
        if MAP[unit[1]][unit[2]]==forest:
            string+=" 1-cut tree"
        if MAP[unit[1]][unit[2]]==grass:
            string+=" 2-grow farm"
        if resourses[0]>=8 and (MAP[unit[1]][unit[2]]==mountain or MAP[unit[1]][unit[2]]==rock):
            string+=" 3-build wood mine"
        if resourses[1]>=20 and (MAP[unit[1]][unit[2]]==mountain or MAP[unit[1]][unit[2]]==rock):
            string+=" 4-build stone mine"
        if resourses[0]>=5 and MAP[unit[1]][unit[2]]==forest:
            string+=" 5-build lumber hut"
        if resourses[0]>=5 and not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock:
            string+=" 6-build wood house"
        if resourses[1]>=15 and not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock:
            string+=" 7-build stone house"
        if resourses[3]>=10 and not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock:
            string+=" 8-build barracks"
        if resourses[3]>=12 and not MAP[unit[1]][unit[2]]==water:
            string+=" 9-build airport"
        if resourses[0]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
            string+=" w-build wood statue"
        if resourses[1]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
            string+=" e-build stone statue"
        if resourses[3]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
            string+=" r-build metal statue"
        if resourses[3]>=10 and resourses[4]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
            string+=" t-build gold statue"
    if unit[0]=="bomber":
        string+=" 1-drop bomb"
    if unit[0]=="diplomat":
            string+=" 1-set message 2-make trade"
            if resourses[3]>=6:
                string+=" 3-become spy"
    if len(unit)==7:
        string+=" lv-"+str(unit[6])
    if type(unit[0])==list:
        if unit[0][1][0]=="green":
            string+=" "+"runner"
        else:
                string+=" "+unit[0][1][0]
    return string
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
    if unit[1]>39 or unit[1]<5 or unit[2]>39 or unit[2]<5 or (not p1MAP[unit[1]][unit[2]]):
        return []
    elif not [unit[1],unit[2]] in targets:
        targets.append([unit[1],unit[2]])
    if unit[0]=="worker":
        speed=6
    if unit[0]=="swordman":
        speed=4
    if unit[0]=="archer":
        speed=6
    if unit[0]=="runner":
        speed=7
    if unit[0]=="hi":
        speed=unit[3]
    if unit[0]=="green":
        speed=5
    if unit[0]=="spy" or unit[0]=="diplomat":
        speed=7
    for a in range(2):
        for b in range(2):
            
            if p1MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))] and not [[unit[1]+a*round(2*(.5-b))],[unit[2]+(1-a)*round(2*(.5-b))]] in targets:
                if MAP[unit[1]+a*round(2*(.5-b))][unit[2]+(1-a)*round(2*(.5-b))]==water and ((unit[0]=="worker" and resourses[0]>=6)or(testForPort([unit[1]+a*round(2*(.5-b)),unit[2]+(1-a)*round(2*(.5-b))],buildings))):
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
    for u in units:
            if u[0]=="diplomat" and u[4]==p1:
                    if u[3]:
                            u[6]=" "
                            if not u[7][0]==None:
                                    res[u[7][0]]+=u[7][1]
                            u[7]=[None,0]
                            u[8]=[None,0]
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

                    if unit[0]=="worker" or unit[0]=="archer" or unit[0]=="swordman" or unit[0]=="runner" or unit[0]=="green" or unit[0]=="spy" or unit[0]=="diplomat":
                        markers=landMovement(MAP,unit,res,p1MAP,buildings,targets=[])
                    elif type(unit[0])==list:
                        markers=waterMovement(MAP,unit,res,p1MAP,buildings,targets=[])
                    else:
                        markers=airMovement(MAP,unit,res,p1MAP,buildings,targets=[])

                    for marker in markers:
                        a=marker[0]
                        b=marker[1]
                        pygame.draw.polygon(windowSurface,(0,100,0),((Coef*a+Add1+C,Coef*b+Add1),(Coef*a+Add1+C,Coef*b+Add2),(Coef*a+Add2+C,Coef*b+Add2),(Coef*a+Add2+C,Coef*b+Add1)))
                    x=True
                    pygame.display.update()
                    while x and unit[3]:
                        for event in pygame.event.get():
                            if event.type==pygame.KEYUP and guyCheck(pos,buildings)==False and type(unit[0])==list and unit[0][1][0]=="worker":
                                if event.key == pygame.K_1 and MAP[unit[1]][unit[2]]==water and res[0]>=6:
                                    res[0]-=6
                                    buildings.append(["port",pos[0],pos[1],p1,8])
                                    unit[3]=False
                                if event.key == pygame.K_1 and MAP[unit[1]][unit[2]]==ocean and res[0]>=5:
                                    res[0]-=5
                                    buildings.append(["fishing spot",pos[0],pos[1],p1,6])
                                    unit[3]=False
                            if event.type==pygame.KEYUP and guyCheck(pos,buildings)==False and unit[0]=="worker":
                                if event.key == pygame.K_1 and MAP[unit[1]][unit[2]]==forest:
                                    res[0]+=10
                                    MAP[unit[1]][unit[2]]=grass
                                    unit[3]=False
                                if event.key == pygame.K_2 and MAP[unit[1]][unit[2]]==grass:
                                    buildings.append(["farm",unit[1],unit[2],p1,6])
                                    unit[3]=False
                                if event.key == pygame.K_3 and (MAP[unit[1]][unit[2]]==mountain or MAP[unit[1]][unit[2]]==rock) and res[0]>=8:
                                    buildings.append(["wood mine",unit[1],unit[2],p1,8])
                                    unit[3]=False
                                    res[0]-=8
                                if event.key == pygame.K_4 and (MAP[unit[1]][unit[2]]==mountain or MAP[unit[1]][unit[2]]==rock) and res[1]>=20:
                                    buildings.append(["stone mine",unit[1],unit[2],p1,10])
                                    unit[3]=False
                                    res[1]-=20
                                if event.key == pygame.K_5 and MAP[unit[1]][unit[2]]==forest and res[0]>=5:
                                    buildings.append(["lumber hut",unit[1],unit[2],p1,6])
                                    unit[3]=False
                                    res[0]-=5
                                if event.key==pygame.K_6 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock and res[0]>=5:
                                    buildings.append(["house",unit[1],unit[2],p1,6,1])
                                    unit[3]=False
                                    res[0]-=5
                                if event.key==pygame.K_7 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock and res[1]>=15:
                                    buildings.append(["house",unit[1],unit[2],p1,8,2])
                                    unit[3]=False
                                    res[1]-=15
                                if event.key==pygame.K_8 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and res[3]>=10:
                                    buildings.append(["barracks",unit[1],unit[2],p1,10,3])
                                    unit[3]=False
                                    res[3]-=10
                                if False and event.key==pygame.K_0 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and res[1]>=8:
                                    buildings.append(["wall",unit[1],unit[2],p1,50])
                                    unit[3]=False
                                    res[1]-=8
                                if False and event.key==pygame.K_q and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and res[0]>=8:
                                    buildings.append(["wall",unit[1],unit[2],p1,25])
                                    unit[3]=False
                                    res[0]-=8
                                if event.key==pygame.K_9 and not MAP[unit[1]][unit[2]]==water and res[3]>=12:
                                    buildings.append(["airport",unit[1],unit[2],p1,15])
                                    unit[3]=False
                                    res[3]-=12
                                if event.key==pygame.K_w and res[0]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                                    buildings.append(["wood statue",unit[1],unit[2],p1,10])
                                    unit[3]=False
                                    res[0]-=10
                                if event.key==pygame.K_e and res[1]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                                    buildings.append(["stone statue",unit[1],unit[2],p1,15])
                                    unit[3]=False
                                    res[1]-=10
                                if event.key==pygame.K_r and res[3]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                                    buildings.append(["metal statue",unit[1],unit[2],p1,20])
                                    unit[3]=False
                                    res[3]-=10
                                if event.key==pygame.K_t and res[3]>=10 and res[4]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
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
                                                    building[4]-=25
                                            for un in units:
                                                if [pos[0]+1-a,pos[1]+1-b]==[un[1],un[2]] and not(un[0]=="jet" or un[0]=="bomber"):
                                                    un[5]-=5
                                    unit[3]=False
                            if event.type==pygame.KEYUP and unit[0]=="diplomat":
                                    if event.key==pygame.K_1:
                                            done=False
                                            string="*"
                                            while not done:
                                                    for event in pygame.event.get():
                                                            if event.type==KEYDOWN and not event.key==K_RETURN and not event.key==K_BACKSPACE and not event.key==K_TAB and not event.key==K_ESCAPE:
                                                                    string+=event.unicode
                                                            elif event.type==KEYDOWN and event.key==K_BACKSPACE and not string=="*":
                                                                    string=string[:-1]
                                                            elif event.type==KEYUP and event.key==K_RETURN:
                                                                    done=True
                                                    pygame.display.set_caption(string+"*")
                                                    drawMAP(MAP,p1MAP)
                                            unit[6]=string+"*"
                                            unit[3]=False
                                    if event.key==pygame.K_2:
                                            R=["wood","stone","food","metal","gold"]
                                            RN=["1","2","3","4","5"]
                                            N=["0","1","2","3","4","5","6","7","8","9"]
                                            pygame.display.set_caption("1-wood 2-stone 3-food 4-metal 5-gold")
                                            drawMAP(MAP,p1MAP)
                                            done=False
                                            while unit[7][0]==None:
                                                    for event in pygame.event.get():
                                                            if event.type==KEYDOWN and event.unicode in RN:
                                                                  unit[7][0]=int(event.unicode)-1
                                            string=" "
                                            while not done:
                                                    for event in pygame.event.get():
                                                            if event.type==KEYDOWN and event.unicode in N:
                                                                    string+=event.unicode
                                                            elif event.type==KEYUP and event.key==K_RETURN:
                                                                    done=True
                                                    pygame.display.set_caption(string)
                                                    drawMAP(MAP,p1MAP)

                                            if string==" ":
                                                 string="0"   
                                            if res[unit[7][0]]<int(string):
                                                    break
                                            else:
                                                    unit[7][1]=int(string)
                                                    res[unit[7][0]]-=unit[7][1]
                                                    pygame.display.set_caption("1-wood 2-stone 3-food 4-metal 5-gold")
                                                    drawMAP(MAP,p1MAP)

                                                    done=False
                                                    while unit[8][0]==None:
                                                            for event in pygame.event.get():
                                                                    if event.type==KEYDOWN and event.unicode in RN:
                                                                          unit[8][0]=int(event.unicode)-1
                                                    string=" "
                                                    while not done:
                                                            for event in pygame.event.get():
                                                                    if event.type==KEYDOWN and event.unicode in N:
                                                                            string+=event.unicode
                                                                    elif event.type==KEYUP and event.key==K_RETURN:
                                                                            done=True
                                                            pygame.display.set_caption(string)
                                                            drawMAP(MAP,p1MAP)

                                                    if string==" ":
                                                            string="0"
                                                    unit[8][1]=int(string)
                                                    unit[6]=R[unit[8][0]]+"-"+str(unit[8][1])+" --> "+R[unit[7][0]]+"-"+str(unit[7][1])
                                                    unit[3]=False
                                    if event.key==pygame.K_3 and res[3]>=6:
                                            unit.remove(unit[6])
                                            unit.remove(unit[6])
                                            unit.remove(unit[6])
                                            unit[0]="spy"
                                            res[3]-=6
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
                                                
                                        elif testForPort(pos,buildings) and guyCheck(pos,units)==False and (guyCheck(pos,buildings)==False or guyCheck(pos,buildings)==p1) and not type(unit[0])==list and not unit[0]=="jet" and not unit[0]=="bomber":
                                            if unit in units:
                                                units.remove(unit)
                                                units.append([["ship",unit],pos[0],pos[1],False,unit[4],unit[5]])
                                                unit[3]==False
                                        elif unit[0]=="worker" and guyCheck(pos,units)==False and (guyCheck(pos,buildings)==False or guyCheck(pos,buildings)==p1):
                                            if MAP[marker[0]][marker[1]]==water and res[0]>=6:
                                                buildings.append(["port",pos[0],pos[1],p1,8])
                                                res[0]-=6
                                                unit[3]=False
                                        elif type(unit[0])==list and guyCheck(pos,units)==False and (guyCheck(pos,buildings)==False or guyCheck(pos,buildings)==p1) and (MAP[marker[0]][marker[1]]==water or MAP[marker[0]][marker[1]]==ocean):
                                            unit[3]=False
                                            unit[1],unit[2]=pos[0],pos[1]
                                        elif guyCheck(pos,units)==False  and guyCheck(pos,buildings)!=p1 and (unit[0]=="spy" or (type(unit[0])==list and unit[0][1][0]=="spy")):
                                            for un in buildings:
                                                if [un[1],un[2]]==pos:
                                                    un[3]=p1
                                                unit[1],unit[2]=pos[0],pos[1]
                                                unit[3]=False
                                        elif guyCheck(pos,units)!=False and guyCheck(pos,units)!=p1 and (unit[0]=="jet" or unit[0]=="archer" or (type(unit[0])==list and len(unit[0][1])==7)):
                                            for un in units:
                                                if [un[1],un[2]]==pos:
                                                    if unit[0]=="archer":
                                                        un[5]-=3+unit[6]
                                                        unit[3]=False
                                        
                                                    elif unit[0]=="jet" and (un[0]=="jet" or un[0]=="bomber"):
                                                        un[5]-=12
                                                        unit[3]=False
                                                        
                                                    elif type(unit[0])==list:
                                                        un[5]-=unit[0][1][6]*2
                                                        unit[3]=False
                                        elif guyCheck(pos,buildings)!=p1 and (unit[0]=="archer" or (type(unit[0])==list and len(unit[0][1])==7)):
                                            print('go')
                                            for un in buildings:
                                                if [un[1],un[2]]==pos:
                                                    if unit[0]=="archer":
                                                        un[4]-=4+unit[6]
                                                        unit[3]=False
                                                    else:
                                                        un[4]-=unit[0][1][6]*2
                                                        unit[3]=False
                                        elif unit[0]=="green" or unit[0]=="runner" or unit[0]=="swordman":
                                            for a in range(2):
                                                for b in range(2):
                                                    if pos[0]==unit[1]+a*round(2*(.5-b)) and pos[1]==unit[2]+(1-a)*round(2*(.5-b)):
                                                        for un in units:
                                                            if [un[1],un[2]]==pos and not (un[0]=="jet" or un[0]=="bomber") and un[4]!=p1:
                                                                if unit[0]=="runner" or unit[0]=="green":
                                                                    un[5]-=2+unit[6]
                                                                else:
                                                                    un[5]-=8+2*unit[6]
                                                                unit[3]=False
                                                        for un in buildings:
                                                            if [un[1],un[2]]==pos and not (un[0]=="jet" or un[0]=="bomber") and un[3]!=p1:
                                                                if unit[0]=="runner" or unit[0]=="green":
                                                                    un[4]-=2+unit[6]
                                                                else:
                                                                    un[4]-=8+unit[6]
                                                                unit[3]=False
                                        elif unit[0]=="diplomat" and guyCheck(pos,units)!=p1:
                                                for un in units:
                                                        if [un[1],un[2]]==pos and (un[0]=="diplomat"):
                                                                pygame.display.set_caption(un[6])
                                                                drawMAP(MAP,p1MAP)
                                                                if un[8][0]!=None:
                                                                        if res[un[8][0]]>=un[8][1]:
                                                                                pygame.display.set_caption(un[6]+" 1-accept trade")
                                                                                drawMAP(MAP,p1MAP)
                                                                x= True
                                                                while x:
                                                                        for event in pygame.event.get():
                                                                            if event.type==pygame.MOUSEBUTTONUP:
                                                                                pos=pygame.mouse.get_pos()
                                                                                pos=[round((pos[0]-C)/Coef-.5),round(pos[1]/Coef-.5)]
                                                                                x=False

                                                                            if un[8][0]!=None and res[un[8][0]]>=un[8][1] and event.type==KEYUP and event.key==pygame.K_1:
                                                                                unit[3]=False
                                                                                x=False
                                                                                res[un[8][0]]-=un[8][1]
                                                                                res[un[7][0]]+=un[7][1]
                                                                                un[6]="Accepted Trade"
                                                                                un[7]=un[8]
                                                                                un[8]=[None,0]


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
                        if [unit[1],unit[2]]==pos and p1MAP[unit[1]][unit[2]] and not unit[3]==p1:
                                pygame.display.set_caption("health-"+str(unit[4]))
                                drawMAP(MAP,p1MAP)
                                while x:
                                        for event in pygame.event.get():
                                            if event.type==pygame.MOUSEBUTTONUP:
                                                pos=pygame.mouse.get_pos()
                                                pos=[round((pos[0]-C)/Coef-.5),round(pos[1]/Coef-.5)]
                                                x=False
                        if [unit[1],unit[2]]==pos and p1MAP[unit[1]][unit[2]] and unit[3]==p1:
                            pygame.display.set_caption(buildInfo(unit,res))
                            drawMAP(MAP,p1MAP)
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
                                            units.append(["worker",pos[0],pos[1],False,p1,5])
                                            x=False
                                        if event.key == pygame.K_5 and res[5]>=2 and res[4]>=4:
                                            res[5]-=2
                                            res[4]-=4
                                            units.append(["diplomat",pos[0],pos[1],False,p1,4," ",[None,0],[None,0]])
                                            x=False                                        
                                        if event.key == pygame.K_2 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                            res[5]-=unit[5]+1
                                            res[4]-=6+2*re
                                            res[re]-=5
                                            units.append(["swordman",pos[0],pos[1],False,p1,10+re,unit[5]])
                                            x=False
                                        if event.key == pygame.K_3 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                            res[5]-=unit[5]+1
                                            res[4]-=6+2*re
                                            res[re]-=5
                                            units.append(["runner",pos[0],pos[1],False,p1,16+re,unit[5]])
                                            x=False
                                        if event.key == pygame.K_4 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                            res[5]-=unit[5]+1
                                            res[4]-=6+2*re
                                            res[re]-=5
                                            units.append(["archer",pos[0],pos[1],False,p1,8+re,unit[5]])
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
            if unit[0]=="diplomat" and not unit[7][0]==None:
                    res[unit[7][0]]+=unit[7][1]
            units.remove(unit)
def sig(x):
    return (2/(1+math.exp(-3*x)))-1
def SCORE(pos,relations):
    res=pos[0]
    player=pos[1]
    p1MAP=pos[2]
    MAP=pos[3]
    buildings=pos[4]
    units=pos[5]
    score=0
    seen=[]
    jets=0
    bombers=0
    swordmen=0
    archers=0
    runners=0
    D=0
    g=0
    for unit in units:
        if unit[4]==turn:
            for n in range(3):
                for m in range(3):
                    if not p1MAP[unit[1]+n-1][unit[2]+m-1]:
                        score+=1/(math.sqrt((22-unit[1]+n-1)**2+(22-unit[2]+m-1)**2)+1)
    for unit in units:
        if unit[3]:
            score-=1
        if unit[0]=='green' and unit[3]:
            score+=.25

        #if unit[4]==player:
        #    g+=1
        #    score-=g*.5
        #    score+=1.5
        if p1MAP[unit[1]][unit[2]]:
            if not unit[4] in seen:
                seen.append(unit[4])
            score+=unit[5]*relations[int(unit[4][1])-1]

            if relations[int(unit[4][1])-1]==-1:
                if unit[0]=='runner':
                    runners+=1
                if unit[0]=='archer':
                    archers+=1
                if unit[0]=='swordman':
                    swordmen+=1
                if unit[0]=='jet':
                    jets+=1
                if unit[0]=='bomber':
                    bombers+=1
    minD=1000
    minD2=1000
    for s in seen:
      minD=1000
      minD2=1000

      for unit in units:
        if (unit[0]=='diplomat' or (type(unit)==list and unit[0][1][0]=='diplomat')) and unit[4]==player:
                score-=5
                D+=len(seen)
                for u in units:
                    if u[4]==s and not u[4]==player and p1MAP[u[1]][u[2]]:
                        minD=min(minD,((u[1]-unit[1])**2+(u[2]-unit[2])**2))
                for u in units:
                    if u[4]==s and not u[4]==player and p1MAP[u[1]][u[2]] and (u[0]=='diplomat' or (type(u)==list and u[0][1][0]=='diplomat')):
                        minD2=min(minD2,((u[1]-unit[1])**2+(u[2]-unit[2])**2))/1000
    if not minD2==1000:
        score-=minD2/1000

    else:
        score-=minD/1000
    Mworker=0
    Mjet=0
    Mbomber=0
    Marcher=0
    Mspy=0
    Mswordman=0
    Mrunner=0
    for unit in units:
        if unit[4]==player:
            if unit[0]=='worker' or type(unit)==list and unit[0][1][0]=='worker':
                Mworker+=1
            if unit[0]=='jet'or type(unit)==list and unit[0][1][0]=='jet':
                Mjet+=1
            if unit[0]=='bomber'or type(unit)==list and unit[0][1][0]=='bomber':
                Mbomber+=1
            if unit[0]=='archer'or type(unit)==list and unit[0][1][0]=='archer':
                Marcher+=1
            if unit[0]=='spy'or type(unit)==list and unit[0][1][0]=='spy':
                Mspy+=1
            if unit[0]=='swordman'or type(unit)==list and unit[0][1][0]=='swordman':
                Mswordman+=1
            if unit[0]=='runner' or unit[0]=='green' or type(unit)==list and (unit[0][1][0]=='runner' or unit[0][1][0]=='green'):
                Mrunner+=1

    score+=2*math.sqrt(Mworker)
    score+=bombers*math.sqrt(Mjet)
    score+=(4-jets)*math.sqrt(Mbomber)
    score+=swordmen*math.sqrt(Marcher)
    score+=1.3*math.sqrt(Mspy)
    score+=runners*math.sqrt(Mswordman)
    score+=(.8+archers)*math.sqrt(Mrunner)
    F=False
    for unit in units:
        if unit[4]==player:
            if unit[0] in ['swordman','runner','archer','bomber','jet','spy','green']:
                S=0
                for u in units:
                    if p1MAP[u[1]][u[2]] and relations[int(u[4][1])-1]==-1:
                        S=max(S,1/(((u[1]-unit[1])**2+(u[2]-unit[2])**2)))
                for u in buildings:
                   if p1MAP[u[1]][u[2]] and relations[int(u[3][1])-1]==-1:
                        S=max(S,1/(((u[1]-unit[1])**2+(u[2]-unit[2])**2))) 
                score+=S
    H=0
    P=0
    A=0
    R=deepcopy(res)

    for unit in units:
            if guyCheck(unit,buildings)==False and R[0]<8 and MAP[unit[1]][unit[2]]==forest:
                score+=.15
    for b in buildings:
        if b[3]==player:
            if b[0]=='house':
                H+=1.5*b[5]
            if b[0]=='barracks':
                H+=6
            if b[0]=='airport':
                P+=5
            if b[0]=='port':
                P+=.5
    score+=math.sqrt(H)+math.sqrt(A)+math.sqrt(P)
    for t in range(6):
        if F and R[0]>=10:
            R[1]+=5
            R[0]-=6
        culture=0
        housing=0
        for building in buildings:
            if building[3]==player:
                if building[0]=="farm":
                    R[2]+=2
                if building[0]=="lumber hut":
                    R[0]+=3
                if building[0]=="wood mine":
                    R[1]+=1
                if building[0]=="stone mine":
                    R[1]+=2
                    R[3]+=1
                if building[0]=="house":
                    housing+=3*building[5]
                if building[0]=="fishing spot":
                    R[2]+=5
                if building[0]=="wood statue":
                    culture+=1
                if building[0]=="stone statue":
                    culture+=3
                if building[0]=="metal statue":
                    culture+=6
                if building[0]=="gold statue":
                    culture+=10
        for unit in units:
           if player==unit[4]:
                        if unit[0]=="worker" or (type(unit[0])==list and unit[0][1][0]=="worker"):
                            R[2]-=1
                        elif unit[0]=="spy" or unit[0]=="diplomat" or (type(unit[0])==list and (unit[0][1][0]=="spy" or unit[0][1][0]=="diplomat")):
                           R[2]-=2
                        elif unit[0]=="jet" or unit[0]=="bomber"  or (type(unit[0])==list and (unit[0][1][0]=="jet" or unit[0][1][0]=="bomber")):
                           R[2]-=5
                        else:
                           if not type(unit[0])==list:
                              R[2]-=unit[5]+1
                           else:
                              R[2]-=unit[0][1][5]+1
                        R[2]=max(0,R[2])
        R[5]=min(R[2],housing,R[5]+culture)
        R[2]-=R[5]
        R[4]+=R[5]
    for r in range(6):
         score+=math.sqrt(R[r])
    score+=12*min(D,len(seen)-1)
    return(score)
def AI(res,player,p1MAP,MAP,buildings,units,relations,needs,ST):
    for unit in units:
        if unit[4]==turn:
            for n in range(3):
                for m in range(3):
                        p1MAP[unit[1]+n-1][unit[2]+m-1]=True
    p1=player[0]
    for u in units:
        if u[0]=="diplomat" and u[4]==p1:
            if u[3]:
                u[6]=" "
                if not u[7][0]==None:
                    res[u[7][0]]+=u[7][1]
                u[7]=[None,0]
                u[8]=[None,0]
    p1p2=relations[0][0]
    p1p3=relations[0][1]
    p1p4=relations[0][2]
    p2p3=relations[0][3]
    p2p4=relations[0][4]
    p3p4=relations[0][5]
    if p1=='p1':
        R=[0,p1p2,p1p3,p1p4]
    if p1=='p2':
        R=[p1p2,0,p2p3,p2p4]
    if p1=='p3':
        R=[p1p3,p2p3,0,p3p4]
    if p1=='p4':
        R=[p1p4,p2p4,p3p4,0]
    if ST:
        News=[]
        ST=False
        RES=["wood","stone","food","metal","gold"]
        p1Words=["p1","P1","RED","red","Red"]
        p2Words=["p2","P2","BLUE","blue","Blue"]
        p3Words=["p3","P3","GREEN","green","Green"]
        p4Words=["p4","P4","YELLOW","yellow","Yellow"]
        warWords=["battle","war","fight","attack","beat"]
        peaceWords=["peace","end","broken","can't","don't"]
        friendWords=["friend","alliance","team","help","will"]
        needWords=["need","please"]
        Min=10000
        lowest=None
        for r in range(5):
            if r==2 and res[r]>10:
                continue
            if res[r]<Min:
                Min=res[r]
                lowest=r
        News.append(["*I need "+RES[lowest]+"*",0])
        p1p2=relations[0][0]
        p1p3=relations[0][1]
        p1p4=relations[0][2]
        p2p3=relations[0][3]
        p2p4=relations[0][4]
        p3p4=relations[0][5]
        P1C=0
        P2C=0
        P3C=0
        P4C=0
        RM=[[0,p1p2,p1p3,p1p4],[p1p2,0,p2p3,p2p4],[p1p3,p2p3,0,p3p4],[p1p4,p2p4,p3p4,0]]
        if p1=='p1':
            R=[0,p1p2,p1p3,p1p4]
        if p1=='p2':
            R=[p1p2,0,p2p3,p2p4]
        if p1=='p3':
            R=[p1p3,p2p3,0,p3p4]
        if p1=='p4':
            R=[p1p4,p2p4,p3p4,0]
        for unit in buildings:
                if unit[3]==p1:
                     for u in units:
                        if u[0] in ['swordman','runner','archer','bomber','jet'] and p1MAP[u[1]][u[2]] and not u[4]==p1:
                            if u[4]=='p1':
                                P1C-=3/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p2':
                                P2C-=3/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p3':
                                P3C-=3/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p4':
                                P4C-=3/((unit[1]-u[1])**2+(unit[2]-u[2])**2)   
        for unit in units:
            if unit[0]=='diplomat' and unit[4]==p1:
                if unit[3]:
                    for u in units:
                        targets=[]
                        if u[0] in ['swordman','runner','archer','bomber','jet'] and p1MAP[u[1]][u[2]] and not u[4]==p1:
                            if u[4]=='p1':
                                P1C-=1/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p2':
                                P2C-=1/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p3':
                                P3C-=1/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p4':
                                P4C-=1/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                        if (u[0]=="diplomat" or u[0]=='spy') and p1MAP[u[1]][u[2]] and not u[4]==p1:
                            if u[4]=='p1':
                                P1C+=1/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p2':
                                P2C+=1/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p3':
                                P3C+=1/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if u[4]=='p4':
                                P4C+=1/((unit[1]-u[1])**2+(unit[2]-u[2])**2)
                            if [u[1],u[2]] in landMovement(MAP,unit,res,p1MAP,buildings,targets=[]) and u[0]=="diplomat":
                                targets=[]
                                if u[8][0]!=None and res[u[8][0]]>=u[8][1] and math.sqrt(res[u[8][0]])+math.sqrt(res[u[7][0]])<math.sqrt(res[u[8][0]]-u[8][1])+math.sqrt(res[u[7][0]]+u[7][1]):
                                    unit[3]=False
                                    res[u[8][0]]-=u[8][1]
                                    res[u[7][0]]+=u[7][1]
                                    u[6]="Accepted Trade"
                                    u[7]=u[8]
                                    u[8]=[None,0]
                                    if u[4]=='p1':
                                        P1C+=1
                                    if u[4]=='p2':
                                        P2C+=1
                                    if u[4]=='p3':
                                        P3C+=1
                                    if u[4]=='p4':
                                        P4C+=1
                                    needs[int(u[4][1])-1]=None

                                elif u[8][0]!=None:

                                    needs[int(u[4][1])-1]=RES[u[8][0]]
                            
                                M=[]
                                S=None
                                for W in p1Words:
                                    if W in u[6] and not 'p1' in M:
                                        M.append('p1')
                                for W in p2Words:
                                    if W in u[6] and not 'p2' in M:
                                        M.append('p2')
                                for W in p3Words:
                                    if W in u[6] and not 'p3' in M:
                                        M.append('p3')
                                for W in p4Words:
                                    if W in u[6] and not 'p4' in M:
                                        M.append('p4')
                                for W in needWords:
                                    if W in u[6]:
                                        S='need'
                                for W in friendWords:
                                    if W in u[6]:
                                        S='friend'
                                for W in warWords:
                                    if W in u[6]:
                                        S='war'
                                for W in peaceWords:
                                    if W in u[6]:
                                        S='peace'
                                if S in ['peace','friend','war']:
                                    if M==[]:
                                        M=[p1,u[4]]
                                    elif len(M)>2:
                                        M=[]
                                        S=None
                                    elif len(M)==1 and not u[4] in M:
                                        M.append(u[4])
                                    elif len(M)==1 and not p1 in M:
                                        M.append(p1)
                                    elif len(M)==1:
                                        M=[]
                                        S=None
                                    if p1 in M and not u[4] in M:
                                        M=[]
                                        S=None
                                if S=='peace':
                                    G1=M[0]
                                    G2=M[1]
                                    if p1 in M:
                                        if R[int(u[4][1])-1]==-1 and relations[1][int(G2[1])-1]>=-3/7:
                                            News.append(["*"+u[4]+" and I have made peace.*",2])
                                            unit[6]="*I will accept peace.*"
                                            unit[3]=False
                                            RM[int(G2[1])-1][int(G1[1])-1]=0
                                            RM[int(G1[1])-1][int(G2[1])-1]=0
                                            R[int(u[4][1])-1]=0
                                        elif R[int(u[4][1])-1]==-1:
                                            unit[6]="*The war is not over.*"
                                            unit[3]=False
                                        elif R[int(u[4][1])-1]==1:
                                            News.append(["*"+u[4]+" and I have ended our alliance.*",1])
                                            R[int(u[4][1])-1]=0
                                            RM[int(G2[1])-1][int(G1[1])-1]=0
                                            RM[int(G1[1])-1][int(G2[1])-1]=0
                                    else:
                                        RM[int(G2[1])-1][int(G1[1])-1]=0
                                        RM[int(G1[1])-1][int(G2[1])-1]=0
                                if S=='war':
                                    G1=M[0]
                                    G2=M[1]
                                    if p1 in M:
                                            News.append(["*"+u[4]+" has declared war on me.*",4])
                                            unit[6]="*If you incist.*"
                                            unit[3]=False
                                            RM[int(G2[1])-1][int(G1[1])-1]=-1
                                            RM[int(G1[1])-1][int(G2[1])-1]=-1
                                            R[int(u[4][1])-1]=-1
                                    else:
                                        RM[int(G2[1])-1][int(G1[1])-1]=-1
                                        RM[int(G1[1])-1][int(G2[1])-1]=-1
                                if S=='friend':
                                    G1=M[0]
                                    G2=M[1]
                                    if p1 in M:
                                        if relations[1][int(G2[1])-1]>=3/7:
                                            News.append(["*"+u[4]+" and I have formed an alliance.*",2])
                                            unit[6]="*I will accept the alliance.*"
                                            unit[3]=False
                                            RM[int(G2[1])-1][int(G1[1])-1]=1
                                            RM[int(G1[1])-1][int(G2[1])-1]=1
                                            R[int(u[4][1])-1]=1
                                        else:
                                            unit[6]="*I can't accept*"
                                            unit[3]=False
                                    else:
                                        RM[int(G2[1])-1][int(G1[1])-1]=1
                                        RM[int(G1[1])-1][int(G2[1])-1]=1
                                if S=='need':
                                    p=True
                                    K=None
                                    for r in RES:
                                        if r in u[6]:
                                            if p:
                                                K=r
                                                p=False
                                            else:
                                                K=None
                                    if not K==None:
                                        needs[int(u[4][1])-1]=K
                                if not R[int(u[4][1])-1]==-1 and relations[1][int(u[4][1])-1]<-5/7 and unit[3]:  
                                    News.append(["*I have declared war on "+u[4]+".*",4])
                                    unit[6]="*I declare war on you.*"
                                    unit[3]=False
                                    RM[int(u[4][1])-1][int(p1[1])-1]=-1
                                    RM[int(p1[1])-1][int(u[4][1])-1]=-1
                                    R[int(u[4][1])-1]=-1
                                if R[int(u[4][1])-1]==-1 and relations[1][int(u[4][1])-1]>-1/7 and unit[3]:
                                    News.append(["*I am trying to make peace with "+u[4]+".*",2])
                                    unit[6]="*Can we please end this war?*"
                                    unit[3]=False
                                    RM[int(u[4][1])-1][int(p1[1])-1]=0
                                    RM[int(p1[1])-1][int(u[4][1])-1]=0
                                    R[int(u[4][1])-1]=0
                                if not R[int(u[4][1])-1]==1 and relations[1][int(u[4][1])-1]>5/7 and unit[3]:  
                                    News.append(["*I am asking "+u[4]+"to join the alliance.*",3])
                                    unit[6]="*Do you want to make an alliance.*"
                                    unit[3]=False
                                    RM[int(u[4][1])-1][int(p1[1])-1]=1
                                    RM[int(p1[1])-1][int(u[4][1])-1]=1
                                    R[int(u[4][1])-1]=1
                                if R[int(u[4][1])-1]==1 and relations[1][int(u[4][1])-1]<1/7 and unit[3]:
                                    News.append(["*I have ended the alliance with "+u[4]+".*",1])
                                    unit[6]="*I am ending our alliance.*"
                                    unit[3]=False
                                    RM[int(u[4][1])-1][int(p1[1])-1]=0
                                    RM[int(p1[1])-1][int(u[4][1])-1]=0
                                    R[int(u[4][1])-1]=0
        for Play in range(4):
            if relations[1][Play]<-5/7:  
                RM[Play][int(p1[1])-1]=-1
                RM[int(p1[1])-1][Play]=-1
                R[Play]=-1
        L=-1
        for n in News:
            if n[1]>L:
                L=n[1]
                NEWS=n[0]
        for unit in units:
            if unit[0]=="diplomat" and unit[4]==p1:
                for u in units:
                    targets=[]
                    if u[0]=="diplomat" and not u[4]==p1 and p1MAP[u[1]][u[2]] and [u[1],u[2]] in landMovement(MAP,unit,res,p1MAP,buildings,targets=[]):
                        targets=[]
                        if unit[3] and not R[int(u[4][1])-1]==-1:
                            if not needs[int(u[4][1])-1]==None and not RES[lowest]==needs[int(u[4][1])-1] and (R[int(u[4][1])-1]==0 or L>=0):
                                for T in range(len(RES)):
                                    if RES[T]==needs[int(u[4][1])-1]:
                                        O=T
                                unit[7][0]=O
                                unit[7][1]=round(res[O]/10)
                                unit[8][0]=lowest
                                if R[int(u[4][1])-1]==0:
                                        unit[8][1]=round(15/100*math.sqrt(res[lowest])*math.sqrt(res[O]))+2
                                else:
                                        unit[8][1]=round(11/100*math.sqrt(res[lowest])*math.sqrt(res[O]))+1

                                unit[6]=RES[unit[8][0]]+"-"+str(unit[8][1])+" --> "+RES[unit[7][0]]+"-"+str(unit[7][1])
                                unit[3]=False
                            elif R[int(u[4][1])-1]==0:
                                unit[6]=News[0][0]
                                unit[3]=False
                            else:
                                unit[6]=NEWS
                                unit[3]=False
        for k in range(4):
            P1C+=R[k]*RM[k][0]
            P2C+=R[k]*RM[k][1]
            P3C+=R[k]*RM[k][2]
            P4C+=R[k]*RM[k][3]
        J=(P1C+P2C+P3C+P4C)/3
        P1C-=J
        P2C-=J
        P3C-=J
        P4C-=J
        relations[1][0]+=sig(P1C)**3-relations[1][0]*sig(P1C)**2
        relations[1][1]+=sig(P2C)**3-relations[1][1]*sig(P2C)**2
        relations[1][2]+=sig(P3C)**3-relations[1][2]*sig(P3C)**2
        relations[1][3]+=sig(P4C)**3-relations[1][3]*sig(P4C)**2
        relations[1][int(p1[1])-1]=0
        relations[0]=[RM[0][1],RM[0][2],RM[0][3],RM[1][2],RM[1][3],RM[2][3]]
    POS=[res,p1,p1MAP,MAP,buildings,deepcopy(units)]
    poss=[deepcopy(POS)]
    OPOS=deepcopy(POS)
    best=SCORE(OPOS,R)
    action=OPOS
    UU=deepcopy(units)
    for unit in units:
        if unit[4]==p1 and unit[3]:
            if unit[0]=="worker" or unit[0]=="archer" or unit[0]=="swordman" or unit[0]=="runner" or unit[0]=="green" or unit[0]=="spy" or unit[0]=="diplomat":
                markers=landMovement(MAP,unit,res,p1MAP,buildings,targets=[])
            elif type(unit[0])==list:
                markers=waterMovement(MAP,unit,res,p1MAP,buildings,targets=[])
            else:
                markers=airMovement(MAP,unit,res,p1MAP,buildings,targets=[])
            if not markers==[]:
                break
    

    U=deepcopy(unit)
    pos=[unit[1],unit[2]]
    if unit[4]==p1 and unit[3]:
        for i in range(10):
            if guyCheck(pos,buildings)==False and type(unit[0])==list and unit[0][1][0]=="worker":
                if i==0 and MAP[unit[1]][unit[2]]==water and res[0]>=6:
                    res[0]-=6
                    buildings.append(["port",pos[0],pos[1],p1,8])
                    unit[3]=False
                if i==0 and MAP[unit[1]][unit[2]]==ocean and res[0]>=5:
                    res[0]-=5
                    buildings.append(["fishing spot",pos[0],pos[1],p1,6])
                    unit[3]=False
            if guyCheck(pos,buildings)==False and unit[0]=="worker":
                if i==0 and MAP[unit[1]][unit[2]]==forest:
                    res[0]+=10
                    MAP[unit[1]][unit[2]]=grass
                    unit[3]=False
                if i==1 and MAP[unit[1]][unit[2]]==grass:
                    buildings.append(["farm",unit[1],unit[2],p1,6])
                    unit[3]=False
                if i==0 and (MAP[unit[1]][unit[2]]==mountain or MAP[unit[1]][unit[2]]==rock) and res[0]>=8:
                    buildings.append(["wood mine",unit[1],unit[2],p1,8])
                    unit[3]=False
                    res[0]-=8
                if i==1 and (MAP[unit[1]][unit[2]]==mountain or MAP[unit[1]][unit[2]]==rock) and res[1]>=20:
                    buildings.append(["stone mine",unit[1],unit[2],p1,10])
                    unit[3]=False
                    res[1]-=20
                if i==1 and MAP[unit[1]][unit[2]]==forest and res[0]>=5:
                    buildings.append(["lumber hut",unit[1],unit[2],p1,6])
                    unit[3]=False
                    res[0]-=5
                if i==2 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock and res[0]>=5:
                    buildings.append(["house",unit[1],unit[2],p1,6,1])
                    unit[3]=False
                    res[0]-=5
                if i==3 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and not MAP[unit[1]][unit[2]]==rock and res[1]>=15:
                    buildings.append(["house",unit[1],unit[2],p1,8,2])
                    unit[3]=False
                    res[1]-=15
                if i==4 and  not MAP[unit[1]][unit[2]]==mountain and not MAP[unit[1]][unit[2]]==water and res[3]>=10:
                    buildings.append(["barracks",unit[1],unit[2],p1,10,3])
                    unit[3]=False
                    res[3]-=10
                if i==5 and not MAP[unit[1]][unit[2]]==water and res[3]>=12:
                    buildings.append(["airport",unit[1],unit[2],p1,15])
                    unit[3]=False
                    res[3]-=12
                if i==6 and res[0]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                    buildings.append(["wood statue",unit[1],unit[2],p1,10])
                    unit[3]=False
                    res[0]-=10
                if i==7 and res[1]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                    buildings.append(["stone statue",unit[1],unit[2],p1,15])
                    unit[3]=False
                    res[1]-=10
                if i==8 and res[3]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                    buildings.append(["metal statue",unit[1],unit[2],p1,20])
                    unit[3]=False
                    res[3]-=10
                if i==9 and res[3]>=10 and res[4]>=10 and (MAP[unit[1]][unit[2]]==grass or MAP[unit[1]][unit[2]]==mountain):
                    buildings.append(["gold statue",unit[1],unit[2],p1,5])
                    unit[3]=False
                    res[3]-=10
                    res[4]-=10
            if unit[0]=="bomber":
                if i==0:
                    for a in range(3):
                        for b in range(3):
                            for building in buildings:
                                if [pos[0]+1-a,pos[1]+1-b]==[building[1],building[2]]:
                                    building[4]-=25
                            for un in units:
                                if [pos[0]+1-a,pos[1]+1-b]==[un[1],un[2]] and not(un[0]=="jet" or un[0]=="bomber"):
                                    un[5]-=5
                    unit[3]=False
            if unit[0]=="diplomat":
                    if i==0 and res[3]>=6:
                            unit.remove(unit[6])
                            unit.remove(unit[6])
                            unit.remove(unit[6])
                            unit[0]="spy"
                            res[3]-=6
                            unit[3]=False
            if unit[3]==False:
                poss.append(deepcopy(POS))
            POS=deepcopy(poss[0])
            res=POS[0]
            p1=POS[1]
            p1MAP=POS[2]
            MAP=POS[3]
            buildings=POS[4]
            units=POS[5]
            for unit in units:
                if unit==U:
                    break
        for marker in markers:
                pos=marker
                if guyCheck(marker,units)==False and (not (MAP[marker[0]][marker[1]]==water or MAP[marker[0]][marker[1]]==ocean) or unit[0]=="jet" or unit[0]=="bomber") and (guyCheck(pos,buildings)==False or guyCheck(pos,buildings)==p1):
                    if unit[0]=="runner":
                        unit[0]="green"
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
                elif testForPort(pos,buildings) and guyCheck(pos,units)==False and (guyCheck(pos,buildings)==False or guyCheck(pos,buildings)==p1) and not type(unit[0])==list and not unit[0]=="jet" and not unit[0]=="bomber":
                    if unit in units:
                        unit[3]=False
                        units.remove(unit)
                        units.append([["ship",unit],pos[0],pos[1],False,unit[4],unit[5]])
                        unit[3]==False
                elif unit[0]=="worker" and guyCheck(pos,units)==False and (guyCheck(pos,buildings)==False or guyCheck(pos,buildings)==p1):
                    if MAP[marker[0]][marker[1]]==water and res[0]>=6:
                        buildings.append(["port",pos[0],pos[1],p1,8])
                        res[0]-=6
                        unit[3]=False
                elif type(unit[0])==list and guyCheck(pos,units)==False and (guyCheck(pos,buildings)==False or guyCheck(pos,buildings)==p1) and (MAP[marker[0]][marker[1]]==water or MAP[marker[0]][marker[1]]==ocean):
                    unit[3]=False
                    unit[1],unit[2]=pos[0],pos[1]
                elif guyCheck(pos,units)==False  and guyCheck(pos,buildings)!=p1 and (unit[0]=="spy" or (type(unit[0])==list and unit[0][1][0]=="spy")):
                    for un in buildings:
                        if [un[1],un[2]]==pos:
                            un[3]=p1
                        unit[1],unit[2]=pos[0],pos[1]
                        unit[3]=False
                elif guyCheck(pos,units)!=False and guyCheck(pos,units)!=p1 and (unit[0]=="jet" or unit[0]=="archer" or (type(unit[0])==list and len(unit[0][1])==7)):
                    for un in units:
                        if [un[1],un[2]]==pos:
                            if unit[0]=="archer":
                                un[5]-=3+unit[6]
                                unit[3]=False
                
                            elif unit[0]=="jet" and (un[0]=="jet" or un[0]=="bomber"):
                                un[5]-=12
                                unit[3]=False
                                
                            elif type(unit[0])==list:
                                un[5]-=unit[0][1][6]*2
                                unit[3]=False
                elif guyCheck(pos,buildings)!=p1 and (unit[0]=="archer" or (type(unit[0])==list and len(unit[0][1])==7)):
                    for un in buildings:
                        if [un[1],un[2]]==pos:
                            if unit[0]=="archer":
                                un[4]-=4+unit[6]
                            else:
                                un[4]-=unit[0][1][6]*2
                            unit[3]=False
                elif unit[0]=="green" or unit[0]=="runner" or unit[0]=="swordman":
                    for a in range(2):
                        for b in range(2):
                            if pos[0]==unit[1]+a*round(2*(.5-b)) and pos[1]==unit[2]+(1-a)*round(2*(.5-b)):
                                for un in units:
                                    if [un[1],un[2]]==pos and not (un[0]=="jet" or un[0]=="bomber") and un[4]!=p1:
                                        if unit[0]=="runner" or unit[0]=="green":
                                            un[5]-=2+unit[6]
                                        else:
                                            un[5]-=8+2*unit[6]
                                        unit[3]=False
                                for un in buildings:
                                    if [un[1],un[2]]==pos and not (un[0]=="jet" or un[0]=="bomber") and un[3]!=p1:
                                        if unit[0]=="runner" or unit[0]=="green":
                                            un[4]-=2+unit[6]
                                        else:
                                            un[4]-=8+unit[6]
                                        unit[3]=False
                if unit[3]==False or unit[0]=='green':
                    poss.append(deepcopy(POS))
                POS=deepcopy(poss[0])
                res=POS[0]
                p1=POS[1]
                p1MAP=POS[2]
                MAP=POS[3]
                buildings=POS[4]
                units=POS[5]
                for unit in units:
                    if unit==U:
                        break
    for unit in buildings:
            
        if guyCheck([unit[1],unit[2]],units)==False and unit[3]==p1 and (unit[0] in ["house","barracks","airport","farm"]):

            if unit in buildings:
                pos=[unit[1],unit[2]]
                for i in range(5):
                    if (unit[0]=="house" or unit[0]=="barracks"):
                            if unit[5]==1:
                                re=0
                            if unit[5]==2:
                                re=1
                            if unit[5]==3:
                                re=3
                            if i==0 and res[5]>=1 and res[4]>=3:
                                res[5]-=1
                                res[4]-=3
                                units.append(["worker",pos[0],pos[1],False,p1,5])
                                x=False
                            if i==4 and res[5]>=2 and res[4]>=4:
                                res[5]-=2
                                res[4]-=4
                                units.append(["diplomat",pos[0],pos[1],False,p1,4," ",[None,0],[None,0]])
                                x=False                                        
                            if i==1 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                res[5]-=unit[5]+1
                                res[4]-=6+2*re
                                res[re]-=5
                                units.append(["swordman",pos[0],pos[1],False,p1,10+re,unit[5]])
                                x=False
                            if i==2 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                res[5]-=unit[5]+1
                                res[4]-=6+2*re
                                res[re]-=5
                                units.append(["runner",pos[0],pos[1],False,p1,16+re,unit[5]])
                                x=False
                            if i==3 and res[5]>=unit[5]+1 and res[4]>=6+2*re and res[re]>=5:
                                res[5]-=unit[5]+1
                                res[4]-=6+2*re
                                res[re]-=5
                                units.append(["archer",pos[0],pos[1],False,p1,8+re,unit[5]])
                                x=False
                    if (unit[0]=="airport"):

                            if i==0 and res[5]>=5 and res[4]>=10 and res[3]>=10:
                                res[5]-=5
                                res[4]-=10
                                res[3]-=10
                                units.append(["bomber",pos[0],pos[1],False,p1,12])
                                x=False
                            if i==1 and res[5]>=5 and res[4]>=10 and res[3]>=10:
                                res[5]-=5
                                res[4]-=10
                                res[3]-=10
                                units.append(["jet",pos[0],pos[1],False,p1,20])
                                x=False
                        
                    poss.append(deepcopy(POS))
                    POS=deepcopy(poss[0])
                    res=POS[0]
                    p1=POS[1]
                    p1MAP=POS[2]
                    MAP=POS[3]
                    buildings=POS[4]
                    units=POS[5]
            if not unit[0]=="farm":
                break
    #poss.append(OPOS)
    H=True                   
    for a in poss:
        g=SCORE(a,R)
        if g>best:
            best=g
            action=a
    res=action[0]
    player=action[1]
    p1MAP=action[2]
    MAP=action[3]
    buildings=action[4]
    units=action[5]
    for X in action[5]:
        if not X[3]:
            H=False
    if H:
        return 1
    for building in buildings:
        if building[4]<=0:
            buildings.remove(building)
    for unit in units:
        if unit[5]<=0:
            if unit[0]=="diplomat" and not unit[7][0]==None:
                    res[unit[7][0]]+=unit[7][1]
            units.remove(unit)
    if action==poss[0]:
        units=UU

        return 1
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
        units=[["worker",7,37,True,"p1",5],["worker",37,7,True,"p2",5],["worker",7,7,True,"p3",5],["worker",37,37,True,"p4",5]]
        buildings=[]
        resourses=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
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
            units=[["worker",7,37,True,"p1",5],["worker",37,7,True,"p2",5]]
        if pos[0]>3/9*Height+C and pos[0]<6/9*Height+C and pos[1]>5/16*Height and pos[1]<7/16*Height:
            inAGame=True
            P=0
            players=[1,0,0,0]
            units=[["worker",7,37,True,"p1",5]]
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
                        units.remove(units[P])
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
        elif players[T]==-1:
            F=AI(resourses[T],[turn],M[T],MAP,buildings,units,R[T],N[2],ST)
            ST=False
        elif players[T]==0:
            F=1
        if not F==1 and not F==None:
            [resourses[int(turn[1])-1],MAP,buildings,units]=F
        if players[T]==-1 and (F==1 or F==None):
            j+=1
        if (F==1 and not players[T]==-1) or players[T]==0 or j>=1:
            j=0
            ST=True
            for unit in units:
                unit[3]=True
                if unit[0]=="green":
                    unit[0]="runner"
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
            
            for building in buildings:
                if turn=="p1" and building[3]=="p1":
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
                    
                elif turn=="p2" and building[3]=="p2":
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
                elif turn=="p3" and building[3]=="p3":
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
                    
                elif turn=="p4" and building[3]=="p4":
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
            for unit in units:
                     if turn==unit[4]:
                        k=int(turn[1])-1
                        if unit[0]=="worker" or (type(unit[0])==list and unit[0][1][0]=="worker"):
                            resourses[k][2]-=1
                        elif unit[0]=="spy" or unit[0]=="diplomat" or (type(unit[0])==list and (unit[0][1][0]=="spy" or unit[0][1][0]=="diplomat")):
                           resourses[k][2]-=2
                        elif unit[0]=="jet" or unit[0]=="bomber" or (type(unit[0])==list and (unit[0][1][0]=="jet" or unit[0][1][0]=="bomber")):
                           resourses[k][2]-=5
                        else:
                           if not type(unit[0])==list:
                              resourses[k][2]-=unit[5]+1
                           else:
                              resourses[k][2]-=unit[0][1][5]+1
                        resourses[k][2]=max(0,resourses[k][2])
            if turn=="p3":
                resourses[2][5]=min(resourses[2][2],housing,resourses[2][5]+culture)
                resourses[2][2]-=resourses[2][5]
                resourses[2][4]+=resourses[2][5]
            elif turn=="p4":
                resourses[3][5]=min(resourses[3][2],housing,resourses[3][5]+culture)

                resourses[3][2]-=resourses[3][5]
                resourses[3][4]+=resourses[3][5]
            elif turn=="p1":
                resourses[0][5]=min(resourses[0][2],housing,resourses[0][5]+culture)

                resourses[0][2]-=resourses[0][5]
                resourses[0][4]+=resourses[0][5]
            else:
                resourses[1][5]=min(resourses[1][2],housing,resourses[1][5]+culture)

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

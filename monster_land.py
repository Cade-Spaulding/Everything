import pygame
from pygame.locals import*
from statistics import median
import sys
pygame.init()
windowSurface=pygame.display.set_mode((875,600),0,32)
road=[(200,100,0),[0,0,0,0],[0,0,1,0]]
house=[(200,0,200),[1,1,1,0],[0,0,0,0]]
candle=[(200,0,0),[0,1,2,0],[0,1,2,0]]
ice=[(200,200,200),[0,-1,0,1],[0,-1,0,1]]
tree=[(0,100,0),[2,0,0,0],[0,0,-1,0]]
ocean=[(0,0,200),[-2,-1,-2,2],[0,0,0,1]]
den=[(0,0,0),[-2,1,-2,0],[0,0,0,0]]
orb=[(100,0,200),[1,0,1,0],[1,0,1,0]]
sand=[(200,200,0),[0,1,0,-2],[0,1,0,-2]]
plains=[(0,200,0),[0,0,0,0],[0,0,0,0]]
pixie=[[1,1,1,0],[0,0,2,0],[0,-1,1,1],'pixie',(250,50,250)]
mole=[[-2,1,-2,0],[0,1,-1,0],[0,0,-1,2],'mole',(50,50,50)]
bigFoot=[[0,1,-3,0],[1,0,-2,0],[0,0,0,1],'bigFoot',(50,250,50)]
birdy=[[2,0,0,0],[0,0,-2,0],[0,-1,-1,1],'birdy',(50,150,50)]
crab=[[0,2,1,1],[-1,1,0,2],[-2,0,0,3],'crab',(250,150,50)]
sandMonster=[[0,3,0,-3],[1,2,-1,-3],[0,1,0,-1],'sandMonster',(250,250,50)]
fish=[[-2,-1,-1,5],[-2,0,0,4],[-2,-1,-2,7],'fish',(50,50,250)]
dragon=[[3,2,1,0],[1,2,-1,0],[1,1,1,1],'dragon',(150,50,250)]
icy=[[0,-2,0,1],[1,-4,0,2],[0,-2,0,4],'icy',(250,250,250)]
torchy=[[0,2,2,0],[2,3,2,0],[-1,2,1,1],'torchy',(250,50,50)]
mons=[pixie,mole,bigFoot,birdy,crab,sandMonster,fish,dragon,icy,torchy]
land=[]
for l in range(12):
    line=[]
    for r in range(12):
        line.append(plains)
    land.append(line)
def ok(c1,c2):
    return (c1[0]-c2[0])**2+(c1[1]-c2[1])**2+(c1[2]-c2[2])**2+(c1[3]-c2[3])**2 < 2
def getStats(land):
    stats=[]
    D=[-1,0,1]
    for l in range(12):
        line=[]
        for r in range(12):
            line.append([0,0,0,0])
        stats.append(line)
    for i in range(12):
        for j in range(12):
            for k in range(4):
                stats[i][j][k]+=land[i][j][1][k]
            for V in D:
                for H in D:
                    if not V==H:
                        if i+H in range(12) and j+V in range(12):
                            for k in range(4):
                                stats[i+H][j+V][k]+=land[i][j][2][k]
    return stats
def getMon(stats,mon):
    MIN=[]
    MAX=[]
    pop=0
    for stat in range(4):
        MIN.append(min(mon[0][stat],mon[1][stat],mon[2][stat]))
        MAX.append(max(mon[0][stat],mon[1][stat],mon[2][stat]))
    area=[]
    D=[-1,0,1]
    for l in range(12):
        line=[]
        for r in range(12):
            line.append('none')
        area.append(line)
    home=[]
    spot=[]
    water=[]
    path=[]
    for i in range(12):
        for j in range(12):
            MED=[]
            for stat in range(4):
                MED.append(median([MIN[stat],MAX[stat],stats[i][j][stat]]))
            if ok(mon[0],stats[i][j]):
                area[i][j]='home'
                home.append([i,j])
            elif ok(mon[1],stats[i][j]):
                area[i][j]='spot'
                spot.append([i,j])
            elif ok(mon[2],stats[i][j]):
                area[i][j]='water'
                water.append([i,j])
            elif ok(MED,stats[i][j]):
                area[i][j]='path'
                path.append([i,j])
    safe=home+spot+water+path
    for A in home:
        s=False
        w=False
        domain=[A]
        size=1
        for P in domain:
            for V in D:
                for H in D:
                    if (not V==H) and (not [P[0]+H,P[1]+V] in domain) and ([P[0]+H,P[1]+V] in safe):
                        domain.append([P[0]+H,P[1]+V])
        for S in spot:
            if S in domain:
                s=True
        for W in water:
            if W in domain:
                w=True
        if s and w:
            pop+=1
            a=A[0]
            b=A[1]
            pygame.draw.polygon(windowSurface,mon[4],((50*a+25*b+12,50*b+12),(50*a+25*b+38,50*b+12),(50*a+25*b+38,50*b+38),(50*a+25*b+12,50*b+38)))
    return pop
def drawMAP(land):
    windowSurface.fill((255,255,255))
    for a in range(12):
        for b in range(12):
            pygame.draw.polygon(windowSurface,land[a][b][0],((50*a+25*b,50*b),(50*a+25*b+50,50*b),(50*a+25*b+50,50*b+50),(50*a+25*b,50*b+50)))
while True:
    num=range(12)
    stats=getStats(land)
    POP=""
    drawMAP(land)

    for mon in mons:
        POP+=(mon[3]+"-"+str(getMon(stats,mon))+"  ")
    pygame.display.set_caption(POP)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            pos=[round(pos[0]/50-.5-round(pos[1]/50-.5)/2),round(pos[1]/50-.5)]
            a=pos[0]
            b=pos[1]
            pygame.draw.polygon(windowSurface,(100,100,100),((50*a+25*b,50*b),(50*a+25*b+50,50*b),(50*a+25*b+50,50*b+50),(50*a+25*b,50*b+50)))
            pygame.display.update()
            if pos[0] in num and pos[1] in num:
                pygame.display.set_caption("1-road  2-house  3-candle  4-ice  5-tree  6-ocean  7-den  8-orb  9-sand  0-plains  height="+str(stats[a][b][0])+"  temp="+str(stats[a][b][1])+"  light="+str(stats[a][b][2])+"  water="+str(stats[a][b][3]))
                x=True
                while x:
                    for event in pygame.event.get():
                        if event.type==pygame.KEYUP:
                            if event.key == pygame.K_1:
                                land[pos[0]][pos[1]]=road
                                x=False
                            if event.key == pygame.K_2:
                                land[pos[0]][pos[1]]=house
                                x=False
                            if event.key == pygame.K_3:
                                land[pos[0]][pos[1]]=candle
                                x=False
                            if event.key == pygame.K_4:
                                land[pos[0]][pos[1]]=ice
                                x=False
                            if event.key == pygame.K_5:
                                land[pos[0]][pos[1]]=tree
                                x=False
                            if event.key == pygame.K_6:
                                land[pos[0]][pos[1]]=ocean
                                x=False
                            if event.key == pygame.K_7:
                                land[pos[0]][pos[1]]=den
                                x=False
                            if event.key == pygame.K_8:
                                land[pos[0]][pos[1]]=orb
                                x=False
                            if event.key == pygame.K_9:
                                land[pos[0]][pos[1]]=sand
                                x=False
                            if event.key == pygame.K_0:
                                land[pos[0]][pos[1]]=plains
                                x=False
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            x=False

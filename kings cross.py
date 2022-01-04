from copy import deepcopy
import random
from sys import maxsize
import math
import pygame
from pygame.locals import*
pygame.init()
W=(255,255,255)
G=(127.5,127.5,127.5)
WB=(191.25,191.25,255)
GB=(100.75,100.75,127.5)
B=(0,0,0)
R=(255,0,0)
Y=(255,255,0)
bots=[]
BA=False
WA=False
draw=False
L=[[0,0],[0,0]]
blist=[0.43642435934811613, 0.381921703196649, 0.5662724678630274, 0.7109254545426532, 0.40369599946327106, 0.5130843746761296, 0.37607298813814427, 0.39790065623151244, 0.49810252587122583, 0.47635259358598714, 0.7448167413444872, 0.4825190565524034, 0.3020468431015957, 0.43995330749147676, 0.20238375554927238, 0.6393359684696741, 0.4244552239286382, 0.2804013655737117, 0.47859364866345727, 0.3460182447397399, 0.3075307889836815, 0.530892175292578, 0.4858497489945547, 0.5436031934632055, 0.39386393747127385, 0.6965530066937824, 0.5650806827683434, 0.1509146264769228, 0.40053087759458905, 0.4560076622428466, 0.3484011568016042, 0.30825127400155017, 0.6592215179205714]
for i in range(15):
    bot=[]
    for i in range(33):
        bot.append(random.random())
    bots.append(bot)
def botScore(bot,board,turn):
    if winCheck(board):
        return -15
    score=0
    out=[1,6]
    mid=[2,5]
    cen=[3,4]
    for dot in range(8):
        for stripe in range(8):
            s=board[stripe][dot]
            if not s==None and not 'K' in s and not s=='edge':
                if stripe in out and dot in out:
                    p=0
                if (stripe in out or dot in out) and (stripe in mid or dot in mid):
                    p=1
                if (stripe in out or dot in out) and (stripe in cen or dot in cen):
                    p=2
                if stripe in mid and dot in mid:
                    p=3
                if (stripe in mid or dot in mid) and (stripe in cen or dot in cen):
                    p=4
                if stripe in cen and dot in cen:
                    p=5
                g=1
                if s[0]=='B':
                    g=-1
                if s[1]=='X':
                    m=0
                if s[1]=='+':
                    m=1
                if s[1]=='':
                    m=2
                try:
                    score+=g*bot[6*m+p]
                except:
                    print(6*m+p)
                    print(len(bot))
            if not s==None and s[1]=='K':
                if stripe in out:
                    j=0
                if stripe in mid:
                    j=1
                if stripe in cen:
                    j=2
                if s[0]=='B':
                    score-=bot[18+5*j+6-dot]
                if s[0]=='W':
                    score+=bot[18+5*j+dot-1]
    if turn=='B':
        score*=-1
    return score
def winCheck(board):
    kingDead=0
    for dot in board:
        if dot[6]==['W','K'] or dot[1]==['B','K']:
            return True
        for stripe in dot:
            if stripe==['W','K'] or stripe==['B','K']:
                kingDead+=1
    return kingDead!=2
def DRAW(board,L2):
    windowSurface=pygame.display.set_mode((800,800),0,0)
    windowSurface.fill(G)
    for i in range(8):
        for J in range(8):
            j=7-J
            if [i,J] in L2:
                pygame.draw.polygon(windowSurface,GB,((100*i,100*j),(100*i,100*j+100),(100*i+100,100*j+100),(100*i+100,100*j)))
            if (i+J)%2==0:
                pygame.draw.polygon(windowSurface,W,((100*i,100*j),(100*i,100*j+100),(100*i+100,100*j+100),(100*i+100,100*j)))
                if [i,J] in L2:
                    pygame.draw.polygon(windowSurface,WB,((100*i,100*j),(100*i,100*j+100),(100*i+100,100*j+100),(100*i+100,100*j)))
    
            if board[i][J]=='edge':
                pygame.draw.polygon(windowSurface,B,((100*i,100*j),(100*i,100*j+100),(100*i+100,100*j+100),(100*i+100,100*j)))
            elif board[i][J]!=None: 
                if board[i][J][0]=='B':
                    color=R
                else:
                    color=Y
                if board[i][J][1]=='K':
                    pygame.draw.polygon(windowSurface,color,((100*i+25,100*j+25),(100*i+25,100*j+75),(100*i+75,100*j+75),(100*i+75,100*j+25)))
                if board[i][J][1]=='':
                    pygame.draw.polygon(windowSurface,color,((100*i+25,100*j+50),(100*i+50,100*j+75),(100*i+75,100*j+50),(100*i+50,100*j+25)))
                if board[i][J][1]=='X':
                    pygame.draw.polygon(windowSurface,color,((100*i+40,100*j+40),(100*i+40,100*j+60),(100*i+60,100*j+60),(100*i+60,100*j+40)))
                if board[i][J][1]=='+':
                    pygame.draw.polygon(windowSurface,color,((100*i+40,100*j+25),(100*i+40,100*j+75),(100*i+60,100*j+75),(100*i+60,100*j+25)))
    pygame.display.update()
def getMoves(board,turn):
    BP=[['B','K'],['B',''],['B','+'],['B','X']]
    WP=[['W','K'],['W',''],['W','+'],['W','X']]
    movement=[-1,0,1]
    moves=[]
    if turn=='W':
        P=WP
    else:
        P=BP
    if winCheck(board):
        return []
    for dot in range(8):
        for stripe in range(8):
            if board[dot][stripe] in P:
                for moveH in movement:
                    for moveV in movement:
                        if not (board[dot+moveH][stripe+moveV] in P)and not( board[dot+moveH][stripe+moveV]=='edge'):
                            if board[dot][stripe][1]=='X' and (moveH+moveV==0 or moveH+moveV==-2 or moveH+moveV==2):
                                moves.append([dot,stripe,dot+moveH,stripe+moveV])
                            elif board[dot][stripe][1]=='+' and (moveH+moveV==1 or moveH+moveV==-1):
                                moves.append([dot,stripe,dot+moveH,stripe+moveV])
                            elif board[dot][stripe][1]=='' or board[dot][stripe][1]=='K':
                                moves.append([dot,stripe,dot+moveH,stripe+moveV])
    random.shuffle(moves)
    return(moves)
LL=[10,4,2,.5,.25,.25,1,1,1.2,4,2,.15,.5,.5,4,2,1,.3,5,2,1,3,2.5,2,1,.25,2]
def score(board,turn,boards):
    if winCheck(board):
        return -100
    score=0
    BKL=[0,0]
    WKL=[0,0]
    J=[-1,0,1]
    XW=[0,0]
    XB=[0,0]
    for dot in range(8):
        for stripe in range(8):
            s=board[dot][stripe]

            if s==['B','K']:
                BKL=[7/3+dot/3,stripe]
                #score-=6/(stripe-1)**3
                if stripe==2:
                    score-=10
                if stripe==3:
                    score-=4
                if stripe==4:
                    score-=2
                if stripe==5:
                    score-=.5
                if stripe==6:
                    score-=0
            if s==['W','K']:
                WKL=[7/3+dot/3,stripe]
                #score+=6/(6-stripe)**3
                if stripe==5:
                    score+=10
                if stripe==4:
                    score+=4
                if stripe==3:
                    score+=2
                if stripe==2:
                    score+=.5
                if stripe==1:
                    score+=0
    for dot in range(7):
        for stripe in range(7):
            control=0
            for i in J:
                for k in J:
                    S=board[dot+i][stripe+k]
                    if not (i==0 and k==0):
                        if S==['B','K']:
                            control-=1/4
                        elif S==['W','K']:
                            control+=1/4
                        if S==['B','']:
                            control-=1/4
                        elif S==['W','']:
                            control+=1/4
                        elif S==['B','+'] and i*k==0:
                            control-=1
                        elif S==['W','+'] and i*k==0:
                            control+=1
                        elif S==['B','X'] and not i*k==0:
                            control-=1
                        elif S==['W','X'] and not i*k==0:
                            control+=1
            s=board[dot][stripe]
            if s==['B','']:
                score-=1.6+4/(2+(WKL[0]-dot)**2+(WKL[1]-stripe)**2)
                for i in J:
                    for k in J:
                        if board[dot+i][stripe+k]==['B',''] or ['B','K']:
                            score-=.15
                if dot in [1,6] and stripe in [1,6]:
                    score+=.2
            elif s==['W','']:
                score+=1.6+4/(2+(BKL[0]-dot)**2+(BKL[1]-stripe)**2)
                for i in J:
                    for k in J:
                        if board[dot+i][stripe+k]==['W',''] or ['W','K']:
                            score+=.15
                if dot in [1,6] and stripe in [1,6]:
                    score-=.2
            elif s==['B','+']:
                score-=.8+4/(2+(WKL[0]-dot)**2+(WKL[1]-stripe)**2)
                if dot in [1,6] and stripe in [1,6]:
                    score+=.4
            elif s==['B','X']:
                score-=.8+5/(2+(WKL[0]-dot)**2+(WKL[1]-stripe)**2)
                XB[(dot+stripe)%2]+=1
                if dot in [1,6] and stripe in [1,6]:
                    score+=.4
            elif s==['W','+']:
                score+=.8+4/(2+(BKL[0]-dot)**2+(BKL[1]-stripe)**2)
                if dot in [1,6] and stripe in [1,6]:
                    score-=.4
            elif s==['W','X']:
                score+=.8+5/(2+(BKL[0]-dot)**2+(BKL[1]-stripe)**2)
                if dot in [1,6] and stripe in [1,6]:
                    score-=.4
                XW[(dot+stripe)%2]+=1
            if control>0:
                
                score+=math.sqrt(control)/(3+2.5*max(2*(3.5-stripe)**2,(3.5-dot)**2))
            else:
                score-=math.sqrt(-control)/(3+2.5*max(2*(3.5-stripe)**2,(3.5-dot)**2))

    score+=XW[0]*XW[1]/4
    score-=XB[0]*XB[1]/4
    if turn=='B':
        score*=-1
    return score*2
def score2(board,turn,boards,L):
    if winCheck(board):
        return -100
    score=0
    BKL=[0,0]
    WKL=[0,0]
    J=[-1,0,1]
    XW=[0,0]
    XB=[0,0]
    for dot in range(8):
        for stripe in range(8):
            s=board[dot][stripe]

            if s==['B','K']:
                BKL=[7/3+dot/3,stripe]
                #score-=6/(stripe-1)**3
                if stripe==2:
                    score-=L[0]
                if stripe==3:
                    score-=L[1]
                if stripe==4:
                    score-=L[2]
                if stripe==5:
                    score-=L[3]
                if stripe==6:
                    score-=0
            if s==['W','K']:
                WKL=[7/3+dot/3,stripe]
                #score+=6/(6-stripe)**3
                if stripe==5:
                    score+=L[0]
                if stripe==4:
                    score+=L[1]
                if stripe==3:
                    score+=L[2]
                if stripe==2:
                    score+=L[3]
                if stripe==1:
                    score+=0
    for dot in range(7):
        for stripe in range(7):
            control=0
            for i in J:
                for k in J:
                    S=board[dot+i][stripe+k]
                    if not (i==0 and k==0):
                        if S==['B','K']:
                            control-=L[4]
                        elif S==['W','K']:
                            control+=L[4]
                        if S==['B','']:
                            control-=L[5]
                        elif S==['W','']:
                            control+=L[5]
                        elif S==['B','+'] and i*k==0:
                            control-=L[6]
                        elif S==['W','+'] and i*k==0:
                            control+=L[6]
                        elif S==['B','X'] and not i*k==0:
                            control-=L[7]
                        elif S==['W','X'] and not i*k==0:
                            control+=L[7]
            s=board[dot][stripe]
            if s==['B','']:
                score-=L[8]+L[9]/(L[10]+(WKL[0]-dot)**2+(WKL[1]-stripe)**2)
                for i in J:
                    for k in J:
                        if board[dot+i][stripe+k]==['B',''] or ['B','K']:
                            score-=L[11]
                if dot in [1,6] and stripe in [1,6]:
                    score+=L[12]
            elif s==['W','']:
                score+=L[8]+L[9]/(L[10]+(BKL[0]-dot)**2+(BKL[1]-stripe)**2)
                for i in J:
                    for k in J:
                        if board[dot+i][stripe+k]==['W',''] or ['W','K']:
                            score+=L[11]
                if dot in [1,6] and stripe in [1,6]:
                    score-=L[12]
            elif s==['B','+']:
                score-=L[13]+L[14]/(L[15]+(WKL[0]-dot)**2+(WKL[1]-stripe)**2)
                if dot in [1,6] and stripe in [1,6]:
                    score+=L[16]
            elif s==['B','X']:
                score-=L[17]+L[18]/(L[19]+(WKL[0]-dot)**2+(WKL[1]-stripe)**2)
                XB[(dot+stripe)%2]+=1
                if dot in [1,6] and stripe in [1,6]:
                    score+=L[20]
            elif s==['W','+']:
                score+=L[13]+L[14]/(L[15]+(BKL[0]-dot)**2+(BKL[1]-stripe)**2)
                if dot in [1,6] and stripe in [1,6]:
                    score-=L[16]
            elif s==['W','X']:
                score+=L[17]+L[18]/(L[19]+(BKL[0]-dot)**2+(BKL[1]-stripe)**2)
                if dot in [1,6] and stripe in [1,6]:
                    score-=L[20]
                XW[(dot+stripe)%2]+=1
            if control>0:
                
                score+=math.sqrt(control)/(L[21]+L[22]*max(L[23]*(3.5-stripe)**2,L[24]*(3.5-dot)**2))
            else:
                score-=math.sqrt(-control)/(L[21]+L[22]*max(L[23]*(3.5-stripe)**2,L[24]*(3.5-dot)**2))

    score+=XW[0]*XW[1]*L[25]
    score-=XB[0]*XB[1]*L[25]
    if turn=='B':
        score*=-1
    return score*L[26]
def NewAI(board,turn,time,boards,T=0):
    if T==0:
        DRAW(board,L)
    M=getMoves(board,turn)
    K=deepcopy(board)
    A2=deepcopy(boards)
    M=len(getMoves(board,turn))
    if M==0:
        return([-100,1])
    if T==2 and (time<=M or M==0):
        return([-score(board,turn,boards),1])
    if T==1 and (time<=M or M==0):
        return(None)
    TimeUsed=0
    G=NewAI(board,turn,time/2,boards,T=1)
    if not G==None:
        moves=G[0]
        time-=G[1]
        TimeUsed+=G[1]
        M=len(moves)
    else:
        m=getMoves(board,turn)
        moves=[]
        for move in m:
            moves.append([0,move,0])
        M=len(moves)
    total=0
    X=(time)**(1/2)
    t=time-X
    for move in moves:
        total+=TimeUsed**(move[0]-moves[M-1][0])
    for move in moves:
        makeMove(move[1],board)

        if turn=='B':
            turn='W'
        else:
            turn='B'
        A=round((t*(time)**(move[0]-moves[M-1][0]))/total+((time/(M**2))**1/2)-.5)
        if A>move[2]:
            S=NewAI(board,turn,A,A2+[board],T=2)
            move[0]=S[0]
            TimeUsed+=S[1]
            move[2]=A
        board=deepcopy(K)
        A2=deepcopy(boards)
        if turn=='B':
            turn='W'
        else:
            turn='B'
    moves.sort()
    if T==1:
        return([moves,TimeUsed])
    if T==2:
        #print(moves)
        return([-moves[M-1][0],TimeUsed])
    if T==0:
        print(moves)
        print(moves[M-1][0])
        print(TimeUsed)
        return(moves[M-1][1])
def AI (board,turn,difficulty,boards,inAI=False,test=False):

    if not inAI:
        DRAW(board,L)
        #print(score(board, turn, boards))
    moves=[]
    K=deepcopy(board)
    M=getMoves(board,turn)
    if difficulty<5:
        if not test:
            return score(board,turn,boards)
        return score2(board,turn,boards,LL)
    #boards.append(board)
    for move in M:
        moves.append([-101,move,0])
    for i in range(round(difficulty**(1/5))):
        C=((i)**2)*50+50
        total=0
        for move in moves:
            try:
                total+=(C)**((move[0]-moves[len(moves)-1][0])*C)
            except:
                continue
        g=0
        if i==0:
            total*=2
        for move in moves:
            makeMove(move[1],board)

            if turn=='B':
                turn='W'
            else:
                turn='B'
            if board in boards:
                move[0]=0
                board=deepcopy(K)
                continue

            try:
                A=(difficulty**(2/3))*(C)**((move[0]-moves[len(moves)-1][0])*C)/total
                round((difficulty**(2/3))*(C)**(move[0]*C)/total)
            except:
                continue

            if move[1]==moves[-1][1] and move[2]<difficulty/10:

                move[2]=difficulty/10
                move[0]=-AI(board,turn,difficulty/10,boards+[deepcopy(board)],inAI=True,test=test)

            elif A>move[2] and (moves[len(moves)-1][0]-1/((i+1)**2)<move[0]):
                move[2]=A
                move[0]=-AI(board,turn,A,boards+[deepcopy(board)],inAI=True,test=test)
            board=deepcopy(K)
            if turn=='B':
                turn='W'
            else:
                turn='B'
        moves.sort()
        if i>2 and len(moves)>1:
            if moves[len(moves)-1][2]==difficulty/5:
                break
        #if not inAI:
            #print(round(i/round(difficulty**(1/3))*100)/100)
    if inAI:
        if len(moves)==0:
            return -100
        return moves[len(moves)-1][0]
    if not inAI:
        #print(moves)
        print(round(100*moves[len(moves)-1][0])/100)
    return moves[len(moves)-1][1]
def makeMove(move,board,L=[[0,0],[0,0]]):
    if move==None:
        return None
    dot=move[0]
    stripe=move[1]
    H=move[2]-dot
    V=move[3]-stripe
    peice=board[dot][stripe]
    board[dot][stripe]=None
    board[dot+H][stripe+V]=peice
    L[0][0]=move[0]
    L[0][1]=move[1]
    L[1][0]=move[2]
    L[1][1]=move[3]
def playerMove(board,turn):
    DRAW(board,L)
        
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                pos1=[round((pos[0])/100-.5),7-round(pos[1]/100-.5)]
                X=True
                while X:
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONUP:
                            pos=pygame.mouse.get_pos()
                            pos2=[round((pos[0])/100-.5),7-round(pos[1]/100-.5)]
                            X=False
                                    
                move=None
                moves=getMoves(board,turn)
                move1=str(pos1+pos2)
                for move in moves:
                    if move1==str(move):

                        DRAW(board,L)
                        print(move)
                        return move
def mix(B1,B2):
    B3=[]
    for i in range(33):
        B3.append(B1[i]*.49+B2[i]*.49+random.random()*.02)
    #print(len(B3))
    return B3
S=[]
C=['A','B','C','D','E','F']
#for i in range(85):
#    if len(S)==3:
#        k=[S[0],mix(S[1],S[2]),S[1],mix(S[0],S[2]),S[2],mix(S[0],S[1])]
#        bots=bots+k
#        S=[]
#    print(str(i+1))
#    game=True
#    D2=3*math.log(10)
#    board=[['edge','edge','edge','edge','edge','edge','edge','edge'],['edge',['W',''],['W','+'],None,None,['B','+'],['B',''],'edge'],['edge',['W',''],['W','X'],None,None,['B','X'],['B',''],'edge'],['edge',['W',''],['W','X'],None,None,['B','X'],['B',''],'edge'],['edge',['W','K'],['W','X'],None,None,['B','X'],['B','K'],'edge'],['edge',['W',''],['W','X'],None,None,['B','X'],['B',''],'edge'],['edge',['W',''],['W','+'],None,None,['B','+'],['B',''],'edge'],['edge','edge','edge','edge','edge','edge','edge','edge']]
#    boards=[deepcopy(board)]
#    difficulty='max'
#    while game:
#        mem=deepcopy(board)
#        move=AI(mem,'W',difficulty,deepcopy(boards),D2=D2,L=bots[0],draw=False)
#        print(C[move[0]-1]+str(move[1])+C[move[2]-1]+str(move[3]))
#        makeMove(move,board,L)
#        if winCheck(board):
#            print('P1 win')
#            S.append(bots[0])
#            bots.remove(bots[0])
#            bots.remove(bots[0])
#            game=False
#        elif board in boards:
#            print('it was a tie')
#            bots.append(bots[0])
#            bots.remove(bots[0])
#            bots.append(bots[0])
#            bots.remove(bots[0])
#            game=False
#        boards.append(deepcopy(board))
#        if game:
#            mem=deepcopy(board)
#            move=AI(mem,'B',difficulty,deepcopy(boards),D2=D2,L=bots[1],draw=False)
#            print(C[move[0]-1]+str(move[1])+C[move[2]-1]+str(move[3]))
#            makeMove(move,board,L)
#            if winCheck(board):
#                print('P2 win')
#                S.append(bots[0])
#                bots.remove(bots[0])
#                bots.remove(bots[0])
#                game=False
#            elif board in boards:
#                print('it was a tie')
#                bots.append(bots[0])
#                bots.remove(bots[0])
#                bots.append(bots[0])
#                bots.remove(bots[0])
#                game=False
#            boards.append(deepcopy(board))
#print(str(bots+S))
while True:
    boards=[]
    difficulty=None
    player=None
    game=True
    board=[['edge','edge','edge','edge','edge','edge','edge','edge'],['edge',['W',''],['W','+'],None,None,['B','+'],['B',''],'edge'],['edge',['W',''],['W','X'],None,None,['B','X'],['B',''],'edge'],['edge',['W',''],['W','X'],None,None,['B','X'],['B',''],'edge'],['edge',['W','K'],['W','X'],None,None,['B','X'],['B','K'],'edge'],['edge',['W',''],['W','X'],None,None,['B','X'],['B',''],'edge'],['edge',['W',''],['W','+'],None,None,['B','+'],['B',''],'edge'],['edge','edge','edge','edge','edge','edge','edge','edge']]
    boards=[deepcopy(board)]
    while player==None:
        print('do you want to be black or white')
        answer=input()
        if answer=='white' or answer=='White' or answer=='WHITE' or answer=='w' or answer=='W':
            player='white'
        if answer=='black' or answer=='Black' or answer=='BLACK' or answer=='b' or answer=='B':
            player='black'
    5*math.log(15)
    time=100000
    while difficulty==None:
        print('what difficulty do you want')
        answer=input()
        if answer=='random':
            difficulty=2**3
        if answer=='beginer-1':
            difficulty=2**6
        if answer=='beginer-2':
            difficulty=2**9
        if answer=='easy':
            difficulty=2**12
        if answer=='normal':
            difficulty=2**15
        if answer=='medium hard':
            difficulty=2**18
        if answer=='hard':
            difficulty=2**21
        if answer=='expert':
            difficulty=2**24
        if answer=='master':
            difficulty=2**27
        if answer=='grandmaster':
            difficulty=2**30
        if answer=='champion':
            difficulty=2**33
        if answer=='max':
            difficulty=2**36
        if answer=='battle':
            player='battle'
        if answer=='freeplay':
            player='all'
    while game:
        #time+=100
        if player=='all':
            makeMove(playerMove(board,'W'),board,L)
            if winCheck(board):
                print('you win')
                game=False
            elif board in boards:
                print('we tied')
                game=False
            boards.append(deepcopy(board))
            if game:
                makeMove(playerMove(board,'B'),board,L)
                if winCheck(board):
                    print('you win')
                    game=False
                elif board in boards:
                    print('we tied')
                    game=False
                boards.append(deepcopy(board))
        elif player=='white':
            makeMove(playerMove(board,'W'),board,L)
            if winCheck(board):
                print('you win')
                game=False
            elif board in boards:
                print('we tied')
                game=False
            boards.append(deepcopy(board))
            if game:
                mem=deepcopy(board)
                M=AI(mem,'B',difficulty,deepcopy(boards))
                move=M

                print(str(move))
                makeMove(move,board,L)
                if winCheck(board):
                    print('I win')
                    game=False
                elif board in boards:
                    print('we tied')
                    game=False
                boards.append(deepcopy(board))
        elif player =='black':
            mem=deepcopy(board)
            move=AI(mem,'W',difficulty,deepcopy(boards))
            print(str(move))
            makeMove(move,board,L)
            if winCheck(board):
                print('I win')
                game=False
            elif board in boards:
                print('we tied')
                game=False
            boards.append(deepcopy(board))
            if game:
                makeMove(playerMove(board,'B'),board,L)
                if winCheck(board):
                    print('you win')
                    game=False
                elif board in boards:
                    print('we tied')
                    game=False
                boards.append(deepcopy(board))
        else:
            mem=deepcopy(board)
            if WA:
                move=AI(mem,'W',difficulty,deepcopy(boards),test=True)
            else:
                move=AI(mem,'W',difficulty,deepcopy(boards))
            print(str(move))
            makeMove(move,board,L)
            if winCheck(board):
                print('P1 win')
                
                game=False
            elif board in boards:
                print('it was a tie')
                game=False
            boards.append(deepcopy(board))
            if game:
                mem=deepcopy(board)
                if BA:
                    move=AI(mem,'B',difficulty,deepcopy(boards),test=True)
                else:
                    move=AI(mem,'B',difficulty,deepcopy(boards))
                print(str(move))
                makeMove(move,board,L)
                if winCheck(board):
                    print('P2 win')
                    game=False
                elif board in boards:
                    print('it was a tie')
                    game=False
                boards.append(deepcopy(board))

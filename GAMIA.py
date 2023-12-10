Length = 0
TurnTimer = 30


import random
import time
import os

Turn = 0

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    
Points = [[[0,0],[0,0]],[[0,0],[0,0]]]
Tokens = [[0,0],[0,0]]
Stars = [0,0]

LastOnly=[]
TokenScore = []

Danger=[]

NTW = False


for i in range(2):
    I=[]
    for j in range(2):
        J=[]
        for k in range(2):
            J.append([0,0,0])
        I.append(J)
    TokenScore.append(I)
StarScore = [[0,0,0],[0,0,0]]
def STRING(X):
    return str(X[0])+" - "+str(X[1])+" ("+str(X[2])+" Turns ago)"
def STRINGS(X):
    return str(X[0])+" - "+str(X[1])
def WinCheck2(Points,Tokens):
    if Tokens[0]==Tokens[1]:
        if sum(Points[0])==sum(Points[1]):
            return False
        if sum(Points[0])>sum(Points[1]):
            W1=0
        if sum(Points[0])<sum(Points[1]):
            W1=1
    if Tokens[0]>Tokens[1]:
        W1=0
    if Tokens[0]<Tokens[1]:
        W1=1
    if Points[W1][0]==Points[W1][1]:
        return False
    if Points[W1][0]>Points[W1][1]:
        W2=0
    if Points[W1][0]<Points[W1][1]:
        W2=1
    return 2*W1+W2+1
def WinCheck(Points,Tokens,Stars):
    if Stars[0]==Stars[1]:
        if sum(Tokens[0])==sum(Tokens[1]):
            return False
        if sum(Tokens[0])>sum(Tokens[1]):
            W=0
        if sum(Tokens[0])<sum(Tokens[1]):
            W=1
    if Stars[0]>Stars[1]:
        W=0
    if Stars[0]<Stars[1]:
        W=1
    F=WinCheck2(Points[W],Tokens[W])
    return 4*W+F
Debug=False
X=" "

while not X=="":
    clear_screen()
    print("GAMIA")
    print("By Cade Spaulding")
    print()
    print()
    print("*This Game Requires Eight Players*")
    print()
    X=input("PRESS ENTER TO START OR TYPE \"RULES\": ")
    Random=False
    Simple=False
    if X.upper()=="RULES":
        clear_screen()
        print("Game structure")
        print("______________")
        print()
        print("In order to win, you need to beat your partner, The rest of your team, and the other team")
        print("There are two teams, Players 1-4 make a team, and Players 5-8 make a team")
        print("In addition, each player has a partner, Player 1 with Player 2, Player 3 with Player 4 and so on")
        print("Keep in mind your partner is on your team")
        print()
        input("PRESS ENTER TO CONTINUE: ")
        clear_screen()
        print("Turns")
        print("_____")
        print()
        print("Each turn is split into three parts")
        print("First you will see all the current scores, as well as how outdated they are")
        print("Following this, there will be a discussion time to discuss strategy")
        print("You should split up discussion time between team discussion and partner discussions as you see fit")
        print("Each team should take the same amount of discussion time")
        print("However they can split it up between Partner discussion and Team Discussion differently")
        print("The above information about discussion time is only a suggestion")
        print("However you won't be able to play for 30 seconds after the last player sees the scores")
        print("discussion time is the heart of the game so don't take it lightly")
        print("After this You will be shown the current scores again")
        print("You will be prompted to choose either Points, Tokens, or Stars")
        print("The effects of these choices will be explained next")
        print()
        input("PRESS ENTER TO CONTINUE: ")
        clear_screen()
        print("Points and Tokens")
        print("_________________")
        print()
        print("Points are an individual score, When you choose points you gain One Point")
        print("You will also earn two bonus points if you are the only player on your team to pick stars for two turns in a row")
        print("You will also be able to see the exact number of points you have, however you won't be able to see anyone else's points")
        print("On your Turn Type \"P\" to select Points")
        print()
        print("Tokens are shared between you and your partner, When at least one partner chooses Tokens you gain one Token")
        print("Keep in mind that it is wasteful for both you and your partner to choose tokens as you can only gain one token per turn")
        print("Whenever you pick Tokens the current Tokens score updates, you get to see how many tokens you and your partner have")
        print("as well as how many tokens the other pair on your team has")
        print("The score only updates for you when YOU pick Tokens, Not when your partner picks Tokens")
        print("On your Turn Type \"T\" to select Tokens")
        print()
        input("PRESS ENTER TO CONTINUE: ")
        clear_screen()
        print("Stars")
        print("_____")
        print()
        print("Stars are exclusively a team score")
        print("When you pick Stars your team gains one Star")
        print("If all four members of a team pick Stars, The team will only score three Stars, not four")
        print("However An exception occurs if, for two consecutive turns, a team has all four of their members pick Stars")
        print("And during those two turns the other team is unable to get all four players picking stars on either turn")
        print("In other words, if anyone on your team picks anything other than stars, or if the other team has all four members picking stars")
        print("Then your team won't be eligible to gain four stars on this turn or the next turn")
        print("Bonus Points are similar")
        print("Recall that if you are the only player on your team to pick Stars twice in a row, that you get two bonus points")
        print("This means that if you don't pick Stars, or any other member on your team picks stars")
        print("Then you won't be eligible for the two point bonus for this turn or the next turn")
        print("The score in Stars is only updated when at least two members of the team pick stars")
        print("The Star score updating is independent of if you picked Stars as long as at least two members of the team did")
        print("This means the Star score updates when you and someone else picks stars")
        print("or when two other members of your team, not including you pick Stars")
        print("On your Turn Type \"S\" to select Stars")
        print()
        input("PRESS ENTER TO CONTINUE: ")
        clear_screen()
        print("Winning")
        print("_______")
        print()
        print("In order to win the game you have to be \"Winning\" for two turns in a row")
        print("In order to be Winning on any particular turn you must follow the following criterion")
        print("   a. Your Team has more Stars than the other team, or if Stars are tied, your team has more TOTAL Tokens, from both pairs than the other team")
        print("   b. You and your partner have more Tokens than the other pair on your team, or if Tokens are tied, you and your partner have more TOTAL points than the other pair")
        print("   c. You have more points than your partner, There is no tie breaker for this criterion")
        print("If you follow all three criterion for two turns in a row, you win")
        print()
        input("PRESS ENTER TO CONTINUE: ")

    if X=="Fast":
        TurnTimer=0
    if X=="DEBUG":
        Debug=True
        TurnTimer=0
    if X=="RAND":
        Debug=True
        TurnTimer=0
        Random=True
    if X=="Simple":
        TurnTimer=0
        Simple=True

while Turn<Length or NTW==False or not NTW == WinCheck(Points,Tokens,Stars):
    NTW = WinCheck(Points,Tokens,Stars)
    Turn += 1
    StarAdd=[0,0]
    TokenAdd=[[False,False],[False,False]]
    Bonus=[]
    Info=[]
    if not Debug and not Simple:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    clear_screen()
                    print("Turn #"+str(Turn))
                    print("Player " + str(4*i+2*j+k+1)+ "'s Scores")
                    input()
                    print("Points: "+str(Points[i][j][k]))
                    print("Tokens: "+STRING(TokenScore[i][j][k]))
                    print("Stars: "+STRING(StarScore[i]))
                    input()
        clear_screen()
        print("discussion Time")
        time.sleep(TurnTimer)
    if Simple:
        MP=[]
        MT=[]
        for i in range(2):
            MPI=[]
            MTI=[]
            for j in range(2):
                MPJ=[]
                MTJ=[]
                for k in range(2):
                    clear_screen()
                    print("Turn #"+str(Turn))
                    print("Player " + str(4*i+2*j+k+1)+ "'s Scores")
                    input()
                    print("Points: "+str(Points[i][j][k]))
                    print("Tokens: "+STRING(TokenScore[i][j][k]))
                    print("Stars: "+STRING(StarScore[i]))
                    print()
                    MPJ.append(input("Input Message to Partner : "))
                    MTJ.append(input("Input Message to Team : "))
                MPI.append(MPJ)
                MTI.append(MTJ)
            MP.append(MPI)
            MT.append(MTI)
        clear_screen()
        print("discussion Time")
        time.sleep(TurnTimer)        
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i + j + k == 0 or Random==False:
                    clear_screen()
                    print("Turn #"+str(Turn))
                    print("Player " + str(4*i+2*j+k+1)+ "'s Turn")
                    if not Debug:
                        input()
                    print("Points: "+str(Points[i][j][k]))
                    print("Tokens: "+STRING(TokenScore[i][j][k]))
                    print("Stars: "+STRING(StarScore[i]))
                    if Simple==True:
                        print()
                        print("Message From Partner (Player "+str(4*i+2*j+(1-k)+1) +") : \""+MP[i][j][1-k]+"\"")
                        print()
                        print("Team Messages")
                        print("\""+MT[i][j][1-k]+"\" : (From Player "+ str(4*i+2*j+(1-k)+1)+")")
                        print("\""+MT[i][1-j][k]+"\" : (From Player "+ str(4*i+2*(1-j)+k+1)+")")
                        print("\""+MT[i][1-j][1-k]+"\" : (From Player "+ str(4*i+2*(1-j)+(1-k)+1)+")")
                        print()

                    Choice=None
                    while not Choice in ["P","T","S"]:
                        Choice = input("Choose an action:")
                    if Choice=="P":
                        Points[i][j][k]+=1
                    if Choice=="T":
                        TokenAdd[i][j]=True
                        Info.append([i,j,k])
                    if Choice=="S":
                        StarAdd[i]+=1
                        Bonus.append([i,j,k])
                else:
                    if random.random()<1/3:
                        print("P")
                        Points[i][j][k]+=1
                    elif random.random()<1/2:
                        print("T")

                        TokenAdd[i][j]=True
                        Info.append([i,j,k])
                    else:
                        print("S")

                        StarAdd[i]+=1
                        Bonus.append([i,j,k])                    

    for i in range(2):
        StarScore[i][2]+=1
        for j in range(2):
            for k in range(2):
                TokenScore[i][j][k][2]+=1
    NLastOnly=[]
    for i in Bonus:
        if StarAdd[i[0]]==1:
            if i in LastOnly:
                Points[i[0]][i[1]][i[2]]+=2
            NLastOnly.append(i)
    LastOnly=NLastOnly
    for i in range(2):
        for j in range(2):
            if TokenAdd[i][j]:
                Tokens[i][j]+=1
    for i in range(2):
        Stars[i]+=min(3,StarAdd[i])
    NDanger=[]
    for i in range(2):
        if StarAdd[i]==4 and not StarAdd[1-i]==4:
            if i in Danger:
                Stars[i]+=1
            NDanger.append(i)
    Danger=NDanger
    for i in range(2):
        if StarAdd[i]>1:
            StarScore[i]=[Stars[i],Stars[1-i],0]
    for i in Info:
        TokenScore[i[0]][i[1]][i[2]]=[Tokens[i[0]][i[1]],Tokens[i[0]][1-i[1]],0]


clear_screen()        
print("Player " + str(NTW) + " Wins")
input()

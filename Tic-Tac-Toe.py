#Tic-Tac-Toe using Mini-Max Algorithm
#Vineet Joshi
#GEU,Dehradun


"""-----------------------"""

#Draws the board's current state every time the user turn arrives. 
from tkinter import E
from numpy import Infinity

import sys
sys.setrecursionlimit(30000)


giga = 0

def drawBoard(board):
    print("Current State Of Board : \n\n")
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n")
        if(board[i]==0):
            print("- ",end=" ")
        if (board[i]==1):
            print("O ",end=" ")
        if(board[i]==-1):    
            print("X ",end=" ")
    print("\n\n")

#Takes the user move as input and make the required changes on the board.

def user1Turn(board):
    
    flag = True  #flag to emulate do while loop
    while(flag):
        pos=input("Enter X's position from [1...9]: ")
        pos=int(pos)
        if(board[pos-1]!=0):
            print("Wrong Move!!!")
        else:    
            flag = False
            board[pos-1]=1

def user2Turn(board):
    flag = True  #flag to emulate do while loop
    while(flag):
        pos=input("Enter O's position from [1...9]: ")
        pos=int(pos)
        if(board[pos-1]!=0):
            print("Wrong Move!!!")
        else:    
            flag = False
            board[pos-1]=1



#MinMax function.
def minimax(board,player,alpha,beta,depth):
    global giga 
    x=analyzeBoard2(board)
    if(x!=0): 
        return (x*player)
       
    if (player == 1):
        value = -1
    else:
        value = 1
         
    pos=-1      
    score = 0
    for i in range(0,9):
        if(board[i]==0):        #for each child possible moves...
            board[i]=1
            giga=giga+1

            score =+ minimax(board,(player*-1),alpha,beta,depth+1)

            if(score<value and player == -1):    #if the score is greater than the current best score
                value=score
                pos=i           #then update the best score and position    
            if(score>value and player == 1):    #if the score is greater than the current best score
                value=score
                pos=i           #then update the best score and position        
            board[i]=0

            #alpha beta prunning
            
            if (player == -1):
                beta = max(beta, value)
                if (beta <= alpha):
                    break
            else:
                alpha = max(alpha, value)
                if (alpha <= beta):
                    break
            

    if(pos==-1):
        return 0
    return value
    
 


#Makes the computer's move using minmax algorithm.
def computeTurn(board):
    pos=-1
    value=-1
    LastPossibleMove = -1
    for i in range(0,9):
        if(board[i]==0):    #for each possible moves...
            LastPossibleMove = i
            board[i]=1      #make move...
            score=minimax(board, -1,-Infinity,Infinity,1)   #...and calculate minimax score
            board[i]=0
            print("move "+str(i)+"score "+str(score))
            if(score>value):    #if the score is greater than the current best score
                value=score
                pos=i           #then update the best score and position
    
    if (pos==-1):
        pos = LastPossibleMove
    board[pos]=1    #make the best move



#Analyzes if game is finished.
#returns: winning player if game is finished
def analyzeBoard(board):

    #All possible winning coordinates   
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    #tic tac toe tie coordinates
   

    #Checking for win by comparing the board with the winning coordinates.
    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]]     
    return 0


def convertCoordinatesToSolutions(board):
    solution = []
    for index,item in enumerate(board):
        if(item == 1):
            solution.append(index)
    return sorted(solution)

def analyzeBoard2(board):
    #All possible winning coordinates   

    winningBoards = [[0,1,3,4],[1,2,4,5],[4,5,7,8], [3,4,6,7],  [0,1,4,5,6], [2,3,4,7,8],[0,4,5,6,7],[1,2,3,4,8],[1,3,5,6,8], [0,1,5,6,7],[1,2,3,7,8],[0,2,3,5,7],[0,2,6,8], [1,2,3,6,8], [0,1,5,6,8], [0,2,5,6,7], [0,2,3,7,8], [0,1,4,5,7,8],[1,2,3,5,6,7]]
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0,8):
        if(board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]): 
            return 1   
    for i in winningBoards:
        if convertCoordinatesToSolutions(board) == i:
            return 1
            
    return 0

#Analyzes if game is finished no matter of next move.
#returns: winning player if game is finished
def analyzeBoardFoward(board,depth):
    #Checking for win for all future possible moves.

    if (analyzeBoard(board) !=0) :
        return -1
    for i in range(0,9):
        if (board[i]==0):
            board[i] = 1
            if(analyzeBoard(board) == 1):
                board[i] = 0
                return 0
            board[i] = 0    
    return 1
#Main function
def main():
    
    print(sys.getrecursionlimit())
    player = 1
    singlePlayer=input("Enter 1 for single player, 0 for multiplayer: ")
    singlePlayer=int(singlePlayer)
    #The board is considered in the form of a single dimentional array.
    #One player moves 1 and other move -1.
    board=[0,0,0,0,0,0,0,0,0]
    if(singlePlayer):
        print("Computer : O Vs. You : X")
        player= input("Enter to play 1(st) or 2(nd) :")
        player = int(player)%2
        for i in range (0,9):
            if(analyzeBoard2(board)!=0):
                break
            if((i+player)%2==0):
                print("Computer Turn")
                drawBoard(board)
                computeTurn(board)
            else:
                print("User Turn sc")
                drawBoard(board)
                print((i+player)%2)
                user1Turn(board)
    else:
        
        for i in range (0,9):
            print(i)
            if(analyzeBoard2(board)!=0):
                player=+1
                break
            if((i)%2==0):
                drawBoard(board)
                print("User1 Turn")
                user1Turn(board)
            else:
                drawBoard(board)
                print("User2 Turn")
                user2Turn(board)

    x=analyzeBoard2(board)
    if (singlePlayer):
        if((i+player)%2==0):
            print("Computer wins")
        else:
            print("User wins")
    else:
        print("User"+str(x)+"wins")
    drawBoard(board)      

#---------------#
main()
print(giga)
#---------------#



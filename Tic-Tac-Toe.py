#Tic-Tac-Toe using Mini-Max Algorithm
#Vineet Joshi
#GEU,Dehradun


"""-----------------------"""

#Draws the board's current state every time the user turn arrives. 
from signal import getsignal
from numpy import Infinity



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
    pos = 0
    while(board[pos-1]==0):
        pos=input("Enter X's position from [1...9]: ")
        pos=int(pos)
        if(board[pos-1]!=0):
            print("Wrong Move!!!")
        else:    
            board[pos-1]=-1

def user2Turn(board):
    pos = 0
    while(board[pos-1]!=0):
        pos=input("Enter O's position from [1...9]: ")
        pos=int(pos)
        if(board[pos-1]!=0):
            print("Wrong Move!!!")
        else:    
            board[pos-1]=1



#MinMax function.
def minimax(board,player,alpha,beta):
    global giga 
    x=analyzeBoard(board)
    if(x!=0):   #if move is winning move
        return (x*player)
    pos=-1      
    value=-2
    for i in range(0,9):
        if(board[i]==0):        #for each child possible moves...
            board[i]=player
            giga=giga+1
            score=-minimax(board,(player*-1),alpha,beta)
            if(score>value):    #if the score is greater than the current best score
                value=score
                pos=i           #then update the best score and position    
            board[i]=0

            #alpha beta prunning
           
            if (player == -1):
                beta = min(beta, value)
                if (beta <= alpha):
                    print("prunning")
                    break
            else:
                alpha = min(alpha, value)
                if (alpha <= beta):
                    print("prunning")
                    break
            

    if(pos==-1):
        return 0
    return value
    
#Makes the computer's move using minmax algorithm.
def computeTurn(board):
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):    #for each possible moves...
            board[i]=1      #make move...
            score=-minimax(board, -1,-Infinity,Infinity)   #...and calculate minimax score
            board[i]=0
            if(score>value):    #if the score is greater than the current best score
                value=score
                pos=i           #then update the best score and position
 
    board[pos]=1    #make the best move


#Analyzes if game is finished.
#returns: winning player if game is finished, 0 if draw.
def analyzeBoard(board):

    #All possible winning coordinates   
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    #Checking for win by comparing the board with the winning coordinates.
    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]]
    return 0

#Main function
def main():
    singlePlayer=input("Enter 1 for single player, 0 for multiplayer: ")
    singlePlayer=int(singlePlayer)
    #The board is considered in the form of a single dimentional array.
    #One player moves 1 and other move -1.
    board=[0,0,0,0,0,0,0,0,0]
    if(singlePlayer):
        print("Computer : O Vs. You : X")
        player= input("Enter to play 1(st) or 2(nd) :")
        player = int(player)
        for i in range (0,9):
            if(analyzeBoard(board)!=0):
                break
            if((i+player)%2==0):
                computeTurn(board)
            else:
                drawBoard(board)
                user1Turn(board)
    else:
        for i in range (0,9):
            if(analyzeBoard(board)!=0):
                break
            if((i)%2==0):
                drawBoard(board)
                user1Turn(board)
            else:
                drawBoard(board)
                user2Turn(board)

    x=analyzeBoard(board)
    if(x==0):
         drawBoard(board)
         print("Draw!!!")
    if(x==-1):
         drawBoard(board)
         print("X Wins!!! Y Loose !!!")
    if(x==1):
         drawBoard(board)
         print("X Loose!!! O Wins !!!!")
       
#---------------#
main()
print(giga)
#---------------#



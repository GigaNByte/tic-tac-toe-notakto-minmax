"""
Tic-Tac-Toe using only X'es (Notakto) using Mini-Max Algorithm
Based on Tic-Tac-Toe by:
Vineet Joshi
GEU,Dehradun

"""



#Draws the board's current state every time the user turn arrives. 
from numpy import Infinity

import sys
sys.setrecursionlimit(30000)


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

#MinIMax function.
def minimax(board,player,alpha,beta,depth):
    if(player == 1):
        print("dsadasdsa")
    #Checking if game is finished.
    x=analyzeBoard2(board)  #returns -1 (lose) or 1 (win) or 0 (game not finished)
    if(x!=0): 
        return (x)  #returns score depending on the player

    #initialize the best score    
    if (player == 1):   #is maximizing player
        value = -1      
    else:
        value = 1

    #initialize the best move      
    pos=-1      

    for i in range(0,9): #test all possible moves
        if(board[i]==0): 
            board[i]=1   

            if (player == -1):      #is minimizing player
                score = minimax(board,-1,alpha,beta,depth+1)
                if(score<value):    #if the score is lesser than the current best score
                    value=score
                    pos=i           #update the best score and position  

                beta = max(beta, value)     #alpha beta pruning
                if (beta <= alpha):
                    break    

            else:                   #is maximizing player
                score = minimax(board,1,alpha,beta,depth+1)
                if(score>value):    #if the score is greater than the current best score
                    value=score
                    pos=i           #then update the best score and position   

                alpha = max(alpha, value)   #alpha beta pruning
                if (alpha <= beta):
                    break

            board[i]=0       

    if(pos==-1):    #if there is no more possible move
        return 0
    return value
    
 


#Makes the computer's move using minmax algorithm.
def computeTurn(board):
    pos=-1      
    value=-1
    LastPossibleMove = -1
    for i in range(0,9):    #test all possible moves
        if(board[i]==0):    
            LastPossibleMove = i

            board[i] = 1     
            score = minimax(board, -1,-Infinity,Infinity,1)   #...and calculate minimax score
            board[i] = 0
            
            print("move "+str(i)+" score "+str(score))

            if(score>value):    #if the score is greater than the current best score
                value=score
                pos=i           #then update the best score and position
    
    if (pos==-1):   #if there is no more possible move
        pos = LastPossibleMove  #make the last possible move
    print("RAZ")
    board[pos]=1    #make the best move


#Converts [0,0,0,0,1...] board into [0,1,3,4] board
def convertCoordinatesToSolutions(board):
    solution = []
    for index,item in enumerate(board):
        if(item == 1):
            solution.append(index)
    return sorted(solution)

def analyzeBoard2(board):
    #All possible winning coordinates   
    winningBoards = [[0,1,3,4],[1,2,4,5],[4,5,7,8], [3,4,6,7],  [0,1,4,5,6], [2,3,4,7,8],[0,4,5,6,7],[1,2,3,4,8],[1,3,5,6,8], [0,1,5,6,7],[1,2,3,7,8],[0,2,3,5,7],[0,2,6,8], [1,2,3,6,8], [0,1,5,6,8], [0,2,5,6,7], [0,2,3,7,8], [0,1,4,5,7,8],[1,2,3,5,6,7]]
    losingSolutions= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #classicTicTacToeSolutions
    for i in range(0,8):
        #Checking for lose by comparing the board with the classic winning coordinates "losingSolutions".
        if(board[losingSolutions[i][0]] != 0 and board[losingSolutions[i][0]] == board[losingSolutions[i][1]] and board[losingSolutions[i][0]] == board[losingSolutions[i][2]]): 
            return -1   #should be -1 TODO
    for i in winningBoards:
        #Checking for win by comparing the board with the custom winning coordinates "winningBoards".
        if convertCoordinatesToSolutions(board) == i:
            return 1

    #Checking for not finished game.        
    return 0

'''
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
'''

#Main function
def main():

    player = 1
    singlePlayer=input("Enter 1 for single player, 0 for multiplayer: ")
    singlePlayer=int(singlePlayer)

    #The board is considered in the form of a single dimentional array.
    #Players move 1
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
                '''
                if  (player == 0 and i == 0):
                    board[4]=1
                else: 
                '''   
                drawBoard(board) 
                computeTurn(board)
                
                
                
            else:
                print("User Turn")
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
                user1Turn(board)

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
#---------------#



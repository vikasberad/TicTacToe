board = [' ' for x in range[10]]

def insertLetter(length,pos):
    board[pos]= letter

def printBoard(board):
    print('   |   |   ')
    print(' '+ board[1] + ' | '+ board[2] + '  |'+ board[3])
    print("-------------")
    print('   |   |   ')
    print(' '+ board[4] + '|'+ board[5] + ' | '+ board[6])
    print("-------------")
    print('   |   |   ')
    print(' '+ board[7] + ' | '+ board[8] + ' | '+ board[9])
    print("-------------")

def spaceIsFree(pos):
    return board[pos] == ' '
    
def isBoardFree(board):
    if board.count(' ')>1:
        return Falsel
    else:
        return True 
    
def InWinner(board,letter):
    return (board[1]==letter and board[2]==letter and board[3]==letter) or
    (board[4]==letter and board[5]==letter and board[6]==letter) or
    (board[7]==letter and board[8]==letter and board[9]==letter) or
    (board[1]==letter and board[4]==letter and board[7]==letter) or
    (board[2]==letter and board[5]==letter and board[9]==letter) or
    (board[3]==letter and board[6]==letter and board[9]==letter) or
    (board[1]==letter and board[5]==letter and board[9]==letter) or
    (board[3]==letter and board[5]==letter and board[7]==letter)

def playerMove():
    run = True
    while run:
        move=input("Select the position to enter X between 1 to 9")
        try:
            move = int (move)
            if move>0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print("Sorry position is occupied")
            else:
                print("Please type number between 1 and 9")
        except:
            print("Please type a number")
    
def computermove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x 1!=0]
    move = 0
    for let in ['0' , 'X']
    for i in possibleMoves:
        boardcopy = board[:]
        boardcopy[i] = letter
        if InWinner(boardcopy,let):
            move = i
            return move

    cornerOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)
    if len(cornerOpen)> 0:
        move = selectRandon(cornerOpen)
        return move 
    if 5 in possibleMoves:
        move = 5
        return move 

    edgeOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)
    if len(edgeOpen)> 0:
        move = selectRandon(edgeOpen)
        return move 

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
        

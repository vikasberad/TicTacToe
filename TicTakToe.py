board = [' ' for x in range[10]]

def insertLetter(l,pos):
    board[pos]= letter

def printBoard(b):
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
    
def isBoardFree(b):
    if board.count(' ')>1:
        return Falsel
    else:
        return True 


    

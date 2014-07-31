import random 

board = [0,1,2,
         3,4,5,
         6,7,8]

print "Welcome to Tic Tac Toe!"

def show(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def checkLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True

def checkAll(char):
    if checkLine(char, 0,1,2):
        return True
    if checkLine(char, 3,4,5):
        return True
    if checkLine(char, 6,7,8):
        return True

    if checkLine(char, 0,3,6):
        return True
    if checkLine(char, 1,4,7):
        return True
    if checkLine(char, 2,5,8):
        return True
    if checkLine(char, 0,4,8):
        return True
    if checkLine(char, 2,4,6):
        return True
 


while True:
    show(board)
    turn = raw_input("Select a spot: ")
    turn = int(turn)

    
    if board[turn] != 'x' and board[turn] != 'o':
        board[turn] = 'x'

        if checkAll('x') == True:
            print "-- X WINS --"
            break;
       
        while True:
            random.seed()
            opponent = random.randint(0,8)

            if board[opponent] != 'o' and board[opponent] != 'x':
                board[opponent] = 'o'
               
    
                if checkAll('o') == True:
                    print "-- O WINS --"
                    break;

            break;

    else:
        print 'This spot is taken!'
        
    

   

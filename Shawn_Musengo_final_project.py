import random

def drawboard():
    print
    print " %s| %s| %s" % (board[0],board[1],board[2])
    print "__|__|__"
    print " %s| %s| %s" % (board[3],board[4],board[5])
    print "__|__|__"
    print " %s| %s| %s" % (board[6],board[7],board[8])
    print
    return
   

def iswinner(test):
    if board[0] == test and board[1] == test and board[2] == test:
        return True
    if board[3] == test and board[4] == test and board[5] == test:
        return True
    if board[6] == test and board[7] == test and board[8] == test:
        return True
    if board[0] == test and board[3] == test and board[6] == test:
        return True
    if board[1] == test and board[4] == test and board[7] == test:
        return True
    if board[2] == test and board[5] == test and board[8] == test:
        return True
    if board[0] == test and board[4] == test and board[8] == test:
        return True
    if board[6] == test and board[4] == test and board[2] == test:
        return True
    return False



game = 0
random.seed()
while (game == 0):

    board = ["1","2","3","4","5","6","7","8","9"]
    print "Welcome to Tic Tac Toe"
    print
    player1 = raw_input("Player ones name? ")
    player2 = raw_input("player two's name? (type 'python' for computer) ")
    movesplayed = 0
    playersturn = 1
    gamewon = False
    while (movesplayed < 9):
        drawboard()
        if playersturn == 1:
            nextmove = raw_input("Your Move %s ? " % (player1))
            if board[(int(nextmove)-1)] == nextmove:
                board[(int(nextmove)-1)] = "X"
                if iswinner("X"):
                    gamewon = True
                    winner = player1
                    break
                playersturn = 0
                movesplayed = movesplayed+1
            else:
                print "the space has been taken"
        else:
            if player2.lower() == "python":
                nextmove = str(random.randrange(1,9))
                print "Pythons move was %s " % (nextmove)
            else:
                nextmove = raw_input("Your Move %s ? " % (player2))
            if board[(int(nextmove)-1)] == nextmove:
                board[(int(nextmove)-1)] = "0"
                if iswinner("0"):
                    gamewon = True
                    winner = player2
                    break
                playersturn = 1
                movesplayed = movesplayed+1
            else:
                print "the space has been taken"
    if gamewon:
        print "congratulatisions %s you won this game" % winner
        print
    else:
        print "Oh well %s the game with %s was a draw....." % (player1,player2)
        print
    print
   
    if  raw_input("Play again? ( Y or N) ").lower() == 'n':
        game = 1
   
print "Good bye!"

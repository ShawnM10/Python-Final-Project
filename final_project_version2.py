grid = [[0,0,0],[0,0,0],[0,0,0]]

def get_state(grid, row, col):
    occupant = grid[col-1] ###This is because a list has a o index
    if occupant == 1:
        return 'X'
    if occupant == 2:
        return '0'
    return ' '

def set_state(grid, row, col, player):
    if player == 'X':
        occupant = 1
    else:
        occupant = 2
    grid[col-1][row-1] = occupant

def is_winner(grid):
    if grid[1][1] != 0:
        if grid[0][0] == grid[1][1]:        ##Top left to bottowm right
            if grid[2][2] == grid[1][1]:
                return True
        if grid[2][0] == grid[1][1]:        ##Top right to bottom left
            if grid[0][2] == grid[1][1]:
                return True
    for i in xrange(0, 3):
        if grid[0][i] != 0:
            if grid[0][i] == grid[1][i]:        ##Top left with middle
                if grid[0][i] == grid[2][i]:        
                    return True

        if grid[i][0] != 0:                     ###Top left to bottom
            if grid[i][0] == [i][1]:                ###Center down
                if grid[i][0] == grid[i][2]:        ###Right down
                    return True
    return False

def print_grid(grid):
    print_row(grid, 1)
    print '-----'
    print_row(grid, 2)
    print '-----'
    print_row(grid, 3)



def print_row(grid, row):
    output = get_state(grid, row, 1)
    output += '|' + get_state(grid, row, 2)
    output += '|' + get_state(grid, row, 3)
    print output

ongoing = True
current_player = 'X'
spaces = 9

while ongoing:
    print_grid(grid)
    print current_player + "'s turn"
    print "Column?"
    col = int(raw_input())
    print "Row?"
    row = int(raw_input())
    current = get_state(grid, row, col)
    if current != ' ':
        print "That space is occupied!"
    else:
        set_state(grid, row, col, current_player)
        spaces -= 1

        
        if is_winner(grid):
            print current_player + "Wins!"
            ongoing = False
        else:
            if current_player == 'X':
                current_player = '0'
            else:
                current_player = 'X'

        if spaces == 0:
            print "Stalemate!"
            ongoing = False
    
                
            

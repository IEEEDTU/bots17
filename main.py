"""
Main file of the project. All functions are to be defined here.
"""

# Board (11 * 11 matrix) initialized with 'U'
board = [['U' for i in range(0, 11)] for j in range(0, 11)]

# BoardHelp for Disjoint Set Matrix
# 0 for 'U', 1 for 'R', 2 for 'B'
boardHelp = [[0 for i in range(0, 11)] for j in range(0, 11)]


# This function checks whether a new piece can be placed or not.
def is_valid_move(x, y):
    if 0 <= x < 11 and 0 <= y < 11 and board[x][y] == 'U':
        return True
    else:
        return False


# This functions first checks for validity of new move and then
# update Board with new move.
def move(x, y, color):
    if is_valid_move(x, y):
        global board, boardHelp
        board[x][y] = color
        if color == 'R':
            boardHelp[x][y] = 1
        else:
            boardHelp[x][y] = 2

        if check_winning(color):
            print(color + " wins!")

        return True
    else:
        return False


# This function checks if any player is winning or not.
# TODO: check_winning()
def check_winning(color):
    if color == 'R':
        for i in range(0, 11):
            if boardHelp[i][10] == 1:
                for j in range(0, 11):
                    if boardHelp[j][0] == 1:
                        return check_connected(i, 10, i, 10, 1)
        return False

    else:
        for i in range(0, 11):
            if boardHelp[10][i] == 2:
                for j in range(0, 11):
                    if boardHelp[0][j] == 2:
                        return check_connected(10, i, 10, i, 2)
        return False


def check_connected(x, y, xpar, ypar, col):
    retval = False
    if col == 1 and y == 0:
        return True
    if col == 2 and x == 0:
        return True

    if 0 <= x - 1 < 11 and retval is False and x - 1 != xpar:
        if boardHelp[x - 1][y] == col:
            retval = check_connected(x - 1, y, x, y, col)
        else:
            retval = False

    if 0 <= x - 1 < 11 and 0 <= y + 1 < 11 and retval is False and (x - 1 != xpar or y + 1 != ypar):
        if boardHelp[x - 1][y + 1] == col:
            retval = check_connected(x - 1, y + 1, x, y, col)
        else:
            retval = False

    if 0 <= x + 1 < 11 and retval is False and x + 1 != xpar:
        if boardHelp[x + 1][y] == col:
            retval = check_connected(x + 1, y, x, y, col)
        else:
            retval = False

    if 0 <= x + 1 < 11 and 0 <= y - 1 < 11 and retval is False and (x + 1 != xpar or y - 1 != ypar):
        if boardHelp[x + 1][y - 1] == col:
            retval = check_connected(x + 1, y - 1, x, y, col)
        else:
            retval = False

    if 0 <= y - 1 < 11 and retval is False and ypar != y - 1:
        if boardHelp[x][y - 1] == col:
            retval = check_connected(x, y - 1, x, y, col)
        else:
            retval = False

    if 0 <= y + 1 < 11 and ypar != y + 1 and retval is False:
        if boardHelp[x][y + 1] == col:
            retval = check_connected(x, y + 1, x, y, col)
        else:
            retval = False
    return retval

# This function drives the program and plays the game.
# TODO: main function()

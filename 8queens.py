"""This programme solves the problem of putting 8 queens in chess game board(8*8)"""
# knowing that each queen will need to be placed so that there is no queen on its
# vertical, horizontal or diagonal lines.
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

total = 0
def print_board():
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=" ")
        print()


def can_place(x, y):
    """Check every position possible to place"""
    for i in range(y):
        if board[x][i] == 1:
            return False
    for i in range(x):
        if board[i][y] == 1:
            return False
    # check '/' diagonal line
    for i in range(x):
        if x+y-i < 8 and board[i][x+y-i]==1:
            return False
    # check '\' diagonal line
    # for i in range(1,x):
    #     if board[x-i][y-i] == 1:
    #         return False
    for index,i in enumerate(range(x-1,-1,-1)):
        s_y = y-(index+1)
        if s_y >= 0:
            if board[i][s_y] == 1:
                return False
    return True


def put_queens(step):
    """put in steps, each step is a row for one queen"""
    if step == 8:
        """exit loop when put 8, print board"""
        global total
        total+=1
        print("Method Number :", total)
        print_board()
        print("================")
        return

    for i in range(8):
        if can_place(step, i):
            # 1. Setting the queen, update board
            board[step][i] = 1
            # 2. Recurrence
            put_queens(step+1)
            # 3. Restore the action
            board[step][i] = 0


if __name__ =="__main__":
    put_queens(0)
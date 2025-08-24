import consts
import random

board = []

def rows_in_board():
    for i in range(consts.ROWS):
        board.append([])
    return board

def cols_in_rows():
    board = rows_in_board()
    for i in range(consts.ROWS):
        for j in range(consts.COLS):
            board[i].append("empty")
    return board


def mines_location():
    mine_index_list = []
    board = cols_in_rows()
    while len(mine_index_list) < 20:
        mine_row = random.randrange(consts.ROWS)
        mine_col = random.randrange(3, consts.COLS-3)
        empty_count = 0
        for j in range(3):
            if board[mine_row][mine_col+j] == "empty":
                empty_count += 1
        if empty_count == 3:
            for k in range(3):
                board[mine_row][mine_col] = "mine"
                mine_col += 1
            mine_index = (mine_row, mine_col)
            mine_index_list.append(mine_index)
    return mine_index_list

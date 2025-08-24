import consts
import random

board = []

def create_board():
    board = []
    for i in range(25):
        row = []
        for j in range(50):
            row.append('empty')
        board.append(row)
    return board


def mines_location():
    mine_index_list = []
    board = create_board()
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
# 프로그래머스 혼자서 하는 틱택토

def solution(board):
    o_cnt = 0
    x_cnt = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o_cnt += 1
            elif board[i][j] == "X":
                x_cnt += 1

    valid = o_cnt - x_cnt

    if valid < 0 or valid > 1:
        return 0

    o_win = 0
    x_win = 0

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "O":
                o_win = 1
            elif board[i][0] == "X":
                x_win = 1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "O":
                o_win = 1
            elif board[0][i] == "X":
                x_win = 1

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "O":
            o_win = 1
        elif board[0][0] == "X":
            x_win = 1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "O":
            o_win = 1
        elif board[0][2] == "X":
            x_win = 1

    if o_win and x_win:
        return 0
    if x_win and valid:
        return 0
    if o_win and valid != 1:
        return 0

    return 1
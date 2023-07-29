# 백준 2580 스도쿠
# https://www.acmicpc.net/problem/2580

from collections import defaultdict


def square_number(r,c):
    if not r//3:
        return c//3+1
    if r//3 == 1:
        return c//3+4
    if r//3 == 2:
        return c//3+7


def solve(r,c):
    if r == 9:
        for i in range(9):
            print(*sudoku[i])
        exit()

    next_r, next_c = r, c+1
    if next_c == 9:
        next_r = r+1
        next_c = 0

    if sudoku[r][c]:
        solve(next_r, next_c)

    if not sudoku[r][c]:
        s_num = square_number(r,c)

        for i in range(1,10):
            if i not in x[r] and i not in y[c] and i not in square[s_num]:
                sudoku[r][c] = i
                x[r].append(i)
                y[c].append(i)
                square[s_num].append(i)
                solve(next_r,next_c)
                sudoku[r][c] = 0
                x[r].pop()
                y[c].pop()
                square[s_num].pop()


sudoku = [list(map(int,input().split())) for _ in range(9)]
x = defaultdict(list)
y = defaultdict(list)
square = defaultdict(list)

for i in range(9):
    for j in range(9):
        if sudoku[i][j]:
            x[i].append(sudoku[i][j])
            y[j].append(sudoku[i][j])
            square[square_number(i,j)].append(sudoku[i][j])

solve(0,0)
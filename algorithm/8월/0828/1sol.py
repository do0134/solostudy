# 백준 3085 사탕 게임
# https://www.acmicpc.net/problem/3085

n = int(input())
bomboni = [list(input()) for _ in range(n)]
answer = 0


def check(r,c):
    global answer
    x_cnt = 1
    y_cnt = 1

    for x in range(n-1):
        if bomboni[r][x] == bomboni[r][x+1]:
            x_cnt += 1
        else:
            x_cnt = 1

        if bomboni[x][c] == bomboni[x+1][c]:
            y_cnt += 1
        else:
            y_cnt = 1

        answer = max(answer, x_cnt, y_cnt)


def swap(r,c):
    global answer
    for sr, sc in ((1,0),(0,1)):
        nr,nc = r+sr,c+sc
        if 0 <= nr < n and 0 <= nc < n:
            temp1 = bomboni[r][c]
            temp2 = bomboni[nr][nc]
            bomboni[r][c] = temp2
            bomboni[nr][nc] = temp1
            check(r,c)
            check(nr,nc)
            bomboni[r][c] = temp1
            bomboni[nr][nc] = temp2

        if answer == n:
            print(answer)
            return True
    return False


for i in range(n):
    for j in range(n):
        if swap(i,j):
            exit()
print(answer)

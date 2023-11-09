# 백준 2239 스도쿠

def dfs(r,c,arr):
    global flag
    if flag:
        return
    if c == 9:
        r += 1
        c = 0
        if r == 9:
            flag = True
            for i in arr:
                print(("").join(i))
            return

    if arr[r][c] != "0":
        dfs(r,c+1,arr)
    else:
        for i in range(1,10):
            if check(r,c,i,arr):
                arr[r][c] = str(i)
                dfs(r,c+1,arr)
                arr[r][c] = "0"


def check(r,c,value,arr):
    global sudoku
    for i in range(9):
        if arr[i][c] == str(value) and i != r:
            return False

    for i in range(9):
        if arr[r][i] == str(value) and i != c:
            return False

    if r // 3 == 1:
        r1 = 3
    elif r // 3 == 2:
        r1 = 6
    else:
        r1 = 0
    if c // 3 == 1:
        c1 = 3
    elif c // 3 == 2:
        c1 = 6
    else:
        c1 = 0

    for i in range(r1,r1+3):
        for j in range(c1,c1+3):
            if arr[i][j] == str(value) and (i != r and j != c):
                return False

    return True


sudoku = list()
for _ in range(9):
    temp = list(input())
    sudoku.append(temp)

flag = False
answer = list()
dfs(0,0,sudoku)

from collections import deque

r, c = map(int,input().split())
arr = [list(input()) for _ in range(r)]
n = int(input())
stick = list(map(int,input().split()))

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def bfs(cr, cc) :
    arr[cr][cc] = "."

    if not check(cr,cc) :
        return

    q = deque()
    q.append((cr,cc))
    while q :
        x, y = q.popleft()
        if not check(x,y) :
            arr[x][y] = "."
            arr[x-1][y] = "x"
            continue



def check(cr, cc) :
    value = list()
    for d in range(4) :
        nr, nc = dr[d] + cr, dc[d] + cc
        if 0 <= nr < r and 0 <= nc < c and arr[nr][nc] == "x" :
            value.append((nr,nc))
    return value


for i in range(n) :
    for j in range(c) :
        if arr[stick[i]][j] == "x" :
            bfs(i,j)
            break

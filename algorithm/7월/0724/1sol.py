# 백준 4179 불!
# https://www.acmicpc.net/problem/4179

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def bfs():
    global flag
    next_j = deque()
    while jihun:
        cr, cc = jihun.popleft()
        if arr[cr][cc] == "F":
            continue
        for d in range(4):
            nr, nc = dr[d]+cr, dc[d]+cc
            if not (0 <= nr < n and 0 <= nc < m):
                flag = True
                return [], []
            else:
                if arr[nr][nc] != "F" and arr[nr][nc] != "#" and not v[nr][nc]:
                    next_j.append((nr,nc))
                    v[nr][nc] = 1

    next_fire = deque()
    while fire:
        cr, cc = fire.popleft()
        for d in range(4):
            nr, nc = dr[d]+cr, dc[d]+cc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc]!= "F" and arr[nr][nc] != "#":
                arr[nr][nc] = "F"
                next_fire.append((nr,nc))

    return [next_j, next_fire]


n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
v = [[0]*m for _ in range(n)]

jihun = deque()
fire = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == "J":
            jihun.append((i,j))
            arr[i][j] = "#"
        if arr[i][j] == "F":
            fire.append((i,j))

answer = 1
flag = False
while True:
    jihun, fire = bfs()
    if not jihun and not fire:
        break
    answer += 1
if flag:
    print(answer)
else:
    print("IMPOSSIBLE")
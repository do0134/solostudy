# 백준 14940 쉬운 최단거리

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = [[int(1e9)]*m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i,j,0))
            answer[i][j] = 0
        if not arr[i][j]:
            answer[i][j] = 0

while q:
    cr,cc,cnt = q.popleft()
    for d in range(4):
        nr,nc = cr+dr[d], cc+dc[d]
        if 0 <= nr < n and 0 <= nc < m and answer[nr][nc] > cnt+1:
            q.append((nr,nc,cnt+1))
            answer[nr][nc] = cnt+1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and answer[i][j] == int(1e9):
            answer[i][j] = -1
    print(*answer[i])
# 백준 17086 아기 상어2

from collections import deque

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0

baby_shark = list()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            baby_shark.append((i,j))
            arr[i][j] = -1

dr = [1,1,1,0,-1,-1,-1,0]
dc = [1,0,-1,-1,-1,0,1,1]

for r, c in baby_shark:
    q = deque()
    q.append((r,c,0))
    while q:
        cr, cc, cnt = q.popleft()
        for d in range(8):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < n and 0 <= nc < m and (arr[nr][nc] > cnt+1 or not arr[nr][nc]):
                q.append((nr,nc,cnt+1))
                arr[nr][nc] = cnt + 1

answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != -1:
            answer = max(answer, arr[i][j])

print(answer)

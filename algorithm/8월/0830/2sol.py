# 백준 16929 Two Dots

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n,m = map(int,input().split())
v = [[0]*m for _ in range(n)]
arr = [list(input()) for _ in range(n)]


def dfs(r,c) -> bool:
    q = deque()
    q.append((r,c,-1,-1))
    v[r][c] = 1
    while q:
        cr, cc, pr, pc = q.pop()
        for d in range(4):
            nr,nc = cr+dr[d],cc+dc[d]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == arr[cr][cc]:
                if not v[nr][nc]:
                    q.append((nr,nc,cr,cc))
                    v[nr][nc] = 1
                elif v[nr][nc] and pr == nr and pc == nc:
                    continue
                elif v[nr][nc]:
                    return True

    return False


for i in range(n):
    for j in range(m):
        if not v[i][j]:
            if dfs(i,j):
                print("Yes")
                exit()

print("No")

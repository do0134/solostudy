# 백준 2667 단지번호붙이기
# https://www.acmicpc.net/problem/2667

from collections import deque, defaultdict

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n = int(input())
maps = [list(input()) for _ in range(n)]
v = [[0]*n for _ in range(n)]
answer = list()


def bfs(r,c):
    q = deque()
    q.append((r,c))
    v[r][c] = 1
    cnt = 1

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < n and 0 <= nc < n and maps[nr][nc] == "1" and not v[nr][nc]:
                cnt += 1
                q.append((nr,nc))
                v[nr][nc] = 1

    answer.append(cnt)


for i in range(n):
    for j in range(n):
        if maps[i][j] == "1" and not v[i][j]:
            bfs(i,j)


answer.sort()
print(len(answer))
for i in answer:
    print(i)

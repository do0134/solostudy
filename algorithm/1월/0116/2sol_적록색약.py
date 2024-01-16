# 백준 10026 적록색약

from collections import deque
import sys
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def bfs(r,c,people):
    color = picture[r][c]
    q = deque()
    q.append((r,c))

    if people == "normal":
        v = v_normal
    else:
        v = v_red_green

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr,nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < n and 0 <= nc < n and not v[nr][nc]:
                if people == "normal" and color == picture[nr][nc]:
                    q.append((nr,nc))
                    v[nr][nc] = 1
                elif people == "red_green" and color == picture[nr][nc]:
                    q.append((nr, nc))
                    v[nr][nc] = 1
                elif people == "red_green" and ((color == "R" or color =="G") and (picture[nr][nc] == "R" or picture[nr][nc] == "G")):
                    q.append((nr,nc))
                    v[nr][nc] = 1


n = int(input())
picture = [list(input()) for _ in range(n)]

v_normal = [[0]*n for _ in range(n)]
v_red_green = [[0]*n for _ in range(n)]
answer = [0,0]

for i in range(n):
    for j in range(n):
        if not v_normal[i][j]:
            bfs(i,j,"normal")
            answer[0] += 1
        if not v_red_green[i][j]:
            bfs(i,j,"red_green")
            answer[1] += 1

print(*answer)
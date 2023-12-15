# https://www.acmicpc.net/problem/1109 못풂 - 문제 잘못읽었다...

from collections import defaultdict, deque

n,m = map(int,input().split())
maps = [list(input()) for _ in range(n)]
v = [[0]*m for _ in range(n)]

dr = [1,-1,0,0,1,1,-1,-1]
dc = [0,0,1,-1,1,-1,1,-1]

island = defaultdict(list)
idx = 1


def bfs():
    global idx
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "x" and not v[i][j]:
                q = deque()
                q.append((i,j))
                v[i][j] = idx
                island[idx].append((i,j))
                while q:
                    cr, cc = q.popleft()
                    for d in range(8):
                        nr,nc = cr+dr[d],cc+dc[d]
                        if 0<= nr < n and 0 <= nc < m and not v[nr][nc] and maps[nr][nc] == "x":
                            q.append((nr,nc))
                            v[nr][nc] = idx
                            island[idx].append((nr,nc))
                idx += 1


def check_height(now_island, now_idx):
    que = deque(now_island)
    visit = [[0]*m for _ in range(n)]
    while que:
        cr, cc = que.popleft()
        for d in range(4):
            nr,nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                if not visit[nr][nc] and (maps[nr][nc] == "." or v[nr][nc] == now_idx):
                    que.append((nr,nc))
                    visit[nr][nc] = 1
            else:
                return True
    return False


bfs()

if idx == 1:
    print(-1)
else:
    answer = [0]
    check = defaultdict(bool)
    height = 0
    cnt = 0
    while cnt != idx-1:
        for i in range(1,idx):
            if check_height(island[i], i):
                check[i] = True
                answer[height] += 1
                cnt += 1

        height += 1
        answer.append(0)

    if not answer[-1]:
        answer.pop()
    print(*answer)
# 백준 1109 섬
# https://www.acmicpc.net/problem/1109

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


def check_out_boundary(now_island, now_idx):
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


def check_inside(out_island:list,current_idx:int, parent:int, same_height:set):
    q = deque()
    visit = [[0]*m for _ in range(n)]
    q.append(out_island[0])
    inside_island = set()
    value = 1

    while q:
        cr, cc= q.popleft()
        for d in range(4):
            nr,nc = cr+dr[d], cc+dc[d]
            if 0<= nr < n and 0<= nc < m and not visit[nr][nc]:
                if maps[nr][nc] == ".":
                    visit[nr][nc] = 1
                    q.append((nr,nc))
                elif v[nr][nc] == current_idx:
                    visit[nr][nc] = 1
                    q.append((nr,nc))
                elif v[nr][nc] != parent and v[nr][nc] not in same_height and not second_check[v[nr][nc]]:
                    inside_island.add(v[nr][nc])

    second_check[current_idx] = True
    max_v = 0
    for next_island in inside_island:
        max_v = max(check_inside(island[next_island], next_island, current_idx, inside_island),max_v)
    value += max_v
    height[current_idx] = value - 1

    return value


bfs()

if idx == 1:
    print(-1)
else:
    check = defaultdict(bool)
    height = defaultdict(int)
    second_check = [0]*idx
    for i in range(1,idx):
        if check_out_boundary(island[i], i):
            check[i] = True
            second_check[i] = 1

    h = 0
    for i in range(1,idx):
        if check[i]:
            h = max(check_inside(island[i],i,-1,set()), h)

    answer = [0]*h
    for i in range(1,idx):
        answer[height[i]] += 1

    print(*answer)
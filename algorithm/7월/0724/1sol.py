# 백준 4179 불!
# https://www.acmicpc.net/problem/4179

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]


# 지훈이 가능한 좌표 bfs
def bfs_jihun():
    global flag
    # 다음 좌표를 저장할 데크
    next_j = deque()

    while jihun:
        cr, cc = jihun.popleft()
        if arr[cr][cc] == "F":
            continue

        for d in range(4):
            nr, nc = dr[d]+cr, dc[d]+cc
            # 만약 탈출한다면 빈 리스트를 return한다.
            if not (0 <= nr < n and 0 <= nc < m):
                # 탈출 성공했다면 깃발을 든다.
                flag = True
                return []
            else:
                # 아니라면 불, 벽이 아닌 장소, 방문하지 않은 장소를 방문한다.
                if arr[nr][nc] != "F" and arr[nr][nc] != "#" and not v[nr][nc]:
                    next_j.append((nr,nc))
                    v[nr][nc] = 1
    return next_j


# 다음 불나는 곳 bfs
def bfs_fire():
    # 1분 뒤 불나는 곳을 담을 데크
    next_fire = deque()

    while fire:
        cr, cc = fire.popleft()
        for d in range(4):
            nr, nc = dr[d]+cr, dc[d]+cc
            # 이미 불이 난 곳이나, 벽이 아니라면 불을 낸다.
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != "F" and arr[nr][nc] != "#":
                arr[nr][nc] = "F"
                next_fire.append((nr,nc))

    return next_fire


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
# 1분씩 흘리면서, 다음 지훈이 좌표와 다음 불 좌표를 계속 얻는다.
while True:
    jihun = bfs_jihun()
    fire = bfs_fire()
    # 만약, 가능한 지훈이의 좌표가 없다면 멈춘다.
    if not jihun:
        break
    answer += 1

# 깃발이 들려있으면 탈출함
if flag:
    print(answer)
else:
    print("IMPOSSIBLE")
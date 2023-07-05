# 백준 2234 성곽
# https://www.acmicpc.net/problem/2234

from collections import defaultdict, deque


# 벽만들기
def make_wall(num):
    wall = list()
    if num >= 8:
        num -= 8
    else:
        wall.append(3)
    if num >= 4:
        num -= 4
    else:
        wall.append(2)
    if num >= 2:
        num -= 2
    else:
        wall.append(1)
    if num >= 1:
        num -= 1
    else:
        wall.append(0)
    return wall


# bfs로 방 구하기
def bfs(r,c):
    q = deque()
    q.append((r,c))
    size = 1
    v[r][c] = 1

    while q:
        cr, cc = q.popleft()
        for d in arr[cr][cc]:
            nr, nc = dr[d]+cr, dc[d]+cc
            if 0 <= nr < n and 0 <= nc < m and not v[nr][nc]:
                size += 1
                q.append((nr,nc))
                v[nr][nc] = 1
                room_info[nr][nc] = idx
    return size


# 벽 부수기
def break_wall(r,c):
    max_v = room_size[room_info[r][c]]
    for i in range(4):
        if i not in arr[r][c]:
            nr,nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if room_info[r][c] == room_info[nr][nc]:
                    continue
                else:
                    max_v = max(max_v,room_size[room_info[r][c]] + room_size[room_info[nr][nc]])
    return max_v

dr = [0,-1,0,1]
dc = [-1,0,1,0]

m, n = map(int,input().split())
arr = [[] for _ in range(n)]
castle = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]

# 벽 정보 저장하기
for i in range(n):
    for j in range(m):
        arr[i].append(make_wall(castle[i][j]))

# 몇번 방인지 저장하는 배열
room_info = [[0]*m for _ in range(n)]
# 방 사이즈 딕셔너리
room_size = defaultdict(int)
# 딕셔너리들의 key + 1번 답
idx = 0
# 2번 답
max_size = 0
# 방 정보 저장하기
for i in range(n):
    for j in range(m):
        if not v[i][j]:
            idx += 1
            room_info[i][j] = idx
            size = bfs(i,j)
            room_size[idx] = size
            max_size = max(size, max_size)

print(idx)
print(max_size)

answer = max_size
for i in range(n):
    for j in range(m):
        if 0 <= i-1 and room_info[i][j] != room_info[i-1][j]:
            answer = max(answer, room_size[room_info[i][j]] + room_size[room_info[i-1][j]])
        if 0 <= j-1 and room_info[i][j] != room_info[i][j-1]:
            answer = max(answer, room_size[room_info[i][j]] + room_size[room_info[i][j-1]])
        # next_size = break_wall(i,j)
        # answer = max(answer, next_size)

print(answer)
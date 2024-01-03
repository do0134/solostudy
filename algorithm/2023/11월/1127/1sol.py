# 백준 2573 빙산

from collections import deque


dr = [1,-1,0,0]
dc = [0,0,1,-1]

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]


def set_first(arr):
    q = deque()
    ice = dict()
    flag = False

    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                q.append((i,j))
                ice[(i, j)] = int(1e9)
                flag = True
                break
        if flag:
            break

    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr,nc = dr[d]+cr, dc[d]+cc
            if 0 <= nr < n and 0 <= nc < m and not ice.get((nr,nc)) and arr[nr][nc]:
                q.append((nr,nc))
                ice[(nr,nc)] = int(1e9)

    for i in range(n):
        for j in range(m):
            if not ice.get((i,j)) and arr[i][j]:
                return {}

    for key in ice.keys():
        r, c = key
        ice[key] = 0
        for d in range(4):
            nr,nc = r+dr[d], c+dc[d]
            if not arr[nr][nc]:
                ice[key] += 1

    return ice


def melt(arr, ice):
    cnt = len(ice.keys())
    for key in ice.keys():
        r,c = key
        if arr[r][c] <= ice[key]:
            arr[r][c] = 0
            cnt -= 1
        else:
            arr[r][c] -= ice[key]

    return arr, ice, cnt


def check(arr, ice, cnt):
    v = dict()
    q = deque()
    for key in ice.keys():
        r,c = key
        if arr[r][c]:
            q.append((r,c))
            v[(r,c)] = int(1e9)
            break

    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < n and 0 <= nc < m and not v.get((nr,nc)) and arr[nr][nc]:
                q.append((nr,nc))
                v[(nr,nc)] = int(1e9)

    if cnt != len(v.keys()):
        return True, v

    for key in v.keys():
        r, c = key
        v[key] = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not arr[nr][nc]:
                v[key] += 1

    return False, v


ice = set_first(arr)
if not ice:
    print(0)
else:
    i = 1

    while True:
        arr, ice, cnt = melt(arr, ice)
        if not cnt:
            print(0)
            break
        c, v = check(arr, ice, cnt)
        if c:
            print(i)
            break
        else:
            ice = v
        i += 1



"""
5 5
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0

4 4
0 0 0 0
0 3 1 0
0 1 3 0
0 0 0 0

5 7
0 0 0 0 0 0 0
0 3 3 2 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0

5 7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 10 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0

7 7
0 0 0 0 0 0 0
0 1 1 0 1 1 0
0 1 9 1 9 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 1 1 1 0 0
0 0 0 0 0 0 0

7 9
0 0 0 0 0 0 0 0 0
0 9 5 5 5 5 5 9 0
0 5 9 5 5 5 9 5 0
0 5 5 9 1 9 5 5 0
0 5 9 5 5 5 9 5 0
0 9 5 5 5 5 5 9 0
0 0 0 0 0 0 0 0 0

5 5
0 0 0 0 0
0 0 9 0 0
0 0 3 1 0
0 0 9 0 0
0 0 0 0 0
"""
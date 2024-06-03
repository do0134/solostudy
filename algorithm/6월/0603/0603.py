# 백준 7569 토마토

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

m,n,h = map(int,input().split())

arr = list()
for _ in range(h):
    arr.append([])
    for i in range(n):
        arr[_].append(list(map(int,input().split())))

q= deque()

dr = [1,-1,0,0,0,0]
dc = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1]

v = defaultdict(bool)
q = deque()
z_cnt = 0


for i in range(h):
    for j in range(n):
        for p in range(m):
            if arr[i][j][p] == 1:
                q.append((i,j,p,0))
                v[(i,j,p)] = True
            elif not arr[i][j][p]:
                z_cnt += 1

day = 0

while q:
    ch, cr, cc, cd = q.popleft()
    day = max(day, cd)
    for d in range(6):
        nh, nr, nc = dh[d] + ch, dr[d] + cr, dc[d] + cc
        if 0 <= nh < h and 0 <= nr < n and 0 <= nc < m and not v[(nh,nr,nc)] and not arr[nh][nr][nc]:
            arr[nh][nr][nc] = 1
            q.append((nh,nr,nc,cd+1))
            z_cnt -= 1
            v[(nh,nr,nc)] = True
    
if z_cnt > 0:
    print(-1)
else:
    print(day)
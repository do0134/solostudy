# 백준 16926 배열돌리기1

import sys
from collections import defaultdict

input = sys.stdin.readline

n,m,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
square = n//2


def solve(r,c,idx):
    total = 0
    cnt = defaultdict(tuple)
    division = 0
    while not v[r][c]:
        cnt[total] = (r,c,arr[r][c])
        total += 1
        v[r][c] = 1
        if not division:
            if r+1 <= n-1-idx:
                r += 1
            else:
                division += 1
                c += 1
        elif division == 1:
            if c+1 <= m-1-idx:
                c += 1
            else:
                division += 1
                r -= 1
        elif division == 2:
            if r-1 >= idx:
                r -= 1
            else:
                c -= 1
                division = 3
        elif division == 3:
            if c-1 >= idx:
                c -= 1
            else:
                division = 0
                break

    next_r = R%total

    for i in range(total):
        if i + next_r < total:
            next_idx = i+next_r
        else:
            next_idx = i+next_r-total

        nr,nc = cnt[next_idx][0],cnt[next_idx][1]
        arr[nr][nc] = cnt[i][2]


idx = 0
for i in range(n):
    for j in range(m):
        if not v[i][j]:
            solve(i,j,idx)
            idx += 1

for i in arr:
    print(*i)
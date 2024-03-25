# 백준 14500 테트로미노

import sys
from collections import defaultdict
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n, m = map(int,input().split())

max_v = 0
arr = list()
answer = 0


for _ in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)
    max_v = max(max_v, max(temp))


def dfs(r,c):
    global answer
    stack = list()
    v = defaultdict(bool)
    stack.append((r,c,arr[r][c],1))
    v[(r,c)] = True

    while stack:
        cr, cc, value, cnt = stack.pop()
        if cnt == 4:
            answer = max(answer, value)
            continue
        if value + (4-cnt)*max_v <= answer:
            continue

        for d in range(4):
            nr,nc = dr[d] + cr, dc[d] + cc
            if 0 <= nr < n and 0 <= nc < m and not v[(nr,nc)]:
                v[(nr,nc)] = True
                stack.append((nr,nc,value+arr[nr][nc],cnt+1))


def square(r,c):
    global answer
    if r+1 < n and c+1 < m:
        answer = max(answer, arr[r][c]+arr[r+1][c]+arr[r][c+1]+arr[r+1][c+1])


def t_shape(r,c):
    global answer
    if r-1 >= 0 and r+1 < n:
        if c-1 >= 0:
            answer = max(answer, arr[r][c]+arr[r-1][c]+arr[r+1][c]+arr[r][c-1])
        if c+1 < m:
            answer = max(answer, arr[r][c]+arr[r-1][c]+arr[r+1][c]+arr[r][c+1])

    if c-1 >= 0 and c+1 < m:
        if r-1 >= 0:
            answer = max(answer, arr[r][c]+arr[r][c-1]+arr[r][c+1]+arr[r-1][c])
        if r+1 < n:
            answer = max(answer, arr[r][c]+arr[r][c-1]+arr[r][c+1]+arr[r+1][c])


for i in range(n):
    for j in range(m):
        square(i,j)
        t_shape(i,j)
        dfs(i,j)

print(answer)
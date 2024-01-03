# 백준 17090 미로 탈출하기

import sys

sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
v = [[0]*m for _ in range(n)]


def dfs(r,c):
    global v
    nr,nc = find_next(r,c)
    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        v[r][c] = 1
        return 1
    elif 0 <= nr < n and 0 <= nc < m and not v[nr][nc]:
        v[r][c] = -1
        v[r][c] = dfs(nr,nc)
        return v[r][c]
    elif 0 <= nr < n and 0 <= nc < m and v[nr][nc]:
        v[r][c] = v[nr][nc]
        return v[nr][nc]


def find_next(r,c):
    if arr[r][c] == "U":
        return U(r,c)
    elif arr[r][c] == "R":
        return R(r,c)
    elif arr[r][c] == "D":
        return D(r,c)
    elif arr[r][c] == "L":
        return L(r,c)


def D(r,c):
    return r+1,c


def L(r,c):
    return r,c-1


def R(r,c):
    return r,c+1


def U(r,c):
    return r-1,c


answer = 0
for i in range(n):
    for j in range(m):
        if not v[i][j]:
            v[i][j] = -1
            dfs(i,j)
        if v[i][j] == 1:
            answer += 1

print(answer)
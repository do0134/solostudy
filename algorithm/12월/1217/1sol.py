# 백준 17070 파이프 옮기기 1

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0

pipes1 = [(0, 1), (1, 1)]
pipes2 = [(1, 0), (1, 1)]
pipes3 = [(0, 1), (1, 0), (1, 1)]


def dfs(cr,cc,d):
    global answer
    if arr[n-1][n-1] == 1:
        return
    if cr == n-1 and cc == n-1:
        answer += 1
        return
    if not d:
        pipes = pipes1
    elif d == 1:
        pipes = pipes2
    else:
        pipes = pipes3

    for pipe in pipes:
        nr,nc = cr+pipe[0], cc+pipe[1]
        if pipe == (0,1):
            nd = 0
        elif pipe == (1,0):
            nd = 1
        else:
            nd = 2

        if nd != 2 and 0 <= nr < n and 0 <= nc < n and not arr[nr][nc]:
            dfs(nr,nc,nd)
        elif nd == 2 and 0 <= nr < n and 0 <= nc < n and not arr[nr][nc] and not arr[nr][nc-1] and not arr[nr-1][nc]:
            dfs(nr,nc,nd)


arr[0][0] = 1
arr[0][1] = 1
dfs(0,1,0)
print(answer)
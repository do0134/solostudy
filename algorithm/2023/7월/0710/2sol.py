# 백준 4485 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def solve(idx):
    n = int(input())
    if not n:
        exit()

    arr = [list(map(int,input().split())) for _ in range(n)]
    dp = [[int(1e9)]*n for _ in range(n)]
    q = deque()
    q.append((0,0,arr[0][0]))
    while q:
        cr,cc,cnt = q.popleft()
        for d in range(4):
            nr,nc = dr[d]+cr,dc[d]+cc
            if 0 <= nr < n and 0 <= nc < n:
                if dp[nr][nc] > cnt+arr[nr][nc]:
                    dp[nr][nc] = cnt+arr[nr][nc]
                    q.append((nr,nc,cnt+arr[nr][nc]))

    return f"Problem {idx}: {dp[n-1][n-1]}"

idx = 1
while True:
    print(solve(idx))
    idx += 1
# 백준 4485 녹색 옷 입은 애가 젤다지?

import heapq as hq
import sys
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def solve():
    dp = [[int(1e9)]*n for _ in range(n)]
    dp[0][0] = arr[0][0]
    heap = list()
    hq.heappush(heap, (dp[0][0],0,0))

    while heap:
        c_cost, cr, cc = hq.heappop(heap)
        if cr == n-1 and cc == n-1:
            return c_cost

        for d in range(4):
            nr,nc = dr[d]+cr, dc[d]+cc
            if 0 <= nr < n and 0 <= nc < n and dp[nr][nc] > c_cost+arr[nr][nc]:
                dp[nr][nc] = c_cost+arr[nr][nc]
                hq.heappush(heap,(dp[nr][nc],nr,nc))

idx = 1
while True:
    n = int(input())
    if not n:
        break

    arr = [list(map(int,input().split())) for _ in range(n)]
    print(f"Problem {idx}: {solve()}")
    idx += 1
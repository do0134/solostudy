# 백준 14284 간선 이어가기 2

import sys
import heapq as hq

input = sys.stdin.readline

n, m = map(int,input().split())
heap = list()

arr = [[] for _ in range(n+1)]
dp = [int(1e9)]*(n+1)

for _ in range(m):
    s,e,w = map(int,input().split())
    arr[s].append((w,e))
    arr[e].append((w,s))

S, T = map(int,input().split())
dp[S] = 0
hq.heappush(heap, (0,S))

while heap:
    cw, cc = hq.heappop(heap)

    for i in arr[cc]:
        if dp[i[1]] > dp[cc] + i[0] and dp[cc] + i[0] < dp[T]:
            dp[i[1]] = dp[cc] + i[0]
            hq.heappush(heap, i)

print(dp[T])

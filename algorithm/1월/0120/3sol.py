# 백준 1753 최단경로

import heapq as hq
import sys
input = sys.stdin.readline

V,E = map(int,input().split())
k = int(input())

graph = [[] for _ in range(V+1)]
dp = [int(1e9)]*(V+1)

heap = list()

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

hq.heappush(heap, (0,k))
dp[k] = 0

while heap:
    now_w, now_idx = hq.heappop(heap)

    for next_w, next_idx in graph[now_idx]:
        if dp[next_idx] > now_w+next_w:
            dp[next_idx] = now_w+next_w
            hq.heappush(heap,(now_w+next_w, next_idx))


for i in range(1,V+1):
    if dp[i] == int(1e9):
        print("INF")
    else:
        print(dp[i])
# 백준 1238 파티

import heapq as hq
import sys
input = sys.stdin.readline

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]


for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((w, e))
    rev_graph[e].append((w, s))


def find_road(start_idx, arr):
    dp = [int(1e9)]*(n+1)
    heap = list()
    dp[start_idx] = 0

    hq.heappush(heap, (0,start_idx))

    while heap:
        cw, c_idx = hq.heappop(heap)

        if cw > dp[c_idx]:
            continue

        for nw, n_idx in arr[c_idx]:
            next_w = nw+cw
            if dp[n_idx] > next_w:
                dp[n_idx] = next_w
                hq.heappush(heap, (next_w, n_idx))

    return dp


departure = find_road(x, rev_graph)
arrive = find_road(x, graph)

answer = 0

for i in range(1,n+1):
    answer = max(answer, departure[i]+arrive[i])

print(answer)
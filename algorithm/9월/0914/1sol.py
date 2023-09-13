# 백준 5972 택배 배송

import heapq as hq
from collections import defaultdict


n,m = map(int,input().split())
graph = defaultdict(list)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v = [int(1e9)]*(n+1)
v[1] = 0
heap = list()
hq.heappush(heap,(1,0))

while heap:
    idx, cow = hq.heappop(heap)

    for next_idx, next_cow in graph[idx]:
        if v[next_idx] > next_cow + cow:
            hq.heappush(heap,(next_idx, cow+next_cow))
            v[next_idx] = next_cow + cow

print(v[n])
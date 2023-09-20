# 백준 1446 지름길

import heapq as hq

n,d = map(int,input().split())
graph = [[] for _ in range(d+1)]
keys = set()
for _ in range(n):
    a,b,c = map(int,input().split())
    if b > d:
        continue
    graph[a].append([b,c])
    keys.add(a)

v = [int(1e9)]*(d+1)
v[0] = 1
heap = list()
hq.heappush(heap, (0,0))
keys = sorted(list(keys)) + [d]

while heap:
    start, dis = hq.heappop(heap)
    if v[start] < dis:
        continue

    for next_idx, short_dis in graph[start]:
        next_dis = short_dis + dis
        if v[next_idx] > next_dis:
            hq.heappush(heap,(next_idx, next_dis))
            v[next_idx] = next_dis

    for key in keys:
        next_dis = dis + key - start
        if 0 < next_dis < v[key] and key > start:
            hq.heappush(heap,(key,next_dis))
            v[key] = next_dis

print(v[-1])
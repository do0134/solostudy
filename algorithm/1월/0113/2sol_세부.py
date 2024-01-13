# 백준 13905 세부
# https://www.acmicpc.net/problem/13905

import sys
import heapq as hq
input = sys.stdin.readline

N,M = map(int,input().split())
S,E = map(int,input().split())

island = [[] for _ in range(N+1)]

for _ in range(M):
    h1,h2,k = map(int,input().split())
    island[h1].append((-k, h2))
    island[h2].append((-k, h1))

v = [0]*(N+1)
heap = list()
v[S] = 0

hq.heappush(heap, (-int(1e9), S))
answer = 0

while heap:
    min_w, now_idx = hq.heappop(heap)

    if now_idx == E:
        break

    for next_w, next_idx in island[now_idx]:
        weight = max(next_w, min_w)
        if v[next_idx] > weight:
            v[next_idx] = weight
            hq.heappush(heap, (weight, next_idx))

print(-v[E])
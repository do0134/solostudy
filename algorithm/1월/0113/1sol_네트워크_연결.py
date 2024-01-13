# 백준 1922 네트워크 연결
# https://www.acmicpc.net/problem/1922

import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
m = int(input())

network = [[] for _ in range(n+1)]


for _ in range(m):
    s,e,w = map(int,input().split())
    network[s].append((w,e))
    network[e].append((w,s))


v = [0]*(n+1)
heap = list()
v[1] = 0
hq.heappush(heap, (0,1))

answer = 0
edge = 0

while edge < n:
    now_cost, now_idx = hq.heappop(heap)
    if v[now_idx]:
        continue

    answer += now_cost
    edge += 1
    v[now_idx] = 1

    for next_cost, next_idx in network[now_idx]:
        if not v[next_idx]:
            hq.heappush(heap,(next_cost, next_idx))

print(answer)
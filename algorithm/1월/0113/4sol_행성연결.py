# 백준 16398 행성 연결
# https://www.acmicpc.net/problem/16398

import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
planets = list()

for i in range(n):
    planets.append(list(map(int,input().split())))

v = [0]*n
heap = list()
hq.heappush(heap, (0,0))
answer = 0

while heap:
    cost, now_idx = hq.heappop(heap)

    if v[now_idx]:
        continue

    v[now_idx] = 1
    answer += cost

    for next_idx, next_cost in enumerate(planets[now_idx]):

        if not v[next_idx]:
            hq.heappush(heap, (next_cost, next_idx))

print(answer)
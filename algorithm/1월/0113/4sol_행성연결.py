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
dp = [int(1e9)]*n
dp[0] = 0
answer = 0
edge = 0

while edge < n:
    cost, now_idx = hq.heappop(heap)

    if v[now_idx]:
        continue

    edge += 1
    v[now_idx] = 1
    answer += dp[now_idx]

    for next_idx, next_cost in enumerate(planets[now_idx]):
        if not v[next_idx] and dp[next_idx] > next_cost:
            hq.heappush(heap, (next_cost, next_idx))
            dp[next_idx] = next_cost

print(answer)
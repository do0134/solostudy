# 백준 1766 문제집

import heapq as hq
import sys
from collections import defaultdict

input = sys.stdin.readline


n, m = map(int,input().split())

tree = [[] for _ in range(n+1)]
idx = defaultdict(int)
for _ in range(m):
    s,e = map(int,input().split())
    tree[s].append(e)
    idx[e] += 1


v = [0]*(n+1)

heap = list()
answer = list()

for i in range(1,n+1):
    if not idx[i]:
        hq.heappush(heap,i)
        v[i] = 1

while heap:
    value = hq.heappop(heap)
    answer.append(value)

    # TODO: 1. 해당 next value를 먼저 풀었을 때, 좋은 문제가 존재하는지

    for next_value in tree[value]:
        idx[next_value] -= 1
        if idx[next_value] <= 0:
            hq.heappush(heap, next_value)
            v[next_value] = 1


print(*answer)

"""
6 7
5 6
5 2
2 4
4 3
2 1
6 1
1 3

5 2 4 6 1 3
"""
# 백준 1927 최소 힙

import heapq as hq
import sys
input = sys.stdin.readline

heap = list()

n = int(input())

for _ in range(n):
    num = int(input())
    if not num and not heap:
        print(0)
    elif not num:
        print(hq.heappop(heap))
    else:
        hq.heappush(heap,num)
# 백준 11279 최대힙

import sys
import heapq

n = int(input())
arr = list()
for _ in range(n):
    i = int(sys.stdin.readline())
    if i :
        heapq.heappush(arr,(-i,i))
    else:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
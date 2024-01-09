# 백준 15903 카드 합체 놀이

import heapq as hq

n, m = map(int,input().split())
heap = list(map(int,input().split()))
hq.heapify(heap)

idx = 0

while idx < m:
    a = hq.heappop(heap)
    b = hq.heappop(heap)

    value = a+b

    for _ in range(2):
        hq.heappush(heap, a+b)

    idx += 1

print(sum(heap))
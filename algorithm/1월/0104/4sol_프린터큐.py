# 백준 1966 프린터큐
# https://www.acmicpc.net/problem/1966

from collections import deque
import heapq as hq

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))

    q = deque()
    heap = list()

    max_v = 0

    for i in range(n):
        q.append((arr[i],i))
        hq.heappush(heap,-arr[i])

    cnt = 0
    while q:
        importance, idx = q.popleft()
        if importance == -heap[0]:
            cnt += 1
            hq.heappop(heap)
            if idx == m:
                print(cnt)
                break

        else:
            q.append((importance,idx))
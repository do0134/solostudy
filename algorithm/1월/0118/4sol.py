# 백준 11000 강의실 배정

import heapq as hq

n = int(input())
room = list()

for _ in range(n):
    s,e = map(int,input().split())
    room.append((s,e))

room.sort(key=lambda x:x[1])
answer = 0
heap = list()

for i in range(n-1,-1,-1):
    s,e = room[i]
    while heap and -heap[0] >= e:
        hq.heappop(heap)

    hq.heappush(heap,-s)
    answer = max(answer, len(heap))

print(answer)

"""
6
1 3
2 5
7 8
4 12
9 10
7 11

3
"""
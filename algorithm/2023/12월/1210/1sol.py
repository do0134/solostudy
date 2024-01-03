# 백준 1379 강의실 2

import heapq, sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
lecture = list()
start = list()
room = defaultdict(int)

for _ in range(n):
    a,b,c = map(int,input().split())
    heapq.heappush(start, (b,c,a))


answer = 0
idx = 1

while start:
    s,e,l = heapq.heappop(start)

    if lecture and lecture[0][0] <= s:
        next_time = heapq.heappop(lecture)
        room[l] = next_time[1]
        heapq.heappush(lecture, (e, next_time[1]))
    else:
        answer += 1
        room[l] = idx
        heapq.heappush(lecture, (e, idx))
        idx += 1


print(answer)
for i in range(1,n+1):
    print(room[i])
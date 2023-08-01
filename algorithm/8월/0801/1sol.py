# softeer 지우는 소수를 좋아해
# https://softeer.ai/practice/info.do?idx=1&eid=582&sw_prbl_sbms_sn=230318

import sys
from collections import defaultdict
import heapq as hq

n,m = map(int,sys.stdin.readline().rstrip().split())
roads = defaultdict(list)

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    roads[a].append((b,c))
    roads[b].append((a,c))

v = [int(1e9)]*(n+1)
heap = list()
hq.heappush(heap,(1,0))
v[1] = 0

while heap:
    next_, level = hq.heappop(heap)

    for road, w in roads[next_]:
        next_level = max(level, w)
        if v[road] > next_level:
            hq.heappush(heap,(road, next_level))
            v[road] = next_level

for i in range(v[n]+1,v[n]*2):
    for j in range(2,int(i**0.5)+1):
        if not i % j:
            break
    else:
        print(i)
        break
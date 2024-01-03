# 백준 1277 발전소 설치

from collections import defaultdict
import heapq as hq
import sys
input = sys.stdin.readline


def calc(start: int or tuple, end: int or tuple) -> int or float:
    if type(start) == int:
        cr,cc = tree[start]
        nr,nc = tree[end]
    else:
        cr,cc = start
        nr,nc = end

    if cr == nr:
        return abs(cc-nc)
    elif cc == nc:
        return abs(cr-nr)
    else:
        return ((cr-nr)**2 + (cc-nc)**2)**0.5


N, W = map(int,input().split())
m = float(input())

heap = list()
tree = defaultdict(tuple)
graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
    r,c = map(int,input().split())
    tree[i] = (r,c)
    for j in range(1,i):
        w = calc(i,j)
        #if w <= m:
        graph[i].append([w,j])
        graph[j].append([w,i])

dp = [int(1e9)]*(N+1)

for _ in range(W):
    s,e = map(int,input().split())
    for i in graph[s]:
        if i[1] == e:
            i[0] = 0
            break
    for i in graph[e]:
        if i[1] == s:
            i[0] = 0
            break

dp[1] = 0
hq.heappush(heap,(0,1))

while heap:
    cw, n_idx = hq.heappop(heap)

    for nw, next_idx in graph[n_idx]:
        if dp[next_idx] > cw+nw:
            dp[next_idx] = cw+nw
            hq.heappush(heap,(cw+nw, next_idx))


print(int(dp[N]*1000))

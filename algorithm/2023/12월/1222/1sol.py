# 백준 11779 최소비용 구하기2

import heapq as hq

n = int(input())
m = int(input())

v = [int(1e9)]*(n+1)
times = [[] for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int,input().split())
    times[a].append((b,c))

s,e = map(int,input().split())

heap = list()
v[s] = 0
answer_city = [s]
answer_visited = 1

for first_time, first_cost in times[s]:
    hq.heappush(heap,(first_cost, first_time, [s, first_time], 2))
    if v[first_time] >= first_cost and e == first_time:
        v[first_time] = first_cost
        answer_city = [s, first_time]
        answer_visited = 2
    else:
        v[first_time] = min(v[first_time], first_cost)

while heap:
    cost, now, cities, prev = hq.heappop(heap)
    if cost >= v[e]:
        continue
    for next_city, next_cost in times[now]:
        if cost+next_cost < v[next_city]:
            if next_city == e:
                answer_city = cities + [next_city]
                v[next_city] = cost+next_cost
                answer_visited = prev+1
                continue
            v[next_city] = cost+next_cost
            hq.heappush(heap,(cost+next_cost, next_city, cities+[next_city],prev+1))

print(v[e])
print(answer_visited)
print(*answer_city)

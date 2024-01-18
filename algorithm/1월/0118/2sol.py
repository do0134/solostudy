# 백준 13305 주유소

n = int(input())
road = list(map(int,input().split()))
cost = list(map(int,input().split()))

answer = cost[0]*road[0]
min_v = cost[0]

for i in range(1,n-1):
    if cost[i] < min_v:
        min_v = cost[i]
    answer += min_v*road[i]

print(answer)
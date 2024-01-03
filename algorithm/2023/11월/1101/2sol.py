# 백준 13305 주유소

n = int(input())
road = list(map(int,input().split()))
cost = list(map(int,input().split()))

answer = 0
m = cost[0]

for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    answer += m*road[i]

print(answer)

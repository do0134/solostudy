# dp 문제 c명을 모으기 위한 최소 비용을 묻는 문제
# 그리디하게 풀 수도 있을 거 같지만, 조건이 너무 많아서 포기
# [c:]의 최솟값을 구하는게 중요했다. -> 실제로 해맸다. 왜냐면 2명 모으는데 100명 모아서 1원 들 수 있고, 2명 모아서 2원 들 수도 있는 경우가 생김

c,n = map(int,input().split())
city = list()
dp = [1e9]*(c+101)
dp[0] = 0
for _ in range(n):
    cost, people = map(int,input().split())
    city.append([cost,people])

city.sort()

for cost, people in city :
    for i in range(people,c+101):
        dp[i] = min(dp[i-people]+cost,dp[i])

print(min(dp[c:]))
# 백준 2631 줄세우기

n = int(input())
num = list()

for _ in range(n):
    num.append(int(input()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))
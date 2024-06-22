# 백준 13250 주사위 게임

n = int(input())
dp = [0]*1000001

for i in range(1,n+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] + dp[i-5] + dp[i-6]) / 6 + 1

print(dp[n])
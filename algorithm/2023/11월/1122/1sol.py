# 백준 14606 피자(small)

n = int(input())

dp = [0]*(n+1)

for i in range(2,n+1):
    if i%2:
        dp[i] = dp[i//2]+dp[i//2+1]+(i//2*(i//2+1))
    else:
        dp[i] = dp[i//2]*2+((i//2)**2)

print(dp[n])

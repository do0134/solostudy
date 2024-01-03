# 백준 11052 카드 구매하기

n = int(input())
arr = [0]+list(map(int,input().split()))
dp = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(arr[j]+dp[i-j],dp[i])

print(dp[n])
# 백준 1495 기타리스트

n,s,m = map(int,input().split())
arr = list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n)]

for i in range(n):
    if not i:
        if s+arr[0] <= m:
            dp[0][s+arr[0]] = 1
        if s-arr[0] >= 0:
            dp[0][s-arr[0]] = 1
    else:
        for j in range(m+1):
            if dp[i-1][j]:
                if j + arr[i] <= m:
                    dp[i][j+arr[i]] = 1
                if j - arr[i] >= 0:
                    dp[i][j-arr[i]] = 1

for i in range(m,-1,-1):
    if dp[n-1][i]:
        print(i)
        break
else:
    print(-1)
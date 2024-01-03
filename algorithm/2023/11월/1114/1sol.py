# 백준 2775 부녀회장이 될테야

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [[0]*n for _ in range(k+1)]

    for i in range(1,n+1):
        dp[0][i-1] = i

    for i in range(1,k+1):
        for j in range(1,n+1):
            dp[i][j-1] = sum(dp[i-1][:j])

    print(dp[k][n-1])
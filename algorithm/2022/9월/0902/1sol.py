n = int(input())
tri = list()
dp = [[0]*(i) for i in range(1,n+1)]
for _ in range(n):
    tri.append(list(map(int,input().split())))
dp[0][0] = tri[0][0]
for i in range(1,n):
    for j in range(i+1):
        if j == 0 :
            dp[i][j] = dp[i-1][j]+tri[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j]= max(dp[i-1][j-1]+tri[i][j],dp[i-1][j] + tri[i][j])
print(max(dp[n-1]))


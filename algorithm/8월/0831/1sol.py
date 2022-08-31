n,m = map(int,input().split())
memory = [0]+list(map(int,input().split()))
cost = [0]+list(map(int,input().split()))
total = sum(cost)
dp = [[0]*(total+1) for _ in range(n+1)]
answer = int(1e9)
for i in range(1,n+1):
    b = memory[i]
    c = cost[i]

    for j in range(1,total+1):
        if j < c :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-c]+b,dp[i-1][j])
        if dp[i][j] >= m:
            answer = min(answer,j)

if m :
    print(answer)
else:
    print(0)



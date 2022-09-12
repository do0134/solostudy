n = int(input())
m = int(input())
dp = [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    dp[s][e] = min(dp[s][e],w)

for i in range(1,n+1):
    for j in range(1,n+1):
        for p in range(1,n+1):
            if j == p :
                dp[j][p] = 0
            else:
                dp[j][p] = min(dp[j][p],dp[j][i]+dp[i][p])

for i in dp[1:]:
    answer = list()
    for j in i[1:]:
        if j == 1e9 :
            answer.append(0)
        else:
            answer.append(j)
    else:
        print(*answer)

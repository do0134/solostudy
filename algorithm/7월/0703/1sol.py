# 백준 10653 마라톤 2

n, k = map(int,input().split())
dp = [[int(1e9)]*n for _ in range(k+1)]
arr = [list(map(int,input().split())) for _ in range(n)]
distance = [[0]*n for _ in range(n)]


def calc_distance(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)


for i in range(n):
    for j in range(n):
        distance[i][j] = calc_distance(arr[i][0],arr[i][1],arr[j][0],arr[j][1])

dp[0][0] = 0

for i in range(1,n):
    dp[0][i] = dp[0][i-1] + distance[i-1][i]

for i in range(1,k+1):
    dp[i][0], dp[i][1] = 0, distance[i-1][1]
    dp[i][i] = distance[0][i]
    for j in range(1,n):
        for p in range(i,0,-1):
            if j-p-1 < 0:
                continue
            dp[i][j] = min(dp[i][j], dp[i-p][j-p-1]+distance[j][j-p-1],dp[i][j-1]+distance[j-1][j])

print(dp[-1][-1])
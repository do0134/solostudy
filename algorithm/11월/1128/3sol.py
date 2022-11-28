import sys

n,m = map(int,input().split())

arr = list()
arr2 = list()

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for _ in range(m):
    arr2.append(list(map(int,sys.stdin.readline().split())))

dp = [[0]*(n+1) for _ in range(n+1)]
dp[1][1] = arr[0][0]

for i in range(2,n+1):
    dp[i][1] = dp[i-1][1] + arr[i-1][0]
    dp[1][i] = dp[1][i-1] + arr[0][i-1]

for i in range(2,n+1) :
    for j in range(2,n+1) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i-1][j-1] - dp[i-1][j-1]

def solve(y1,x1,y2,x2):
    return dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1]



for w,x,y,z in arr2:
    print(solve(w,x,y,z))




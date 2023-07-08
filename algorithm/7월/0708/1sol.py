# 백준 1890 점프
# https://www.acmicpc.net/problem/1890

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1


def solve():
    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                continue
            for dr, dc in ((1,0), (0,1)):
                nr,nc = i+dr*arr[i][j], j+dc*arr[i][j]
                if 0 <= nr < n and 0 <= nc < n:
                    dp[nr][nc] += dp[i][j]


solve()
print(dp[n-1][n-1])
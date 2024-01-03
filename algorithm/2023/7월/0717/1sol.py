# 백준 2133 타일 채우기
# https://www.acmicpc.net/problem/2133

def solve(n):
    if n % 2:
        return 0
    dp = [0]*(n+2)
    dp[2] = 3
    for i in range(4,n+2,2):
        dp[i] = dp[i-2]*3 + sum(dp[:i-2]*2)+2
    return dp[n]


n = int(input())
print(solve(n))
# 백준 10942 팰린드롬?

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [[0]*n for _ in range(n)]

for l in range(1,n+1):
    for i in range(n-l+1):
        j = i + l -1
        if arr[i] == arr[j] and ( l == 1 or l == 2 or dp[i+1][j-1]):
            dp[i][j] = 1

m = int(input())

for _ in range(m):
    s,e = map(int,input().split())
    s -= 1
    e -= 1
    print(dp[s][e])
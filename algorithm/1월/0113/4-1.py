import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(map(int,input().split())))

answer = 0
v = [0]*n
dp = [int(1e9)]*n
dp[0] = 0

zero_cnt = n-1

for _ in range(n):
    if not zero_cnt:
        break

    idx = v.index(0)
    for i in range(n):
        if not v[i] and dp[i] < dp[idx]:
            idx = i

    zero_cnt -= 1
    v[idx] = 1

    for j in range(n):
        if not v[j] and arr[idx][j] < dp[j]:
            dp[j] = arr[idx][j]


print(sum(dp))
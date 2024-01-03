# 백준 2204 동전 2
# https://www.acmicpc.net/problem/2294

n,k = map(int,input().split())
coin = list()
for _ in range(n):
    coin.append(int(input()))

dp = [int(1e9)]*(k+1)
dp[0] = 0

for i in range(n):
    if coin[i] > k:
        continue
    dp[coin[i]] = 1

min_v = min(coin)
answer = 0
if min_v > k:
    answer = -1
else:
    for i in coin:
        for j in range(i,k+1):
            dp[j] = min(dp[j],dp[j-i]+1)

if not answer and dp[k] == int(1e9):
    answer = -1
elif not answer:
    answer = dp[k]

print(answer)
